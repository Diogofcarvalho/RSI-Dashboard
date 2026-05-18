import pandas as pd
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity
from factor_analyzer import FactorAnalyzer
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
df = pd.read_excel(r"C:\Users\dcdio\OneDrive - NOVAIMS\Tese_Mestrado\COPIA_DATA\Calculo_RSI.xlsx", sheet_name="Dados_Finais")

# 2. Criar variáveis derivadas
df["%_arrendados"] = df["Total Alojamentos Classicos Arrendamento"] / df["Total Alojamentos Clássicos"]
df["%_prazo_aloj_certo"] = df["Contrato com prazo certo"] / df["Total Alojamentos Classicos Arrendamento"]
df["%_indeterminado"] = df["Contrato de duração indeterminada"] / df["Total Alojamentos Classicos Arrendamento"]
df["taxa_desemprego"] = df["População Desempregada"] / df["Pop_Total"]
df["indice_envelhecimento"] = df["pop_mais_65"] / df["Pop_menor15"]
df["AL_por_1000_fogos"] = (
    df["Count_AirBNB"] / df["Total Alojamentos Clássicos"]
) * 1000


# 3. Selecionar variáveis para o índice
variaveis_indice = [
    "preco_m2",
    "Rend_Bruto_Anual",
    "%_arrendados",
 #   "%_prazo_aloj_certo",
    "taxa_desemprego",
    "AL_por_1000_fogos",
    "indice_envelhecimento",
    # POIs
   # "POI_Education",
   #"POI_Comercio",
   # "POI_Cultura",
   # "POI_Lazer",
   # "POI_Mobilidade",
   # "POI_Seguranca" 
]
# 5. Normalizar os dados
scaler = StandardScaler()
dados_normalizados = scaler.fit_transform(df[variaveis_indice])
df_normalizado = pd.DataFrame(dados_normalizados, columns=variaveis_indice)


# ============================================================
# AQUI: VALIDAÇÃO ESTATÍSTICA
# KMO, Bartlett e Variância Explicada
# ============================================================

from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity
from factor_analyzer import FactorAnalyzer
import numpy as np

df_validacao = df[variaveis_indice].replace([np.inf, -np.inf], np.nan).dropna()

dados_validacao_norm = scaler.fit_transform(df_validacao)
df_validacao_norm = pd.DataFrame(dados_validacao_norm, columns=variaveis_indice)

# KMO
kmo_all, kmo_model = calculate_kmo(df_validacao_norm)

print("\n================ KMO ================")
print(f"KMO geral: {kmo_model:.3f}")

kmo_variaveis = pd.Series(kmo_all, index=variaveis_indice).sort_values()
print("\nKMO por variável:")
print(kmo_variaveis)

# Bartlett
chi_square_value, p_value = calculate_bartlett_sphericity(df_validacao_norm)

print("\n=========== Bartlett's Test ===========")
print(f"Chi-square: {chi_square_value:.3f}")
print(f"p-value: {p_value:.5f}")

# Eigenvalues e Variância Explicada
fa_test = FactorAnalyzer(rotation=None)
fa_test.fit(df_validacao_norm)

eigenvalues, vectors = fa_test.get_eigenvalues()

df_eigen = pd.DataFrame({
    "Fator": [f"Fator {i+1}" for i in range(len(eigenvalues))],
    "Eigenvalue": eigenvalues,
    "Variância Explicada (%)": eigenvalues / eigenvalues.sum() * 100,
    "Variância Acumulada (%)": np.cumsum(eigenvalues / eigenvalues.sum() * 100)
})

print("\n======= Eigenvalues / Total Variance Explained =======")
print(df_eigen)

plt.figure(figsize=(8, 5))
plt.plot(range(1, len(eigenvalues) + 1), eigenvalues, marker="o")
plt.axhline(y=1, linestyle="--")
plt.title("Scree Plot - Eigenvalues")
plt.xlabel("Número do fator")
plt.ylabel("Eigenvalue")
plt.xticks(range(1, len(eigenvalues) + 1))
plt.tight_layout()
plt.show()


# 4. Análise de correlação entre variáveis (antes de normalizar)
plt.figure(figsize=(14, 10))
correlation_matrix = df[variaveis_indice].corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Matriz de Correlação entre Variáveis para o RSI")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()



# 6. Análise Fatorial (sem rotação)
fa = FactorAnalysis(n_components=1)
fator_1 = fa.fit_transform(df_normalizado)

loadings = pd.Series(fa.components_[0], index=variaveis_indice).sort_values(ascending=False)
print("Loadings (Factor 1):")
print(loadings)


weights_signed_pct = 100 * loadings / loadings.abs().sum()
print("\nWeights (signed, % of abs sum):")
print(weights_signed_pct)


weights_abs_pct = 100 * loadings.abs() / loadings.abs().sum()
print("\nImportance (absolute, %):")
print(weights_abs_pct)


df["RSI_Fator1"] = fator_1

# 8. Scale
df["RSI"] = (df["RSI_Fator1"] - df["RSI_Fator1"].min()) / (df["RSI_Fator1"].max() - df["RSI_Fator1"].min()) * 100

# 9. Visualizar os resultados
df_resultado = df[["Freguesias", "RSI"]].sort_values(by="RSI", ascending=False)
print(df_resultado)

# 10. Gráfico do índice RSI por freguesia
plt.figure(figsize=(12, 6))
sns.barplot(x="RSI", y="Freguesias", data=df_resultado, palette="Reds_r")
plt.title("Rental Stress Index (RSI) por Freguesia")
plt.xlabel("RSI (0-100)")
plt.ylabel("Freguesia")
plt.tight_layout()
plt.show()
# 11. Guardar resultados em ficheiro Excel
caminho_saida = r"C:\Users\dcdio\OneDrive - NOVAIMS\Tese_Mestrado\COPIA_DATA\RSI_por_Freguesia1.xlsx"

df_resultado.to_excel(
    caminho_saida,
    index=False,
    sheet_name="RSI_Freguesias"
)

print("Ficheiro Excel guardado com sucesso em:", caminho_saida)

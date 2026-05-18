# Identifying Rental Stress Zones in Lisbon  
## A Spatial Rental Stress Index for Housing Affordability

This repository contains the materials developed for my master’s thesis, **“Identifying Rental Stress Zones in Lisbon: A Spatial Rental Stress Index for Housing Affordability”**, completed as part of the Master’s Degree in Information Management, with a specialization in Business Intelligence, at NOVA Information Management School.

The project focuses on the development of a **Rental Stress Index (RSI)** for Lisbon, aiming to identify urban areas where rental housing affordability is under greater pressure. The index combines socioeconomic, housing, tourism, and spatial indicators to support a more comprehensive understanding of rental stress at the parish level.

---

## Project Overview

Lisbon has experienced significant housing affordability challenges over the last decade, driven by rising rental prices, tourism pressure, real estate investment, and increasing demand for centrally located housing.

Traditional affordability measures often rely mainly on rent-to-income ratios, which may fail to capture the spatial and multidimensional nature of rental stress. This project addresses that limitation by developing a spatially explicit composite index that integrates multiple dimensions of housing pressure.

The main output of this project is an interactive **Power BI dashboard** that allows users to explore rental stress patterns across Lisbon’s parishes and identify areas that may require policy attention.

---

## Research Objectives

The main objectives of this project are:

- To develop a **Rental Stress Index (RSI)** that measures rental stress across Lisbon’s parishes;
- To integrate housing, socioeconomic, tourism, and territorial indicators into a composite analytical framework;
- To identify spatial patterns of rental stress and intra-urban inequalities;
- To create an interactive **Power BI dashboard** to support monitoring, visualization, and evidence-based decision-making;
- To provide a replicable framework that can be adapted to other urban contexts.

---

## Research Questions

This project is guided by the following research questions:

1. How can a Rental Stress Index be developed using socioeconomic, housing, and territorial indicators to measure and compare rental stress across Lisbon’s parishes?

2. What spatial patterns of rental stress emerge in Lisbon when applying the RSI at the parish level, and what intra-urban inequalities do these patterns reveal?

3. To what extent can an interactive Power BI dashboard support the monitoring and interpretation of the RSI, contributing to evidence-based decision-making and the prioritization of housing policies?

---

## Methodology

The project follows a **Design Science Research Methodology (DSRM)** approach, which is suitable for developing practical artifacts that address real-world problems.

The methodological process includes:

1. Problem identification;
2. Definition of objectives;
3. Design and development of the Rental Stress Index;
4. Data preparation and transformation;
5. Dashboard development in Power BI;
6. Demonstration and evaluation of the results.

The RSI was developed as a composite indicator using standardized variables and factor analysis. The final scores were rescaled to a 0–100 range, where higher values indicate greater levels of rental stress.

---

## Data Sources

The project integrates multiple open data sources, including:

- **INE** – socioeconomic and housing census data;
- **Idealista** – rental price data;
- **Inside Airbnb** – short-term rental data;
- **Geodados Lisboa** – spatial data and points of interest;
- **Lisboa Aberta** – municipal open data;
- **OpenStreetMap** – geospatial contextual data.

The data was processed and aggregated at the parish level to ensure spatial consistency across all indicators.

---

## Main Indicators

The Rental Stress Index integrates indicators related to:

- Rental prices;
- Rental housing availability;
- Rental contract structure;
- Short-term rental pressure;
- Unemployment;
- Demographic structure;
- Ageing index;
- Tourism pressure;
- Urban attractiveness and points of interest.

Points of interest were also used to contextualize urban attractiveness, including mobility, education, commerce, culture, leisure, and safety-related facilities.

---

## Dashboard

The Power BI dashboard was designed as a decision-support tool for analyzing rental stress in Lisbon.

It includes several analytical pages, such as:

- Rental Stress Overview;
- Rental Market Structure;
- Tourism Pressure and Housing;
- Socioeconomic Vulnerability;
- Points of Interest;
- Indicators of Rental Stress.

The dashboard allows users to explore spatial patterns, compare parishes, identify high-stress areas, and understand the factors contributing to rental market pressure.

---

## Key Findings

The results reveal a clear **center–periphery pattern** in Lisbon.

Central parishes, such as **Santa Maria Maior**, **Misericórdia**, and **São Vicente**, show higher levels of rental stress. These areas combine high rental prices, strong tourism pressure, dense urban environments, and a significant presence of short-term rentals.

Peripheral parishes tend to show lower rental stress levels, although their housing dynamics differ from those of the historical and central areas.

Overall, the findings suggest that rental stress is a multidimensional phenomenon shaped by the interaction between housing market dynamics, socioeconomic vulnerability, tourism activity, and territorial characteristics.

---

## Repository Structure

```text
RSI-Dashboard/
│
├── data/                 # Input and processed datasets
├── scripts/              # Python scripts for data processing and analysis
├── dashboard/            # Power BI dashboard files
├── docs/                 # Thesis-related documentation
└── README.md             # Project documentation

# Dashboard Description

## Power BI Dashboard

The Power BI dashboard is the main visualization and decision-support component of this project. It was developed to support the analysis of the **Rental Stress Index (RSI)** across Lisbon’s parishes and to help identify areas where housing affordability is under greater pressure.

The dashboard integrates housing, socioeconomic, demographic, tourism, rental market, and spatial indicators. It allows users to explore territorial differences, compare parishes, analyze rental stress patterns, and understand the main factors contributing to housing pressure in Lisbon.

In addition to visualization, Power BI was also used as a key environment for **data transformation**, **data modeling**, and **indicator creation**.

---

## Dashboard Purpose

The main purpose of the dashboard is to provide an interactive tool for analyzing rental stress in Lisbon at the parish level.

The dashboard supports the following objectives:

- Visualize the spatial distribution of the Rental Stress Index;
- Identify parishes with higher and lower rental stress;
- Analyze rental market structure and housing availability;
- Explore the relationship between tourism pressure and housing stress;
- Examine socioeconomic vulnerability across parishes;
- Support evidence-based decision-making for housing and urban policy;
- Transform raw datasets into structured indicators for analysis.

---

## Unit of Analysis

The dashboard uses the **freguesia** as the main spatial unit of analysis.

This territorial scale allows the project to identify intra-urban differences within Lisbon and detect spatial patterns that would be hidden at broader geographic scales.

Each parish is used as a common key to integrate different datasets, including census data, rental price data, Airbnb data, points of interest, and RSI values.

---

## Data Transformation in Power BI

A significant part of the data preparation process was carried out directly in **Power BI**, using **Power Query**.

The transformation process was essential to clean, harmonize, and structure the datasets before creating the analytical model and dashboard visuals.

---

## Main Transformation Steps

The main data transformation steps included:

1. Importing multiple datasets into Power BI;
2. Cleaning and validating the data;
3. Standardizing parish names and identifiers;
4. Removing unnecessary columns;
5. Renaming variables for consistency;
6. Changing data types;
7. Handling missing or inconsistent values;
8. Merging datasets using parish identifiers;
9. Aggregating data at the parish level;
10. Creating derived indicators;
11. Preparing fact and dimension tables;
12. Building the final data model for dashboard analysis.

---

## Power Query Transformations

Power Query was used to prepare the datasets before visualization.

The transformations included operations such as:

- Filtering relevant records;
- Standardizing column names;
- Converting text, numeric, and date fields to the correct data types;
- Cleaning parish names to ensure consistency across datasets;
- Creating calculated columns;
- Joining tables from different sources;
- Aggregating spatial and statistical indicators by parish;
- Preparing tables for use in the data model.

These transformations ensured that the data from different sources could be integrated into a single analytical framework.

---

## Data Sources Integrated in the Dashboard

The dashboard combines data from several sources:

| Source | Description |
|---|---|
| INE | Census, housing, demographic, and socioeconomic indicators |
| Idealista | Rental price data by parish and month |
| Inside Airbnb | Short-term rental data |
| Geodados Lisboa | Points of interest and spatial information |
| Lisboa Aberta | Municipal open data |
| OpenStreetMap | Complementary geospatial data |
| RSI Output | Final Rental Stress Index values by parish |

---

## Data Model

The dashboard follows a dimensional modeling logic, where the data is organized around shared dimensions and analytical fact tables.

The main grain of the model is:

```text
Parish × Time

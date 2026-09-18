# RTL-Insight

### AI-Assisted RTL Design Analysis and PPA Prediction Framework

RTL-Insight is a machine learning-based framework designed to analyze Register Transfer Level (RTL) designs and estimate key design metrics: **Power, Performance, and Area (PPA)**.

The project aims to assist hardware designers in evaluating RTL designs at an early stage and provide insights for potential optimization before complete synthesis.

## Project Overview

Traditional RTL design evaluation often requires synthesis and simulation to estimate Power, Performance, and Area. RTL-Insight explores the use of machine learning to provide early PPA estimates from RTL design features.

The framework is developed as a Streamlit-based prototype that demonstrates RTL feature extraction, ML-based PPA prediction, and baseline comparison.

## Objectives

* Extract meaningful structural and code-level features from Verilog RTL designs.
* Develop a machine learning model for PPA prediction.
* Compare baseline PPA values with ML-predicted values.
* Explore RTL optimization guidance using machine learning.
* Provide an interactive interface for RTL design assessment.

## Methodology

The proposed RTL-Insight workflow consists of the following stages:

1. **RTL Design Input** – Upload a Verilog HDL design.
2. **Feature Extraction** – Extract structural and code-related features.
3. **ML-Based PPA Prediction** – Estimate Power, Performance, and Area using a machine learning model.
4. **PPA Contribution Analysis** – Analyze important design features and modules.
5. **Optimization Recommendation** – Explore potential RTL optimization techniques.
6. **Engineering Assessment Report** – Generate a detailed assessment of the design.

## Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Verilog HDL
* Machine Learning
* Random Forest Regression

## Project Structure

```text
RTL-Insight/
│
├── app.py
├── feature_extractor.py
├── generate_dataset.py
├── ml_model.py
├── optimization_engine.py
├── ppa_predictor.py
├── ppa_dataset.csv
├── requirements.txt
├── sample_alu.v
└── README.md
```

## Current Prototype

The current prototype demonstrates:

* Verilog RTL design input.
* RTL feature extraction.
* ML-based PPA prediction.
* Baseline versus ML prediction comparison.
* Interactive Streamlit dashboard.

The results are preliminary prototype outputs and require further validation using actual synthesis data and model evaluation metrics.

## Future Scope

* Improve the RTL feature extraction process.
* Train and validate the model using a larger RTL dataset.
* Integrate synthesis-based PPA measurements.
* Add explainable AI for PPA contribution analysis.
* Develop RTL optimization recommendations.
* Generate comprehensive engineering assessment reports.

## Author

**Amulya Dasari**

B.Tech – Electronics and Communication Engineering


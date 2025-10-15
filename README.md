# Nomogram for Predicting Bacteremia in Patients with Persistent Neutropenic Fever

This repository contains a **web-based nomogram calculator** for predicting the risk of bacteremia in patients with persistent neutropenic fever, based on machine learning models developed from clinical data. The tool provides an intuitive interface for clinicians and researchers to estimate patient-specific risk.

## Background

Persistent neutropenic fever is a common complication in patients with hematologic malignancies or undergoing chemotherapy. Early identification of bacteremia is critical for timely intervention. In this project, risk factors were analyzed and predictive models were developed using machine learning methods. The resulting model has been visualized as a **nomogram** to facilitate clinical application.

## Nomogram

The nomogram provides a graphical representation of the predictive model, allowing clinicians to calculate a patient's risk score based on their individual clinical factors.  

![Nomogram](nomogram.png)

You can also interact with the nomogram through the web app:  

[https://nomogram-bacteremia-with-pnf.streamlit.app/](https://nomogram-bacteremia-with-pnf.streamlit.app/)

## Features

- Interactive **nomogram calculator** for individualized risk prediction
- Calculates **total points** and corresponding **predicted probability of bacteremia**
- Built with **Streamlit** for easy deployment and user-friendly interface
- Open-source and reproducible for research purposes

## Installation

To run the app locally, clone this repository and install the required packages:

```bash
git clone https://github.com/hss2864/streamlit-nomogram.git
cd streamlit-nomogram
pip install -r requirements.txt
streamlit run app.py
```

## Usage
1. Open the web app.
2. Input patient data (e.g., clinical risk factors).
3. The nomogram will display the risk score and predicted probability.
4. Use the results to support clinical decision-making.

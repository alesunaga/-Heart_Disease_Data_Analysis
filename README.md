# Heart Disease Data Analysis

This repository contains Python code for analyzing a heart disease dataset. The analysis explores the relationship between various factors and the presence of heart disease.

## Data

The dataset used is 'heart_disease.csv'. It contains information about patients, including:

* `age`: Age of the patient
* `sex`: Sex of the patient
* `cp`: Chest pain type (typical angina, asymptomatic, non-anginal pain, atypical angina)
* `trestbps`: Resting blood pressure
* `chol`: Serum cholesterol
* `thalach`: Maximum heart rate achieved
* `heart_disease`: Presence or absence of heart disease

## Analysis

The code performs the following analysis:

1. **Data Inspection:**  Prints the first 5 rows of the dataset.
2. **Thalach and Heart Disease:**
   - Creates a boxplot of `thalach` by `heart_disease` presence.
   - Performs an independent samples t-test to compare `thalach` between groups.
3. **Age and Heart Disease:**
   - Creates a boxplot of `age` by `heart_disease` presence.
   - Performs a t-test to compare `age` between groups.
4. **Cholesterol and Heart Disease:**
   - Creates a boxplot of `chol` by `heart_disease` presence.
   - Performs a t-test to compare `chol` between groups.
5. **Chest Pain Type and Thalach:**
   - Creates a boxplot of `thalach` by `cp`.
   - Performs Levene's test for equal variances.
   - Performs ANOVA to compare `thalach` across chest pain types.
   - If ANOVA is significant, performs Tukey's HSD post-hoc test.
6. **Chest Pain Type and Heart Disease:**
   - Creates a contingency table of `cp` and `heart_disease`.
   - Visualizes the contingency table with a heatmap.
   - Performs a chi-square test of independence.

## Requirements

The code requires the following Python libraries:

* pandas
* matplotlib.pyplot
* seaborn
* scipy.stats
* numpy
* statsmodels.stats.multicomp

## Usage

1. Make sure you have the required libraries installed.
2. Place the 'heart_disease.csv' file in the same directory as the Python script.
3. Run the Python script.

## Results

The results of the analysis are printed to the console, including:

* T-test results for `thalach`, `age`, and `chol`.
* ANOVA and Tukey's HSD results for `thalach` by chest pain type.
* Chi-square test results for the association between `cp` and `heart_disease`.
* Contingency table and heatmap.

## Notes

* The code assumes that the data is appropriately cleaned and formatted.
* The analysis includes basic statistical tests. Further analysis and interpretation may be needed depending on the research question.
* The code can be adapted and extended for further exploration of the data.

## Author

Alexsandro Alves alexsandroroot@gmail.com

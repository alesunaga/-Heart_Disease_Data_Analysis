# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, kruskal, levene, chi2_contingency
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Load the heart disease dataset
heart = pd.read_csv('heart_disease.csv')

# Inspect the first few rows of the data
print(heart.head())

# --- Thalach (Maximum Heart Rate) and Heart Disease ---
# Visualize the distribution of thalach for each heart disease group
var = 'thalach'
plt.figure(figsize=(8, 6))
sns.boxplot(x='heart_disease', y=var, data=heart)
plt.title('Thalach Distribution by Heart Disease Presence')
plt.xlabel('Heart Disease')
plt.ylabel('Thalach')
plt.show()
plt.clf()  # Clear the figure

# Separate thalach data by heart disease presence
thalach_no_hd = heart[heart['heart_disease'] == 'absence']['thalach']
thalach_hd = heart[heart['heart_disease'] == 'presence']['thalach']

# Perform an independent samples t-test to compare thalach means
alpha = 0.05  # Significance level
t_statistic, p_value = ttest_ind(thalach_no_hd, thalach_hd)
print(f"T-test: statistic={t_statistic:.3f}, p-value={p_value:.3f}")

if p_value < alpha:
    print("The difference in thalach between heart disease groups is statistically significant.")
else:
    print("The difference in thalach between heart disease groups is not statistically significant.")


# --- Age and Heart Disease ---
# Visualize the distribution of age for each heart disease group
plt.figure(figsize=(8, 6))
sns.boxplot(x='heart_disease', y='age', data=heart)
plt.title('Age Distribution by Heart Disease Presence')
plt.xlabel('Heart Disease')
plt.ylabel('Age')
plt.show()
plt.clf()

# Separate age data by heart disease presence
age_no_hd = heart[heart['heart_disease'] == 'absence']['age']
age_hd = heart[heart['heart_disease'] == 'presence']['age']

# Perform a t-test to compare age means
t_statistic, p_value = ttest_ind(age_no_hd, age_hd)
print(f"T-test: statistic={t_statistic:.3f}, p-value={p_value:.3f}")
if p_value < alpha:
    print("The difference in age between heart disease groups is statistically significant.")
else:
    print("The difference in age between heart disease groups is not statistically significant.")


# --- Cholesterol (Chol) and Heart Disease ---
# Visualize the distribution of cholesterol for each heart disease group
plt.figure(figsize=(8, 6))
sns.boxplot(x='heart_disease', y='chol', data=heart)
plt.title('Cholesterol Distribution by Heart Disease Presence')
plt.xlabel('Heart Disease')
plt.ylabel('Cholesterol')
plt.show()
plt.clf()

# Separate cholesterol data by heart disease presence
chol_no_hd = heart[heart['heart_disease'] == 'absence']['chol']
chol_hd = heart[heart['heart_disease'] == 'presence']['chol']

# Perform a t-test to compare cholesterol means
t_statistic, p_value = ttest_ind(chol_no_hd, chol_hd)
print(f"T-test: statistic={t_statistic:.3f}, p-value={p_value:.3f}")
if p_value < alpha:
    print("The difference in cholesterol between heart disease groups is statistically significant.")
else:
    print("The difference in cholesterol between heart disease groups is not statistically significant.")


# --- Chest Pain Type and Thalach ---
# Visualize the distribution of thalach for each chest pain type
plt.figure(figsize=(8, 6))
sns.boxplot(x='cp', y='thalach', data=heart)
plt.title('Thalach Distribution by Chest Pain Type')
plt.xlabel('Chest Pain Type')
plt.ylabel('Thalach')
plt.show()
plt.clf()

# Separate thalach data by chest pain type
thalach_typical = heart.thalach[heart['cp'] == 'typical angina']
thalach_asymptomatic = heart.thalach[heart['cp'] == 'asymptomatic']
thalach_nonanginal = heart.thalach[heart['cp'] == 'non-anginal pain']
thalach_atypical = heart.thalach[heart['cp'] == 'atypical angina']

# Levene's test for equal variances (check assumption for ANOVA)
statistic, p_value = levene(thalach_typical, thalach_asymptomatic, thalach_nonanginal, thalach_atypical)
print(f"Levene's test: statistic={statistic:.3f}, p-value={p_value:.3f}")

# Perform ANOVA to compare thalach means across chest pain types
statistic, p_value = f_oneway(thalach_typical, thalach_asymptomatic, thalach_nonanginal, thalach_atypical)
print(f"ANOVA test: statistic={statistic:.3f}, p-value={p_value:.3f}")

if p_value < alpha:
    print("The difference in thalach across chest pain categories is statistically significant.")

    # Post-hoc test (Tukey's HSD) to identify which groups are different
    data = heart[['thalach', 'cp']]
    m_comp = pairwise_tukeyhsd(data['thalach'], data['cp'], alpha=0.05)
    print(m_comp)
else:
    print("The difference in thalach across chest pain categories is not statistically significant.")


# --- Chest Pain Type and Heart Disease ---
# Create a contingency table to examine the relationship between chest pain and heart disease
Xtab = pd.crosstab(heart['cp'], heart['heart_disease'])

# Display the contingency table
print("\nContingency Table: Chest Pain vs. Heart Disease\n", Xtab) #Added a title to the table

# Visualize the contingency table with a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(Xtab, annot=True, cmap="YlGnBu", fmt="d")
plt.title("Contingency Table: Chest Pain vs. Heart Disease")
plt.xlabel("Heart Disease")
plt.ylabel("Chest Pain Type")
plt.show()

# Perform a chi-square test of independence to test for association
chi2, pval, dof, exp = chi2_contingency(Xtab)
print(f"\nChi-square test: statistic={chi2:.3f}, p-value={pval:.3f}")  # Added statistic to output

if pval < alpha:
    print("There is a statistically significant association between chest pain type and heart disease.")
else:
    print("There is no statistically significant association between chest pain type and heart disease.")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

df_BMI_male = pd.read_excel('data/Indicator_BMI male ASM.xlsx')
# df_BMI_female = pd.read_excel('data/Indicator_BMI female ASM.xlsx')
# df_SBP_male = pd.read_excel('data/Indicator_SBP female ASM.xlsx')
# df_SBP_female = pd.read_excel('data/Indicator_SBP female ASM.xlsx')

df_BMI_male.head()

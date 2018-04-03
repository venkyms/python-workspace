import pandas as pd
import matplotlib.pyplot as plt
import math


def calculate_discriptive_statistics_data(label):
    """
       Function to calculate Descriptive statistics data
    :param label: Column name in CSV file
    :return: None
    """

    df = stroop_effect_df[label]

    # find mean of DataFrame value
    df_mean = round(df.mean(), 2)
    print('{} mean: {}'.format(label, df_mean))

    # find variance of DataFrame value
    df_variance = round(df.var(), 2)
    print('{} variance: {}'.format(label, df_variance))

    # find standard deviation for DataFrame value
    df_sd = round(df.std(), 2)
    print('{} standard deviation: {}'.format(label, df_sd))

    # find standard error for DataFrame value
    df_sem = round(df.sem(), 2)
    print('{} Standard Error: {}'.format(label, df_sem))


def perform_statistical_analysis():
    """
    Function to perform all t-statistical analysis
    :return: None
    """

    # Generate Difference data for Congruent and InCongruent values
    df = stroop_effect_df
    df['Difference'] = df['Congruent'] - df['Incongruent']
    print(df)

    # Find the Mean of the difference value
    mean_difference = round(df['Difference'].mean(), 2)
    print('Mean Difference: {}'.format(mean_difference))

    # Find the Standard Deviation of the difference value
    difference_sd = round(df['Difference'].std(), 2)
    print('Difference Standard Deviation: {}'.format(difference_sd))

    # Find the Standard Error of the difference value
    difference_sem = round(df['Difference'].sem(), 2)
    print('Difference Standard Error: {}'.format(difference_sem))

    # Find the t-statistics of the difference value
    n = len(df['Difference'])
    t_statistic = round(mean_difference / (difference_sd / math.sqrt(n)), 2)
    print('t-Statistics: {}'.format(t_statistic))

    # Got the t-critical value from t-table manually
    degrees_of_freedom = n - 1
    t_critical = 1.714
    print('t-critical value at 95% confidence level and DF at {} is: +or-{}'.format(degrees_of_freedom, t_critical))


def display_stroop_effect_plot():
    """
    Function to generate a bar plot to display the Congruent and Incongruent data in plot
    :return: None
    """
    ax = stroop_effect_df.plot.box()
    ax.set_title('Stroop Effect plot')
    ax.set_xlabel('Test Subject')
    ax.set_ylabel('Response Time')
    plt.show()


stroop_effect_df = pd.read_csv('../../data/stroopdata.csv')
print(stroop_effect_df)
calculate_discriptive_statistics_data('Congruent')
calculate_discriptive_statistics_data('Incongruent')
display_stroop_effect_plot()
perform_statistical_analysis()

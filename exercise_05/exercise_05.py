import pandas as pd 
pd.options.mode.chained_assignment = None  # default='warn'
divorced_df = pd.read_csv('divorced.csv', sep=';')

#What is the change in pct of divorced danes from 2008 to 2020?

divorced2008 = divorced_df.iloc[0,2]
divorced2020 = divorced_df.iloc[1,2]

divorceChangeInPercent = (divorced2020-divorced2008) / divorced2008 * 100

print(divorceChangeInPercent)

#Which of the 5 biggest cities has the highest percentage of 'Never Married' in 2020?

never_married_df = pd.read_csv('nevermarried.csv', sep=';')

totalTop5 = never_married_df[(never_married_df['OMRÅDE'] != 'Hele landet') & (never_married_df['OMRÅDE'] != 'Region Hovedstaden') &(never_married_df['OMRÅDE'] != 'Region Midtjylland') &  (never_married_df['OMRÅDE'] != 'Region Syddanmark') & (never_married_df['OMRÅDE'] != 'Region Sjælland') & (never_married_df['OMRÅDE'] != 'Region Nordjylland')]



totalTop5.sort_values('INDHOLD', ascending=False, inplace=True )
print(totalTop5[:5])


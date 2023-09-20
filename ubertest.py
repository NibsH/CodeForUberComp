import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

population_df = pd.read_csv(r'C:\Users\nabal\Downloads\population.csv')
age_ranges = ['0-4', '5-9', '10-14', '15-19','65-69', '70-74', '75-79', '80-84', '85-89', '90-94','>=95']
population_df = population_df[~population_df['Age'].isin(age_ranges)]
population_df = population_df[population_df['Year'] == 2017]
population_df = population_df.drop('Neighborhood.Name', axis=1)
population_df = population_df.drop('Neighborhood.Code', axis=1)
population_df = population_df.sort_values(by=['District.Name', 'Gender', 'Age'])
population_df = population_df.rename(columns={'District.Name': 'District'})
population_df = population_df .groupby(['District', 'Gender','Age'])['Number'].sum().reset_index()
population_df.reset_index(drop=True, inplace=True)   
population_df = population_df.drop_duplicates(subset=['District', 'Gender', 'Age'], keep='first')
population_df.to_csv(r'C:\Users\nabal\Downloads\filtered3_population.csv', index=False)
filterpopulation_df = pd.read_csv(r'C:\Users\nabal\Downloads\filtered3_population.csv')
print(filterpopulation_df)




pivot_population = filterpopulation_df.pivot(index=['District', 'Gender'], columns='Age', values='Number')


fig, ax = plt.subplots(figsize=(40, 30))


bar_width = 0.35


positions = range(len(pivot_population))



rects1 = ax.bar(positions, pivot_population['20-24'], bar_width, label='20-24')
rects2 = ax.bar([p + bar_width for p in positions], pivot_population['25-29'], bar_width, label='25-29')
rects3 = ax.bar([p + bar_width for p in positions], pivot_population['30-34'], bar_width, label='30-34')
rects4 = ax.bar([p + bar_width for p in positions], pivot_population['35-39'], bar_width, label='35-39')
rects4 = ax.bar([p + bar_width for p in positions], pivot_population['40-44'], bar_width, label='40-44')
rects4 = ax.bar([p + bar_width for p in positions], pivot_population['45-49'], bar_width, label='45-49')
rects4 = ax.bar([p + bar_width for p in positions], pivot_population['50-54'], bar_width, label='50-54')
rects4 = ax.bar([p + bar_width for p in positions], pivot_population['55-59'], bar_width, label='55-59')
rects4 = ax.bar([p + bar_width for p in positions], pivot_population['60-64'], bar_width, label='60-64')



ax.set_xticks([p + bar_width/2 for p in positions])
ax.set_xticklabels([f'{index[0]}, {index[1]}' for index in pivot_population.index], fontsize=5, rotation=45)



plt.xlabel('District, Gender')
plt.ylabel('Population')
plt.title('Population by Age Group, Gender, and District')


plt.legend(title='Age Group')

plt.show()










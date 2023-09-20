import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

unemployment_df = pd.read_csv(r'unemployment.csv')
unemployment_df = unemployment_df[unemployment_df['Year'] == 2017]
unemployment_df  = unemployment_df .drop('Neighborhood Name', axis=1)
unemployment_df  = unemployment_df .drop('Demand_occupation', axis=1)

unemployment_df = unemployment_df.sort_values(by=['District Name','Gender'])
unemployment_df = unemployment_df .groupby(['Month','District Name','Gender'])['Number'].sum().reset_index()
unemployment_df.to_csv(r'C:\Users\nabal\Downloads\unemployment2.csv', index=False)
unemployment_df  = unemployment_df .drop('Month', axis=1)
unemployment_df = unemployment_df.sort_values(by=['District Name','Gender'])
unemployment_df = unemployment_df .groupby(['District Name','Gender'])['Number'].mean().reset_index()
unemployment_df['Number'] = unemployment_df['Number'] .round().astype(int)
#unemployment_df = unemployment_df .groupby(['District Name','Gender'])['Number'].mean().reset_index()
unemployment_df.to_csv(r'C:\Users\nabal\Downloads\unemployment3.csv', index=False)


unemployment_df = pd.read_csv(r'C:\Users\nabal\Downloads\unemployment3.csv')


plt.figure(figsize=(10, 6))


plt.bar(unemployment_df['District Name'] + ' ' + unemployment_df['Gender'], unemployment_df['Number'])


plt.xlabel('District Name and Gender')
plt.ylabel('Average Unemployment')
plt.title('Average Unemployment by District and Gender')


plt.xticks(fontsize=5, rotation=85)


plt.show()

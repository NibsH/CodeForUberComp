import pandas as pd
import matplotlib.pyplot as plt

unemployment_df = pd.read_csv(r'C:\Users\nabal\Downloads\unemployment3.csv')


plt.figure(figsize=(10, 6))

plt.bar(unemployment_df['District Name'] + ' ' + unemployment_df['Gender'], unemployment_df['Number'])

plt.xlabel('District Name and Gender')
plt.ylabel('Average Unemployment')
plt.title('Average Unemployment by District and Gender')


plt.xticks(fontsize=5, rotation=85)

plt.show()

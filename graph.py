import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("transports.csv")
transport = df["Transport"].value_counts()
x = pd.Series(['Underground','Railway (FGC)','Tram','Maritime station','RENFE','Airport train','Cableway','Funicular'])
plt.barh(x,transport)
plt.ylabel("Type of Transportation Station")
plt.xlabel("Number of Stations")
plt.show()
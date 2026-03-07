import pandas as pd
import requests
import numpy as np
import re

df1 = pd.read_csv("risk_final.csv", sep=",", dtype="str", encoding="ISO-8859-1")
risk = df1[['Title', 'Status', 'Owner']]

risk.to_csv('risk_test.csv', index=False)

print(risk)






#risk_final.to_csv('risk_final.csv', index=False)
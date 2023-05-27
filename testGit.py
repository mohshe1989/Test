import os
import pandas as pd

df = pd.read_csv(r"D:\Studium\Master\CER\sotu_paragraphs.csv",on_bad_lines='skip',sep=';')
print(df.info())
print(df.head())

import pandas

from pandas import read_csv as rcsv


df = rcsv("C:\\Users\\mravi\\Personal\\work\\python_training\\resources\\employee.csv")

print(df)
print(df['id'])
print(df['salary'].max())

print("Min Sal", df['salary'].min())
print(df['id'].max())

excel_data = pandas.read_excel("C:\\Users\\mravi\\Downloads\\Big Data & Analytics_Technical Evaluation Sheet  of Chikkala Vijay.xlsx")
print(excel_data)
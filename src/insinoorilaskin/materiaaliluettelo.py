# Imports
import pandas as pd

# Full path and relative path
# path = r"/Users/konsta/Documents/koodaus_projektit/insinoorilaskin/pohjat/materiaaliluettelo.xlsx"
path = r"./pohjat/materiaaliluettelo.xlsx"

# Read and and create dataframe
with pd.ExcelFile(path, engine="openpyxl") as xls:
	df = pd.read_excel(xls,"Taul1")

	# Create new VALUE column where QUANTITY and DIMENSIONS are combined.
	# DIMENSIONS for pipe only and QUANTIY for others.
	is_pipe = df["CODE"].astype(str).str.contains("pipe", case=False, na=False)
	df["VALUE"] = df["QUANTITY"]
	df.loc[is_pipe, "VALUE"] = df.loc[is_pipe, "DIMENSIONS"]
	sum_list = df.groupby("CODE", as_index=False).agg({
	"DESCRIPTION": "first",
	"VALUE": "sum"})

	print(sum_list[['DESCRIPTION', 'CODE', 'VALUE']])

	print(sum_list)

import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='extract specific column in csv/tsv, and print the unique terms')
parser.add_argument('-file', '-f', type=str, required=True, help="file path to extract")
parser.add_argument('-column', '-c', type=str, required=True, help="column name in your file")
parser.add_argument('-delimiter', '-d', type=str, required=False, default=',', help="delimiter, use \'/t\' for tsv, default is \',\' for csv")

args = parser.parse_args()

data = pd.read_csv(args.file, sep=args.delimiter)[args.column].dropna().unique()
for i in data:
	print(i)

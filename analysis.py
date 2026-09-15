import csv
from collection import Counter

FILEPATH = "New_York_City_Leading_Causes_of_Death_20260914.csv"

def load_csv(filepath):
    data = []

    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    return data

def clean_deaths(value):
  value = value.strip()
  if value == "" or value == ".":
    return 0
  return int(value)

def clean_sex(value):
  if value =

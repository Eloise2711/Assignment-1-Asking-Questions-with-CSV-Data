import csv

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
    if value == "M":
        return "Male"
    if value == "F":
        return "Female"
    return value

def clean_race_ethnicity(value):
    if value == "White Non-Hispanic":
        return "Non-Hispanic White"
    if value == "Black Non-Hispanic":
        return "Non-Hispanic Black"
    return value

death_data = load_csv(FILEPATH)

# 1. Print the first 2 rows
print(death_data[:2])

# 2. Print the first row
print(death_data[0])

# 3. Print rows 10–19
print(death_data[10:20])

# 4. Print column names
print(death_data[0].keys())

# 5. Print the first 10 values of one column
for row in death_data[:10]:
    print(row["Leading Cause"])
    
# 6. Print the first 10 rows of three columns
for oew in death_data[:10]:
    print(
        row["Year"],
        row["Leading Cause"],
        row["Deaths"]
    )
    
# Question 1: Which leading cause has the highest total number of deaths?

cause_totals = {}

for row in death_data:
    cause = row["Leading Cause"]
    deaths = clean_deaths(row["Deaths"])

    if cause not in cause_totals:
        cause_totals[cause] = 0

    cause_totals[cause] += deaths

top_cause = ""
top_cause_deaths = 0

for cause in cause_totals:
    if cause_totals[cause] > top_cause_deaths:
        top_cause = cause
        top_cause_deaths = cause_totals[cause]

print(top_cause + ":", top_cause_deaths)

# Question 2: How many total recorded deaths were caused by Heart Disease in 2021?

heart_disease_deaths = 0

for row in death_data:
    if row["Year"] == "2021" and row["Leading Cause"] == "Diseases of Heart (I00-I09, I11, I13, I20-I51)":
        heart_disease_deaths += clean_deaths(row["Deaths"])

print("Heart Disease deaths in 2021:", heart_disease_deaths)

# Question 3: How many total deaths were recorded for Male vs Female demographics overall?

female_deaths = 0
male_deaths = 0

for row in death_data:
    sex = clean_sex(row["Sex"])
    deaths = clean_deaths(row["Deaths"])
    
    if sex == "Female":
        female_deaths += deaths
    elif sex == "Male":
        male_deaths += deaths

print("Female:", female_deaths)
print("Male:", male_deaths)
    













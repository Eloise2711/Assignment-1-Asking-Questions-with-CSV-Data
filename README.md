# New York City Leading Causes of Death - Three Data Questions

## Why I Chose This Dataset
I chose the New York City Leading Causes of Death because it is a real, local (NYC), and offers an impactful look at the public health across different demographics. Each row shows a combination of year, leading cause, sex, race, deaths, death rate and age-adjusted death rate. 
It's a great example of a public dataset that supports insightful population-level comparisons, while still having limits like there's no individual-level records and having many missing datas.

## Three Data Questions

# Question 1: Which leading cause has the highest total number of deaths?

```python
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
```

Output:

```text
Diseases of Heart (I00-I09, I11, I13, I20-I51): 272717
```

Why the data structure supports this question:
This works because the dataset is tabular and each row includes a Leading Cause value and a Deaths value. By grouping rows by the Leading Cause column and adding the Death values, the code can compare total death across causes.

# 

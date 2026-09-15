# New York City Leading Causes of Death - Three Data Questions

## Why I Chose This Dataset
I chose the New York City Leading Causes of Death because it is a real, local (NYC), and offers an impactful look at the public health across different demographics. Each row shows a combination of year, leading cause, sex, race, deaths, death rate and age-adjusted death rate. 
It's a great example of a public dataset that supports insightful population-level comparisons, while still having limits like there's no individual-level records and having many missing datas.

## Three Data Questions

### Question 1: Which leading cause has the highest total number of deaths?

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

### Question 2: How many total recorded deaths were caused by Heart Disease in 2021?

```python
heart_disease_deaths = 0

for row in death_data:
    if row["Year"] == "2021" and row["Leading Cause"] == "Diseases of Heart (I00-I09, I11, I13, I20-I51)":
        heart_disease_deaths += clean_deaths(row["Deaths"])

print("Heart Disease deaths in 2021:", heart_disease_deaths)
```

Output:

```text
Heart Disease deaths in 2021: 16568
```

Why the data structure supports this question:
This works because the dataset has separate columns for Year, Leading Cause and deaths. The code can filter the rows to only 2021 and only heart disease, the ad the deaths value from those matching rows.

### Question 3: How many total deaths were recorded for Male vs Female demographics overall?

```python
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
```

Output:

```text
Female: 422602
Male: 420457
```

Why the data structure supports this question:
This works because Sex is a categorical column and deaths is a count column. Each row belongs to a sex category, so the code can group rows by sex and add the death counts. I also normalize old labels like F and M into Female and Male so the totals are not split across different label styles.

## What the Data Cannot Answer

A question I might want to answer is: "Why did a specific person die from a certain cause?" This dataset cannot answer that because it does not include individual informations like medical histories, hospital records, income... It only shows year, cause, sex, and race. It would be wrong to assume that a higher death total for a group automatically proves one direct cause, because population size, age distribution, and other missing variables could also affect the totals.

# New York City Leading Causes of Death - Three Data Questions

## Why I Chose This Dataset
I chose the New York City Leading Causes of Death because it is a real, local (NYC), and offers an impactful look at the public health across different demographics. Each row shows a combination of year, leading cause, sex, race, deaths, death rate and age-adjusted death rate. 
It's a great example of a public dataset that supports insightful population-level comparisons, while still having limits like there's no individual-level records and having many missing datas.

## Three Data Questions

# Question: Which leading cause has the highest total number of deaths?
#cause_total = Counter()
#for row in death_data:
#    if row["Primary Fur Color"] == "Gray":
#       count += 1
#print(count)
#output: 2473

Why the data structure supports this question:
This works because the dataset is tabular: each row is one squirrel sighting, 
and the Primary Fur Color column stores a categorical label for fur color. 
Counting the rows where that column equals "Gray" gives the total number of gray squirrel
sightings.

import pandas as pd
import matplotlib.pyplot as plt


# Read the CSV file.
df = pd.read_csv('salaries.csv')

# Columns information.
metro = df['Metro']
cost_of_living_difference = df['Mean Software Developer Salary (adjusted)']
average_salary = df['Mean Software Developer Salary (unadjusted)']
number_of_jobs = df['Number of Software Developer Jobs']
median_home_price = df['Median Home Price']
rent_average = df['Rent avg']

# Question 1: What city has the highest software developer salaries and their salaries?
sorted_salary = df.sort_values(
    by=["Mean Software Developer Salary (unadjusted)"],
    ascending=False
    )

highest = sorted_salary.head(10)[["Metro", "Mean Software Developer Salary (unadjusted)"]]
print("What city has the highest software developer salaries and their salaries")
print(highest)


#Question 2: What are the top 10 cities with the lowest amount of jobs?
sorted_jobs = df.sort_values(
    by=["Number of Software Developer Jobs"],
    ascending=True
    )
most_jobs = sorted_jobs.head(10)[["Metro", "Number of Software Developer Jobs"]]
print("What are the top 10 cities with the highest amount of jobs?")
print(most_jobs)

#Histogram graph
# plt.figure(figsize=(12, 6))
# plt.hist(
#     , 
#     bins=50,
#     )

# plt.title("")
# plt.xlabel("")
# plt.ylabel("")
# plt.show()


 #Plot Graph
plt.title("Average Salary vs Median Home Price vs Number of Jobs")
plt.plot(average_salary, label = "Salary")
plt.plot(number_of_jobs, label = "# of Jobs")
plt.plot(median_home_price, label = "Home Price")
plt.legend()
plt.show()
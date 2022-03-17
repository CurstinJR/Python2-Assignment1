# Assignment 1
# Name: Curstin
# Surname: Rose
# Student Number: 220275408

# %%
import pandas as pd

df = pd.read_csv('data/googleplaystore.csv')

# %%
# Question 1 - Display the first 7 records
first_7 = df.head(7)
first_7

# %%
# Question 2 - What is the total number of records
# in column and column datatype?
print("Total number of records in column:", df.shape[0])
print("Column datatype:", df.dtypes, sep="\n")

# %%
# Question 3 - Convert the Review column to a float data type
df['Reviews'] = df['Reviews'].replace('3.0M', '3000000')
df['Reviews'] = df['Reviews'].astype(dtype='float64')
df['Reviews'].dtype

# %%
#  Question 4 - Display the unique values of the Category column
df['Category'].unique()

# %%
# Question 5 - What is the average of rating column?
df['Rating'].mean(skipna=True)

# %%
# Question 6 - What is average rating for apps in the
# photography category?
photography_apps = df.loc[df['Category'] == 'PHOTOGRAPHY']
photography_apps['Rating'].mean()

# %%
# Question 7 - What is the total number of free and paid apps?
nr_free_apps = df.loc[df['Type'] == 'Free'].shape[0]
nr_paid_apps = df.loc[df['Type'] == 'Paid'].shape[0]

print("Total number of free apps:", nr_free_apps)
print("Total number of paid apps:", nr_paid_apps)

# %%
# Question 8 - What is the average value of Reviews?
df['Reviews'].mean(skipna=True)

# %%
# Question 9 - Which app has the highest review?
df.loc[df['Reviews'] == df['Reviews'].max()]

# %%
# Question 10 - What are the top 5 apps with the highest review?
top_5 = df.drop_duplicates(subset=['App']).nlargest(5, 'Reviews')['App']
top_5.reset_index(drop=True)
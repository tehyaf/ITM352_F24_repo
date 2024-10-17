import pandas as pd

ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]

names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

age_gender_tuples = list(zip(ages, gender))

df = pd.DataFrame(age_gender_tuples, index=names, columns=['Age', 'Gender'])

print("DataFrame:")
print(df)

print("\nSummary using describe():")
print(df.describe())

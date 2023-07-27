import pandas as pd
from sklearn.model_selection import train_test_split
import csv

pd.set_option("max_colwidth", None)

# Load the CSV file into a DataFrame
df = pd.read_csv("output.csv", header=None, sep = 'delimiter' )
df = df[df.iloc[:,0] != "."]
# df.reset_index(drop=True, inplace=True)

# Filter out sentences with more than 30 words
df_num_words = df[0].str.split().apply(len)
df = df[df_num_words >= 4]
df = df[df_num_words <= 30]

# Define the ratio for the training dataset (e.g., 0.8 for an 80-20 split)
train_ratio = 0.8

# Split the DataFrame into training and test datasets
train_df, test_df = train_test_split(df, train_size=train_ratio, random_state=42)

# Save the training and test datasets to separate CSV files
train_csv = "train_data.csv"
test_csv = "test_data.csv"

train_df.to_csv(train_csv, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\", sep="\t", header=False, index=False)
test_df.to_csv(test_csv,  quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\", sep="\t", header=False, index=False)

print("Data successfully split and saved to training_data.csv and test_data.csv.")

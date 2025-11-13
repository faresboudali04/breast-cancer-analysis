# Import all required libraries
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

# Get the directory of the script
script_dir = os.path.dirname(__file__)
# Construct the path to the CSV file
csv_path = os.path.join(os.path.dirname(script_dir), 'breast-cancer.csv')

# Load the dataset
df_1 = pd.read_csv(csv_path)

# Display the first few rows
print(df_1.head())

df_1.info()

df_1.describe()

df_1.shape
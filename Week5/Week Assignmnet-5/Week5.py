import pandas as pd

# Load the dataset
file_path = "C:/Users/DELL/Downloads/archive/nba.csv"  # Update this path to where you saved the file
data = pd.read_csv(file_path)
# Display the first few rows of the dataset
print(data.head())

# Display summary statistics
print(data.describe())

# Display information about the dataset
print(data.info())
data = data.drop_duplicates()
# Check for missing values
print(data.isnull().sum())

# Impute missing values (e.g., with mean or median)
data.fillna(data.mean(), inplace=True)

# Alternatively, you can drop rows with missing values
data = data.dropna()
# Convert data types if necessary
data['column_name'] = data['column_name'].astype('desired_type')
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data[['feature1', 'feature2']] = scaler.fit_transform(data[['feature1', 'feature2']])
# One-hot encoding
data = pd.get_dummies(data, columns=['categorical_column'])
# Example: Create a new feature
data['new_feature'] = data['feature1'] / data['feature2']
# Example: Drop irrelevant features
data = data.drop(['irrelevant_feature1', 'irrelevant_feature2'], axis=1)
print(data.head())
print(data.info())
data.to_csv('preprocessed_nba_data.csv', index=False)
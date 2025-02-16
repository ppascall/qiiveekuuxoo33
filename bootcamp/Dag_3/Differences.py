import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
data = pd.read_csv('diabetes.csv')

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Identify the 5 attributes with the lowest pairwise correlations
correlation_pairs = correlation_matrix.unstack().sort_values().drop_duplicates()
lowest_correlations = correlation_pairs[correlation_pairs != 1].head(5)
print("Attributes with the lowest pairwise correlations:\n", lowest_correlations)

# Use RandomForestClassifier to identify the top 5 important features
X = data[data.columns[:-1]]
Y = data['Outcome']
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X, Y)
feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
top_5_features = feature_importances.head(5)
print("Top 5 features according to RandomForestClassifier:\n", top_5_features)

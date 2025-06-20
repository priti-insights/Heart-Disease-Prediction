import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# ✅ Load your data — use the FULL path
df = pd.read_csv('C:/Users/PRITI/heart-disease.csv')

# ✅ Separate features and target
X = df.drop('target', axis=1)
y = df['target']

# ✅ Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Fit the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Save the model as heart_model.pkl
with open('heart_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ heart_model.pkl trained and saved successfully!")

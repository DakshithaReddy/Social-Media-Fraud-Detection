import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 1. Load dataset
df = pd.read_csv("data/social_media_data.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# 2. Select input features
features = [
    "followers",
    "friends",
    "friend_requests",
    "posts",
    "account_age_days",
    "profile_complete",
    "verified"
]

X = df[features]

# Target column
y = df["fraud"]


# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# 4. Create Machine Learning model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 5. Train the model
model.fit(X_train, y_train)

print("Model training completed!")


# 6. Make predictions
y_pred = model.predict(X_test)


# 7. Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)


# 8. Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 9. Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# 10. Save the trained model
joblib.dump(model, "models/fake_account_model.pkl")

print("\nModel saved successfully!")
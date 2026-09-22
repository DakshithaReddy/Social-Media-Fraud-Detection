import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/fake_account_model.pkl")

print("\n===================================")
print("   SOCIAL MEDIA FAKE ACCOUNT DETECTOR")
print("===================================\n")

# Get account details
followers = int(input("Enter number of followers: "))
friends = int(input("Enter number of friends: "))
posts = int(input("Enter number of posts: "))
account_age_days = int(input("Enter account age in days: "))
friend_requests = int(input("Enter number of friend requests: "))

profile_complete = int(
    input("Is the profile complete? (1 = Yes, 0 = No): ")
)

verified = int(
    input("Is the account verified? (1 = Yes, 0 = No): ")
)

# Create input data
data = pd.DataFrame([{
    "followers": followers,
    "friends": friends,
    "posts": posts,
    "account_age_days": account_age_days,
    "friend_requests": friend_requests,
    "profile_complete": profile_complete,
    "verified": verified
}])

# Automatically arrange features in the exact order
# used during model training
data = data[model.feature_names_in_]

# Make prediction
prediction = model.predict(data)[0]

print("\n-----------------------------------")

if prediction == 1:
    print("RESULT: FAKE ACCOUNT")
else:
    print("RESULT: REAL ACCOUNT")

print("-----------------------------------")
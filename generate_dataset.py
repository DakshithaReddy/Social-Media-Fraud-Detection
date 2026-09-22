import pandas as pd
import random

data = []

for i in range(1000):

    followers = random.randint(0, 2000)
    friends = random.randint(0, 1500)
    friend_requests = random.randint(0, 1000)

    posts = random.randint(0, 500)
    account_age = random.randint(1, 2000)

    profile_complete = random.choice([0, 1])
    verified = random.choice([0, 1])

    # Simple rules to create sample fraud labels
    suspicious_score = 0

    if followers < 20:
        suspicious_score += 1

    if friend_requests > 500:
        suspicious_score += 1

    if friends > 1000:
        suspicious_score += 1

    if posts > 400:
        suspicious_score += 1

    if account_age < 30:
        suspicious_score += 1

    if profile_complete == 0:
        suspicious_score += 1

    if verified == 0:
        suspicious_score += 1

    if suspicious_score >= 3:
        fraud = 1
    else:
        fraud = 0

    data.append([
        i + 1,
        followers,
        friends,
        friend_requests,
        posts,
        account_age,
        profile_complete,
        verified,
        fraud
    ])


columns = [
    "user_id",
    "followers",
    "friends",
    "friend_requests",
    "posts",
    "account_age_days",
    "profile_complete",
    "verified",
    "fraud"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/social_media_data.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))
print(df.head())
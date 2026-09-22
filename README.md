# 🛡️ SocialShield – AI-Powered Social Media Fraud Detection

SocialShield is a machine learning-based web application that analyzes social media account characteristics and identifies accounts that may exhibit suspicious behavior.

The system uses a **Random Forest classification model** to analyze account-level features and provides a probability-based assessment of whether an account is likely to be authentic or suspicious.

## 🚀 Features

- 🔍 Social media account analysis
- 🤖 Random Forest machine learning model
- 📊 Probability-based fraud detection
- 📈 Model performance analytics
- 📋 Confusion matrix
- 🎯 Risk-level assessment
- 🌐 Interactive Streamlit dashboard
- 💾 Trained machine learning model
- 📁 Sample dataset included

## 🧠 Machine Learning

The Random Forest model uses the following account characteristics:

- Followers
- Friends
- Posts
- Account age
- Friend requests
- Profile completeness
- Verification status

### Model Performance

| Metric | Result |
|---|---:|
| Accuracy | 96.5% |
| Precision | 97% |
| Recall | 95% |
| F1 Score | 96% |

### Confusion Matrix

| | Predicted Real | Predicted Fake |
|---|---:|---:|
| Actual Real | 129 | 0 |
| Actual Fake | 7 | 64 |

These results are based on the project's generated test dataset.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Machine Learning
- Random Forest

## 📂 Project Structure

```text
Social-Media-Fraud-Detection/
│
├── app.py
├── app_backup.py
├── generate_dataset.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── social_media_data.csv
│
├── models/
│   └── fake_account_model.pkl
│
└── src/
    ├── fake_account_detection.py
    └── predict_account.py
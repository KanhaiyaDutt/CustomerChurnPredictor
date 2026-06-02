# 📊 Customer Churn Predictor

A Machine Learning web application that predicts whether a customer is likely to churn based on customer subscription information.

## 🚀 Live Demo

**Streamlit App:**
https://customerchurnpredictor-aiedyzec8cvfifu5zf5szr.streamlit.app/

## 📂 GitHub Repository

https://github.com/KanhaiyaDutt/CustomerChurnPredictor

---

## 📌 Project Overview

Customer churn is one of the most important business metrics for subscription-based companies. Retaining existing customers is often more cost-effective than acquiring new ones.

This project uses multiple machine learning models to predict whether a customer will churn.

The application allows users to:

* Select different machine learning models
* Enter customer information
* Predict customer churn in real time
* Compare model predictions

---

## 🛠️ Technologies Used

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* XGBoost

### Model Selection & Optimization

* GridSearchCV
* RandomizedSearchCV
* Pipeline
* ColumnTransformer
* Feature Selection using Ridge Regression

### Deployment

* Streamlit

---

## 📊 Dataset Features

| Feature         | Description                       |
| --------------- | --------------------------------- |
| CustomerID      | Unique customer identifier        |
| Age             | Customer age                      |
| Gender          | Male/Female                       |
| Tenure          | Number of months with company     |
| MonthlyCharges  | Monthly subscription charges      |
| ContractType    | Contract type                     |
| InternetService | Internet service type             |
| TotalCharges    | Total amount charged              |
| TechSupport     | Availability of technical support |
| Churn           | Target variable                   |

---

## 🔍 Data Preprocessing

The following preprocessing steps were performed:

* Missing value handling using `SimpleImputer`
* One-Hot Encoding for categorical variables
* Numerical feature scaling using:

  * StandardScaler
  * MinMaxScaler
* Feature Selection using:

  * Ridge Regression
  * SelectFromModel

---

## 🤖 Models Trained

### Logistic Regression

* GridSearchCV Hyperparameter Tuning

### Random Forest Classifier

* RandomizedSearchCV Hyperparameter Tuning

### Ridge Classifier

* GridSearchCV Hyperparameter Tuning

### XGBoost Classifier

* RandomizedSearchCV Hyperparameter Tuning

### Best Classifier

A combined RandomizedSearchCV search was performed across all models to automatically select the best-performing pipeline.

---

## 🎯 Selected Features

After feature selection, the most important features were:

* Tenure
* TotalCharges
* ContractType
* TechSupport

These features contributed most strongly to churn prediction.

---

## 📁 Project Structure

```text
CustomerChurnPredictor/
│
├── app.py
├── requirements.txt
│
├── best_classifier.pkl
├── logistic_model.pkl
├── randomforest_classifier.pkl
├── ridge_Classifier.pkl
├── xgb_classifier.pkl
│
├── Customer_churn_Dataset.csv
│
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/KanhaiyaDutt/CustomerChurnPredictor.git
cd CustomerChurnPredictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## 📈 Machine Learning Pipeline

```text
Input Data
     ↓
Preprocessing
     ↓
Feature Selection (Ridge)
     ↓
Model Training
     ↓
Hyperparameter Tuning
     ↓
Best Model Selection
     ↓
Prediction
```

---

## 🌐 Deployment

The application is deployed using Streamlit Community Cloud.

Live App:

https://customerchurnpredictor-aiedyzec8cvfifu5zf5szr.streamlit.app/

---

## 👨‍💻 Author

Kanhaiya Dutt

GitHub:
https://github.com/KanhaiyaDutt

---

## ⭐ Future Improvements

* Customer retention recommendations
* Advanced model explainability using SHAP
* Interactive analytics dashboard
* Batch prediction through CSV upload

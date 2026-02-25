# 🍷 Wine Quality Prediction App

## 📌 Project Overview

This project uses **Machine Learning** to predict the quality of wine based on its physicochemical properties.
The model analyzes chemical features such as acidity, alcohol content, sulphates, and density to classify wine as:

* ❌ Bad Quality
* ⚖️ Average Quality
* ✅ Good Quality

The project also includes a **Streamlit web app** for interactive predictions.

---

## 🎯 Objectives

* Predict wine quality using ML models
* Handle missing values, outliers, and class imbalance
* Compare multiple algorithms
* Deploy a user-friendly Streamlit app

---

## 📂 Dataset

The dataset contains physicochemical properties of wine and quality ratings.

### Features used:

* Fixed acidity
* Volatile acidity
* Citric acid
* Residual sugar
* Chlorides
* Free sulfur dioxide
* Total sulfur dioxide
* Density
* pH
* Sulphates
* Alcohol

🎯 Target: `quality`

---

## ⚙️ Project Workflow

### 1️⃣ Data Preprocessing

* Handled missing values using mean imputation
* Removed outliers using IQR method
* Balanced classes using RandomOverSampler
* Standardized features using StandardScaler

### 2️⃣ Models Used

* Naive Bayes
* Logistic Regression (Softmax for multiclass)
* Support Vector Machine (RBF Kernel)
* Decision Tree (with GridSearchCV tuning)
* K-Nearest Neighbors
* ✅ Random Forest (Best performer)

---

## 🏆 Best Model Performance

**Random Forest Classifier**

* Accuracy: ~90%
* Handles non-linear relationships effectively
* Robust against overfitting

---

## 🖥️ Streamlit Web App

The app allows users to input wine properties and get instant predictions.

### Features:

✔️ Interactive UI
✔️ Real-time prediction
✔️ Scaled inputs using saved scaler
✔️ Categorized output (Bad/Average/Good)

---

## 🚀 How to Run the Project

### 🔹 1. Clone Repository

```bash
git clone https://github.com/nikithasreek/wine_project_ml
cd wine_project_ml
```

### 🔹 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 4. Run Streamlit App

```bash
streamlit run wineappmodel.py
```

---

## 📦 Requirements

Example dependencies:

```
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
imbalanced-learn
Pillow
```

---

## 📊 Example Prediction

Input:

```
Alcohol: 10.5
Volatile acidity: 0.30
Sulphates: 0.65
```

Output:

```
✅ GOOD QUALITY WINE
```

---

## 📁 Project Structure

```
wine-quality-prediction/
│
├── app.py                # Streamlit app
├── rfmodel.sav           # Trained Random Forest model
├── stdscaler.sav         # Saved StandardScaler
├── wine_quality_project.ipynb
├── requirements.txt
└── README.md
```

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and should not be used for commercial or industrial wine quality assessment.

---

## 👩‍💻 Author

**Nikitha Sree**
Aspiring Data Scientist | AI Enthusiast

---

## ⭐ If you found this helpful

Give this repo a ⭐ and share!

---



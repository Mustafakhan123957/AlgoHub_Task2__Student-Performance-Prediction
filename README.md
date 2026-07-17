# 🎓 Student Performance Prediction System

A Machine Learning web application that predicts whether a student is likely to **Pass** or **Fail** based on academic performance using a trained Random Forest Classifier.

## 📌 Project Overview

This project was developed as part of the **AlgoHub Machine Learning Internship Program**. It uses historical student academic data to classify student performance and provides predictions through a simple Streamlit web interface.

## 🚀 Features

- Predicts student performance (Pass/Fail)
- User-friendly Streamlit interface
- Machine Learning model trained using Random Forest Classifier
- Data preprocessing and visualization
- Model saved using Joblib
- Ready for deployment on Streamlit Cloud

## 📂 Project Structure

```
StudentPerformancePrediction/
│
├── app.py
├── train.ipynb
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── student_performance.csv
│
└── models/
    └── student_performance_model.pkl
```

## 📊 Dataset Features

- student_id
- study_hours
- attendance
- assignments
- previous_marks
- participation
- result (Target)

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

## 🤖 Machine Learning Model

- Logistic Regression
- Random Forest Classifier (Final Model)

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/MustafaKhan123957/StudentPerformancePrediction.git
```

Move into the project directory

```bash
cd StudentPerformancePrediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

## 📷 Application

The application allows users to enter:

- Study Hours
- Attendance
- Assignments Completed
- Previous Marks
- Participation Score

It predicts whether the student is likely to **Pass** or **Fail**.

## 📈 Future Improvements

- Probability score for predictions
- Interactive dashboard
- Better UI design
- Additional ML models
- Cloud deployment

## 👨‍💻 Author

**Mustafa Khan**

GitHub: https://github.com/Mustafakhan123957

LinkedIn: *www.linkedin.com/in/mustafa-khan-55835034b*

---

Developed as part of the **AlgoHub Machine Learning Internship Program**.
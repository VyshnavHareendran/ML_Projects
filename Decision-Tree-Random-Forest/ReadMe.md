# Decision Trees & Random Forests for Classification and Regression

This project demonstrates how to apply tree-based machine learning models for both classification and regression tasks using the same dataset.
We explore both **Decision Trees and Random Forests**, covering model training, overfitting control, ensemble learning, feature interpretation, and evaluation.

Dataset

The dataset used is from Kaggle:  
[Heart Disease Data Set](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

Tools & Terchniques

- Python
- Scikit-learn
- Graphviz (for Decision Tree visualization)
- Matplotlib & Seaborn (Visualizations)
- Google Colab

Program Structure :

The project is structured into two distinct sections for clarity:

1) Classification Task: Heart Disease Prediction
Dataset: Heart Disease Dataset

Goal: Predict whether a patient has heart disease (Binary Classification)

Models Applied:
- Decision Tree Classifier
- Random Forest Classifier (Ensemble Learning)
  
Key Steps:
- Data Loading & Exploration
- Decision Tree Model
- Controlling Overfitting by limiting tree depth
- Random Forest Model
- Feature Importance Analysis
- Cross-Validation

Performance Evaluation using Accuracy and Classification Report

2️) Regression Task: Cholesterol Prediction
Dataset: Same Heart Disease Dataset

Goal: Predict cholesterol levels based on patient attributes (Regression Task)
Note: Though this dataset is primarily for classification, a regression task is constructed for internship purpose .

Models Applied:
- Decision Tree Regressor
- Random Forest Regressor (Ensemble Learning)

Key Steps:
- Data Preparation
- Decision Tree Regression Model
- Controlling Overfitting by limiting tree depth
- Random Forest Regression Model
- Feature Importance Analysis
- Model Evaluation using Mean Squared Error (MSE) and R² Score

  This project demonstrates ensemble learning through the use of Random Forests, which combine predictions from multiple decision trees to improve model accuracy,
  robustness, and generalization for both classification and regression tasks.

Conclusion :

- Tree-based models are highly interpretable and effective for both classification and regression tasks.
- Limiting tree depth helps control overfitting and improve generalization.
- Random Forests, as an ensemble method, enhance performance and provide feature importance insights.
- The same dataset can be leveraged for different machine learning problem types, showcasing the flexibility of tree-based models.














  

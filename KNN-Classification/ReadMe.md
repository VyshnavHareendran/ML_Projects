# K-Nearest Neighbors (KNN) Classification

This project implements the** K-Nearest Neighbors (KNN) Classification** algorithm using the popular Iris flower dataset. The goal is to classify iris flowers into
species based on their physical features using a simple yet effective machine learning approach.

The project includes data preprocessing, exploratory data analysis, model training with KNN, hyperparameter tuning, model evaluation, and decision boundary visualization.

Dataset

The dataset used is from Kaggle:  
[Iris Species Data Set](https://www.kaggle.com/datasets/uciml/iris)
  
Tools & Terchniques

- Python  
- Pandas & NumPy  
- Matplotlib & Seaborn (Visualizations)  
- Scikit-learn (Model Building & Evaluation)  
- Google Colab  

Project Steps

1) Data Loading: Load dataset from CSV.  
2) Exploratory Data Analysis: Understand data distribution and relationships. 
3) Data Preprocessing: Feature scaling using StandardScaler. 
4) Model Building: Train KNN model using KNeighborsClassifier.
5) Hyperparameter Tuning: Test different K values to find optimal performance. 
6) Model Evaluation:
   - Accuracy
   - Confusion Matrix
   - Classification Report
7) Visualization:
   - Pairplot of features
   - Heatmap of feature correlation
   - Decision boundary plot (using first 2 features)




Result

- Best K Value: 5
- Accuracy: ~97%
- Confusion Matrix: Displays correct and incorrect predictions per class
- Classification Report: Shows precision, recall, F1-score for each class

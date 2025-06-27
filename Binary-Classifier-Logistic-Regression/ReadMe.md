# Logistic Regression - Binary Classifier

This project implements a binary classification model using **Logistic Regression** to predict the likelihood of breast cancer being malignant or benign, 
based on the **Breast Cancer Wisconsin (Diagnostic) Data Set**.

Dataset

The dataset used is from Kaggle:  
[Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)

**Features:**  
- 30 real-valued features derived from digitized images of breast mass cell nuclei.  
- Examples include: `radius`, `texture`, `perimeter`, `area`, `smoothness`, etc.  

**Target:**  
- `M` = Malignant  
- `B` = Benign
  
Tools & Terchniques

- Python  
- Pandas & NumPy  
- Matplotlib & Seaborn (Visualizations)  
- Scikit-learn (Model Building & Evaluation)  
- Google Colab  


Project Steps
1) Data Cleaning & Preprocessing  
2) Feature Standardization  
3) Logistic Regression Model Training  
4) Evaluation using:  
   - Confusion Matrix  
   - Classification Report (Precision, Recall, F1-Score)  
   - ROC Curve & AUC Score  
5) Sigmoid Function Explanation  
6) Threshold Tuning Demonstration

Result

The model achieves reliable classification performance with ROC-AUC evaluation and demonstrates how Logistic Regression converts input features into probabilities
for binary decision making.



# SUPPORT VECTOR MACHINE FOR LINEAR AND NON LINEAR CLASSIFICATION

**Support Vector Machines (SVM) for linear and non-linear classification** on the Breast Cancer dataset. Perform data
preprocessing, model training, hyperparameter tuning, visualization, and performance evaluation.

Dataset

The dataset used is from Kaggle:  
[Breast Cancer Dataset Data Set](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)

**Features:**  
- 30 numerical features related to tumor characteristics (e.g., radius, texture, smoothness) 
- diagnosis column indicating:
    - M - Malignant (cancerous)
    - B - Benign (non-cancerous)
  
Tools & Terchniques

- Python  
- Pandas & NumPy  
- Matplotlib & Seaborn (Visualizations)  
- Scikit-learn (Preprocessing,SVM modeling (linear & RBF),Hyperparameter tuning with GridSearchCV,Model evaluation)  
- Google Colab  


Project Steps
1) Data Loading & Exploration  
2) Data Visualization
3) Data Preprocessing
4) Model Training 
   - Trained Linear SVM model
   - Trained Non-linear SVM with RBF Kernel 
5) Model Evaluation 
6) Hyperparameter Tuning
7) Cross-Validation

Result

- The RBF Kernel SVM achieved better classification performance compared to linear SVM.
- Hyperparameter tuning significantly improved accuracy.
- The final model showed high precision and recall, making it suitable for medical diagnosis support.



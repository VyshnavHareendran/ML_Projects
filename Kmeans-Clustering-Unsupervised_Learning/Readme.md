# K-Means Clustering

This project applies **unsupervised machine learning techniques**, specifically **K-Means 
Clustering**, to segment customers based on demographic and behavioral data. The goal is
to group similar customers together to help businesses implement targeted marketing
strategies and improve customer understanding.

Dataset

The dataset used is from Kaggle:  
[Mall Customer Segmentation Data Set](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
  
Tools & Terchniques

- Python  
- Pandas & NumPy  
- Matplotlib & Seaborn (Visualizations)  
- Scikit-learn (Preprocessing,SVM modeling (linear & RBF),Hyperparameter tuning with GridSearchCV,Model evaluation)  
- Principal Component Analysis(PCA)
- Google Colab
  


Project Steps
1) Data Loading & Preprocessing 
2) Exploratory Data Analysis(EDA)
   - Trained Linear SVM model
   - Plotted correlation heatmap to understand feature relationships
3) Finding Optimal Numbers Of Clusters
   - Used Elbow Method to determine optimal K
   - Visualized WCSS (Within Cluster Sum of Squares) curve
4) Applying K-Means Clustering 
   - Applied K-Means with optimal K
   - Assigned cluster labels to each customer
5) Visualizing Clusters 
   - Reduced dimensionality using PCA for 2D visualization
   - Visualized customer clusters using scatter plots
6) Cluster Evaluation
   - Calculated Silhouette Score to evaluate clustering quality
7) Cluster Analysis

Result

- Successfully segmented customers into distinct groups based on behavior and demographics
- Visualizations clearly highlighted separable clusters
- Silhouette Score indicated satisfactory clustering performance



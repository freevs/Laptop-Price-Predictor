# Laptop Price Predictor Model

## Goal
Built a laptop price predictor that provides an estimated price based on the user's input configuration.

## Steps
1. **Data Loading and Preliminary Analysis**
   
   Successfully loaded and explored the dataset, performing an initial analysis to understand the shape, structure, and key characteristics of the features.

2. **Data Cleaning and Exploratory Data Analysis**

   Data Cleaning: Conducted a thorough examination of the dataset to identify and address duplicate values and missing data, ensuring data integrity.
   
   Exploratory Data Analysis (EDA): Performed univariate and bivariate analysis to uncover patterns, trends, and correlations within the features. Detected and handled outliers, ensuring more accurate predictions.
   
   Evaluated the relationships between features using correlation analysis, Checked for multicollinearity in the data
   
4. **Feature Engineering and Transformation**

   Applied advanced feature engineering techniques, including one-hot encoding for categorical variables and normalization for continuous features.
   
   Created new features by transforming existing ones using Categorical Mapping, Splitting and Extracting Features , binning etc

5. **Model Development and Implementation**

    Implemented a variety of regression models, including Linear Regression, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and tree-based models, to predict laptop prices.
    Explored different approaches to capture the complexity of the dataset and improve prediction accuracy.
   
6. **Model Evaluation and Refinement**

   Evaluated the performance of models using key metrics such as R-squared (R²) and Mean Absolute Error (MAE) to ensure robustness and reliability.
   
## 	How to run the project
1. Clone this repository
2. Create a new environment conda create  `-n newenv python==3.6`
3. Open any IDE
4. Then install the requirements.txt file `pip install -r requirements.txt`
5. After all the requirements are installed successfully Then run the app by `python app.py`.py

## Web Application
Enter all the laptop parameters and click the "Predict" button to display the price for that configuration.

<img src="https://github.com/freevs/Laptop-Price-Predictor/blob/master/Laptop%20Prediction.png" width="800" height="600">

## Tools
<p>
<img src="https://github.com/freevs/Laptop-Price-Predictor/blob/master/Icons/Python.png" width="100" height="100">
<img src="https://github.com/freevs/Laptop-Price-Predictor/blob/master/Icons/Streamlit.png" width="100" height="100">
<img src="https://github.com/freevs/Laptop-Price-Predictor/blob/master/Icons/Matplotlib.png" width="100" height="100">
<img src="https://github.com/freevs/Laptop-Price-Predictor/blob/master/Icons/NumPy.png" width="100" height="100">
<img src="https://github.com/freevs/Laptop-Price-Predictor/blob/master/Icons/Pandas.png" width="100" height="100">
</p>




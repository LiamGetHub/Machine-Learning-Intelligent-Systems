# Bank Loan Prediction

This repository contains a machine learning project aimed at predicting whether a customer will accept a personal loan from the bank. The dataset used for this project contains information about customers, including their demographic details, financial history, and other variables.

## Problem Statement

The bank managers want to explore ways to convert their liability customers to personal loan customers. The goal of this project is to create a model that can predict if a customer will accept a personal loan based on their characteristics.

## Dataset

The dataset includes the following columns:

- **ID**: Customer ID
- **Age**: Age of the customer
- **Experience**: Professional experience (years)
- **Income**: Annual income (in thousands of dollars)
- **Family**: Total number of family members
- **CCAvg**: Average spending on credit cards (in thousands of dollars)
- **Education**: Education level:
  - 1: Undergraduate
  - 2: Graduate
  - 3: Postgraduate
- **Mortgage**: House mortgage value (in thousands of dollars)
- **Securities Account**: Whether the customer has a securities account (1: Yes, 0: No)
- **CD Account**: Whether the customer has a CD account (1: Yes, 0: No)
- **Online**: Whether the customer has online banking (1: Yes, 0: No)
- **CreditCard**: Whether the customer has a credit card issued by the bank (1: Yes, 0: No)
- **Personal Loan**: The target variable (1: Yes, 0: No)

## Libraries and Tools Used

- `pandas`: Data manipulation and analysis
- `numpy`: Numerical operations
- `matplotlib`: Data visualization
- `seaborn`: Statistical data visualization
- `sklearn`: Machine learning models and evaluation
  - Naïve Bayes (`GaussianNB`)
  - Perceptron
  - Logistic Regression
  - K-Nearest Neighbors (KNN)

## Approach

1. **Data Preprocessing**:
   - Load and clean the dataset.
   - Handle negative values (e.g., for experience).
   - Visualize various relationships using strip plots, box plots, and distributions.
   - Calculate correlations among features.
   
2. **Model Selection**:
   - We used four different machine learning models:
     - **Naïve Bayes**: A probabilistic classifier based on Bayes' theorem.
     - **Perceptron**: A linear classifier based on supervised learning.
     - **Logistic Regression**: A linear model for binary classification.
     - **K-Nearest Neighbors (KNN)**: A non-parametric, distance-based classifier.
   
3. **Model Evaluation**:
   - Split the data into training and test sets (80%/20%).
   - Trained the models and evaluated their performance using metrics such as:
     - Accuracy
     - AUC-ROC (Area Under the ROC Curve)
     - Classification Report (Precision, Recall, F1 Score)
   
4. **Visualization**:
   - Plotted comparison graphs to visualize the performance of each model with respect to **Accuracy** and **AUC-ROC**.

## Results

The models were evaluated on the test set, and their performance was as follows:

| Model              | Accuracy | AUC-ROC |
|--------------------|----------|---------|
| Naïve Bayes        | 87.90%   | 0.9225  |
| Perceptron         | 85.40%   | **N/A** |
| Logistic Regression| 95.00%   | 0.9594  |
| K-Nearest Neighbors| 90.10%   | 0.8122  |

**Logistic Regression** achieved the highest accuracy and AUC-ROC, making it the best-performing model for this problem.

## Visualizations

The project also includes visualizations that show the comparison of model performance across Accuracy and AUC-ROC. A bar plot was used for accuracy, while a line plot displayed AUC-ROC values.


## Installation & Running the Project Locally

Follow these steps to run the project on your local machine:

1. **Clone the Repository**  
   This command will clone the repository to your local machine.
   ```bash
   git clone https://github.com/LiamGetHub/Bank-Loan-Classification.git
   ```
   After running this command, navigate to the project directory:
   ```bash
   cd bank-loan-prediction
   ```

2. **Create a Virtual Environment (Optional but Recommended)**  
   It's a good practice to create a virtual environment to keep dependencies isolated for this project. Run the following command to create a virtual environment:
   ```bash
   python -m venv venv
   ```
   Then, activate the virtual environment:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Project Dependencies**  
   To install all the required Python libraries and dependencies, use the following command:
   ```bash
   pip install -r requirements.txt
   ```
   This will install all the necessary packages listed in the `requirements.txt` file, including `pandas`, `scikit-learn`, `matplotlib`, and others.

4. **Run the Project**  
   After installing the dependencies, you can run the project by executing the following:
   ```bash
   python main.py
   ```
   This will execute the code in `main.py` and show the output based on the models' predictions and evaluation results.

5. **(Optional) Deactivate Virtual Environment**  
   Once you are done running the project, you can deactivate the virtual environment with the following command:
   ```bash
   deactivate
   ```

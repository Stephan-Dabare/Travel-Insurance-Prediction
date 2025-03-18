# Customer Insurance Prediction Web Application

A Flask-based web application designed to predict customer insurance outcomes based on demographic and behavioral features. The application uses a machine learning model (not shown) to generate predictions from user input.

## 📋 Features

### Customer Data Attributes

-   **Age**: Numerical age of the customer.
-   **AnnualIncome**: Yearly income in local currency.
-   **FamilyMembers**: Number of family members.
-   **ChronicMissense**: Presence of chronic diseases (binary: 0 or 1).
-   **Employment Type** (one-hot encoded):
    -   `Government Sector`: `1` if employed in government sector, else `0`.
    -   `Private Sector/Self Employed`: `1` if private/self-employed, else `0`.
-   **Graduate Status** (one-hot encoded):
    -   `GradwatchMot_No`: `1` if not a graduate, else `0`.
    -   `GradwatchMot_Ves`: `1` if a graduate, else `0`.
-   **Frequent Traveler Status** (one-hot encoded):
    -   `FrequentType_No`: `1` if not a frequent traveler, else `0`.
    -   `FrequentType_Yes`: `1` if a frequent traveler, else `0`.
-   **Travel Abroad History** (one-hot encoded):
    -   `EverTravelIndividual_No`: `1` if no travel history, else `0`.
    -   `EverTravelIndividual_Yes`: `1` if has traveled abroad, else `0`.

## 🛠️ Installation

1.  **Clone the Repository**

    ```bash
    git clone [repository-url]
    cd [project-directory]
    ```

2.  **Install Dependencies**

    ```bash
    pip install flask pandas scikit-learn
    ```

3.  Ensure you have a trained `model.pkl` file in the project directory.

4.  **Run the Application**

    ```bash
    python app.py
    ```

## 🚀 Usage

1.  Access the web interface at `http://localhost:5000`.
2.  Fill out the form with customer details.
3.  Submit the form to view the prediction result.

### Example Input Form

Age: 35
AnnualIncome: 750000
FamilyMembers: 3
ChronicMissense: 0
Employment Type: Government Sector
Graduate Status: Yes
Frequent Traveler: No
Travel Abroad History: Yes


### Output

The prediction result (e.g., `Approved` or `Rejected`) will be displayed on the same page.

## 🧩 Code Structure

### Key Components

#### Customer Data Dictionary

```python
customer = {
    'Age': [age],
    'AnnualIncome': [annual_income],
    # ... other features
}


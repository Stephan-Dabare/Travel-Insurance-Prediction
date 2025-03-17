from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('Travel_Insurance_Model.joblib')

# Define a function to interpret the prediction result
def interpret_prediction(prediction):
    if prediction == 0:
        return "The customer is not likely to purchase travel insurance."
    elif prediction == 1:
        return "The customer is likely to purchase travel insurance."
    else:
        return "Invalid prediction value."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        annual_income = int(request.form['annual_income'])
        family_members = int(request.form['family_members'])
        chronic_diseases = int(request.form['chronic_diseases'])
        employment_type = request.form['employment_type']
        graduate_or_not = request.form['graduate_or_not']
        frequent_flyer = request.form['frequent_flyer']
        ever_travelled_abroad = request.form['ever_travelled_abroad']

        # Create a dictionary of customer data
        customer = {
            'Age': [age],
            'AnnualIncome': [annual_income],
            'FamilyMembers': [family_members],
            'ChronicDiseases': [chronic_diseases],
            'Employment Type_Government Sector': [1 if employment_type == 'Government Sector' else 0],
            'Employment Type_Private Sector/Self Employed': [1 if employment_type == 'Private Sector/Self Employed' else 0],
            'GraduateOrNot_No': [1 if graduate_or_not == 'No' else 0],
            'GraduateOrNot_Yes': [1 if graduate_or_not == 'Yes' else 0],
            'FrequentFlyer_No': [1 if frequent_flyer == 'No' else 0],
            'FrequentFlyer_Yes': [1 if frequent_flyer == 'Yes' else 0],
            'EverTravelledAbroad_No': [1 if ever_travelled_abroad == 'No' else 0],
            'EverTravelledAbroad_Yes': [1 if ever_travelled_abroad == 'Yes' else 0]
        }

        # Create a DataFrame from the customer data
        customer_df = pd.DataFrame(customer)

        # Use the model to make a prediction
        prediction = model.predict(customer_df)[0]
        result = interpret_prediction(prediction)

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
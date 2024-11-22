from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
import os

# Initialize Flask app
app = Flask(__name__)

# CSV file path
CSV_FILE = "user_details.csv"

# Ensure the uploads directory exists
if not os.path.exists(CSV_FILE):
    # Create the file and add headers
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Education Level", "Birthdate"])

# Route for the form page
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_details():
    try:
        # Get form data
        name = request.form['name']
        age = request.form['age']
        education = request.form['education']
        birthdate = request.form['birthdate']

        # Validate form fields
        if not name or not age or not education or not birthdate:
            return jsonify({'error': 'All fields are required!'}), 400

        try:
            age = int(age)
        except ValueError:
            return jsonify({'error': 'Age must be a number!'}), 400

        # Save data to CSV
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, education, birthdate])

        return jsonify({'message': 'Details saved successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask app
#if __name__ == "__main__":
    #app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
import logging
import database as db

# Initialize the Flask app
app = Flask(__name__)

# Logging configuration
logging.basicConfig(level=logging.DEBUG)

# Load coffee data from the database
def load_coffee_data():
    coffees = db.get_all_coffees()
    coffee_data = pd.DataFrame(coffees)
    return coffee_data

coffee_data = load_coffee_data()

# Encode categorical features
def encode_feature(df, feature):
    encoder = LabelEncoder()
    encoder.fit(df[feature].apply(str).str.strip())
    return encoder, encoder.transform(df[feature].apply(str).str.strip())

# Encode the dataset
encoders = {}
for feature in ['Flavor', 'Roast_Level', 'Acidity', 'Drink_Type', 'Drink_Time', 'Strength']:
    encoder, encoded_feature = encode_feature(coffee_data, feature)
    coffee_data[feature + '_Encoded'] = encoded_feature
    encoders[feature] = encoder

# Encode user input
def encode_user_input(user_input, feature, encoders):
    if user_input is None or user_input.strip() == '':
        logging.warning(f"No input provided for {feature}. Setting to default.")
        return encoders[feature].transform([encoders[feature].classes_[0]])[0]  # Default to the first class

    encoder = encoders[feature]
    user_input_cleaned = user_input.strip()
    if user_input_cleaned in encoder.classes_:
        return encoder.transform([user_input_cleaned])[0]
    else:
        logging.warning(f"Invalid input for {feature}. Setting to default.")
        return encoder.transform([encoder.classes_[0]])[0]

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    user_data = {
        'Flavor': request.form.get('flavor'),
        'Roast_Level': request.form.get('roast_level'),
        'Acidity': request.form.get('acidity'),
        'Drink_Type': request.form.get('drink_type'),
        'Drink_Time': request.form.get('drink_time'),
        'Strength': request.form.get('strength')
    }

    user_inputs = {}
    for feature in user_data:
        input_value = user_data[feature]
        encoded_value = encode_user_input(input_value, feature, encoders)
        user_inputs[feature] = encoded_value

    user_vector = np.array(list(user_inputs.values()))
    user_df = pd.DataFrame([user_vector], columns=[f + '_Encoded' for f in user_inputs.keys()])

    # Compute similarity with encoded data
    user_similarity = cosine_similarity(user_df, coffee_data[[f + '_Encoded' for f in user_inputs.keys()]])
    coffee_data['Similarity'] = user_similarity.flatten()

    # Dimensionality reduction using SVD for better similarity matching
    svd = TruncatedSVD(n_components=2)
    coffee_data_svd = svd.fit_transform(coffee_data[[f + '_Encoded' for f in user_inputs.keys()]])
    user_vector_svd = svd.transform(user_df)
    user_similarity_svd = cosine_similarity(user_vector_svd, coffee_data_svd)
    coffee_data['Similarity_SVD'] = user_similarity_svd.flatten()

    # Select the most similar recommendation with a slight randomness for ties
    top_recommendations = coffee_data.sort_values(by='Similarity_SVD', ascending=False).head(3)
    recommendation = top_recommendations.sample(1).to_dict(orient='records')[0]

    return render_template('recommendation.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)

import pandas as pd

# Your dictionary data
data = {
    'Flavor': ['Fruity', 'Nutty', 'Chocolatey', 'Fruity', 'Nutty', 'Chocolatey', 'Fruity', 'Nutty', 'Chocolatey'],
    'Roast Level': ['Light', 'Medium', 'Dark', 'Light', 'Medium', 'Dark', 'Light', 'Medium', 'Dark'],
    'Acidity': ['Medium', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High'],
    'Drink Type': ['Drip', 'Espresso', 'Aeropress Pourover', 'Drip', 'Espresso', 'Aeropress Pourover', 'Drip', 'Espresso', 'Aeropress Pourover'],
    'Country': ['Ethiopia', 'Colombia', 'Brazil', 'Kenya', 'Costa Rica', 'Honduras', 'Yemen', 'Peru', 'Guatemala'],
    'Health Benefit': ['Antioxidant-rich', 'Energy Boost', 'Mood Enhancer', 'Stress Relief', 'Immunity Boost', 'Digestive Aid', 'Anti-inflammatory', 'Focus Improvement', 'Detoxifying'],
    'Description': ['Fruity and vibrant', 'Nutty and smooth', 'Rich and chocolatey', 'Fruity with citrus notes', 'Nutty with chocolate hints', 'Deep chocolate flavors', 'Floral and fruity', 'Herbal notes', 'Bold and rich'],
    'Video URL': [
        'https://example.com/video1', 'https://example.com/video2', 'https://example.com/video3',
        'https://example.com/video4', 'https://example.com/video5', 'https://example.com/video6',
        'https://example.com/video7', 'https://example.com/video8', 'https://example.com/video9'
    ],
    'Drink Time': ['Morning', 'Afternoon', 'Evening', 'Morning', 'Afternoon', 'Evening', 'Morning', 'Afternoon', 'Evening'],
    'Strength': ['Mild', 'Medium', 'Strong', 'Medium', 'Mild', 'Strong', 'Mild', 'Medium', 'Strong']
}


# # # Convert dictionary to DataFrame
csv2_df = pd.DataFrame(data)

# # Read the first CSV file
#csv1_df = pd.read_csv(r"C:\Users\adams\Downloads\coffee_clean.csv")

# # Merge the DataFrames
#merged_df = pd.concat([csv1_df, csv2_df])

# Save the merged DataFrame to a new CSV file
csv2_df.to_csv('coffee_data.csv', index=False)



# # Let's load the CSV file uploaded by the user and inspect the data to better understand how to integrate it into the recommendation system.

# import pandas as pd

# # Load the coffee data from the uploaded file
# #file_path = 
# coffee_data = pd.read_csv('D:\coffee_recomendation\coffee_data_1.csv')

# # Show the first few rows of the dataset to understand its structure
# #coffee_data.head()
# # Clean the dataset by filling in missing values for the relevant columns used in the recommendation system.
# # For simplicity, we will fill missing values with placeholder text (e.g., 'Unknown') where applicable.

# # List of columns relevant to the recommendation system
# relevant_columns = ['Flavor', 'Roast Level', 'Acidity', 'Drink Type', 'Country', 
#                     'Health Benefit', 'Description', 'Drink Time', 'Strength']

# # Fill NaN values with 'Unknown' or a default value
# coffee_data_cleaned = coffee_data[relevant_columns].fillna('Unknown')

# # Save the cleaned dataset for integration into the Flask app
# #cleaned_file_path = '/mnt/data/cleaned_coffee_data.csv'
# coffee_data_cleaned.to_csv('coffee_data.csv', index=True)

# #cleaned_file_path
print ('your jobe is done ')
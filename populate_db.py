import sqlite3
from database import insert_coffee

# Initialize the database and create the table
def create_table():
    conn = sqlite3.connect('coffee_recommendation.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS coffee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Flavor TEXT NOT NULL,
            Roast_Level TEXT NOT NULL,
            Acidity TEXT NOT NULL,
            Drink_Type TEXT NOT NULL,
            Country TEXT NOT NULL,
            Health_Benefit TEXT NOT NULL,
            Description TEXT NOT NULL,
            Video_URL TEXT NOT NULL,
            Drink_Time TEXT NOT NULL,
            Strength TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Populate the database with some sample data
def populate_data():
    # Sample coffee data
    coffees = [
        ('Fruity', 'Light', 'Medium', 'Drip', 'Ethiopia', 'Antioxidant-rich', 'Fruity and vibrant', 'https://example.com/video1', 'Morning', 'Mild'),
        ('Nutty', 'Medium', 'Low', 'Espresso', 'Brazil', 'Boosts Metabolism', 'Rich and smooth', 'https://example.com/video2', 'Afternoon', 'Strong'),
        # Add more entries as needed
    ]

    for coffee in coffees:
        insert_coffee(*coffee)

if __name__ == '__main__':
    create_table()  # Create table if it doesn't exist
    # clear_coffee_data() # Clear existing data (if needed)
    populate_data()  # Populate the table with new data
    print('Your work is done')

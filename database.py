import sqlite3

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('coffee_recommendation.db')
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

# Fetch all coffee data from the database
def get_all_coffees():
    conn = get_db_connection()
    coffees = conn.execute('SELECT * FROM coffee').fetchall()
    conn.close()
    return [dict(coffee) for coffee in coffees]

# Insert a new coffee record into the database (useful for population)
def insert_coffee(flavor, roast_level, acidity, drink_type, country, health_benefit, description, video_url, drink_time, strength):
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO coffee (Flavor, Roast_Level, Acidity, Drink_Type, Country, Health_Benefit, Description, Video_URL, Drink_Time, Strength)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (flavor, roast_level, acidity, drink_type, country, health_benefit, description, video_url, drink_time, strength))
    conn.commit()
    conn.close()

# Clear the coffee table (optional for re-populating)
def clear_coffee_data():
    conn = get_db_connection()
    conn.execute('DELETE FROM coffee')
    conn.commit()
    conn.close()

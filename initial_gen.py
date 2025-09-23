import sqlite3
import random
from random import randrange
from datetime import timedelta, datetime
import os


def create_cats():
    name = [
        "Whiskers",
        "Luna",
        "Oliver",
        "Bella",
        "Charlie",
        "Lucy",
        "Leo",
        "Milo",
        "Lily",
        "Simba",
        "Chloe",
        "Max",
        "Nala",
        "Jack",
        "Sophie",
        "Tiger",
        "Zoe",
        "Jasper",
        "Cleo",
        "Oscar",
        "NULL",
        "Mittens",
    ]
    breed = ["Siamese", "Maine Coon", "Tabby", "Persian"]
    temperament = ["Playful", "Reserved", "Calm", "Energetic"]
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Cats(
                       cat_id INTEGER PRIMARY KEY,
                       name TEXT ,
                       breed TEXT NOT NULL,
                       temperament TEXT NOT NULL,
                       is_adopted INTEGER NOT NULL
                       )"""
    )
    cursor.executemany(
        "insert into Cats (name,breed,temperament,is_adopted) values (?,?,?,?)",
        [
            (
                random.choice(name),
                random.choice(breed),
                random.choice(temperament),
                random.choice([0, 1]),
            )
            for x in range(50000)
        ],
    )
    conn.commit()


def create_customers():
    name = [
        "Oliver",
        "Jane",
        "Emma",
        "John",
        "Michael",
        "Sarah",
        "David",
        "Lisa",
        "James",
        "Emily",
        "William",
        "Sophie",
        "Daniel",
        "Rachel",
        "Thomas",
        "Laura",
        "Robert",
        "Anna",
        "Joseph",
        "Maria",
    ]
    surname = [
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Miller",
        "Davis",
        "Rodriguez",
        "Martinez",
        "Hernandez",
        "Lopez",
        "Gonzalez",
        "Wilson",
        "Anderson",
        "Thomas",
        "Taylor",
        "Moore",
        "Jackson",
        "Martin",
        "Lee",
        "Perez",
        "Thompson",
        "White",
        "Harris",
        "Sanchez",
        "Clark",
        "Ramirez",
        "Lewis",
        "Robinson",
    ]
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Customers (
                        customer_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL
                        
                        )"""
    )
    cursor.executemany(
        "insert into Customers (name,email) values (?,?)",
        [
            (
                random.choice(name),
                random.choice(name) + "." + random.choice(surname) + "@gmail.com",
            )
            for x in range(500)
        ],
    )
    cursor.execute(
        "insert into Customers (name,email) values (?,?)",
        [
            (
                random.choice(name),
                random.choice(name) + "." + random.choice(surname) + "@gmail.com",
            )
            for x in range(500)
        ],
    )
    conn.commit()


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def create_adoptions():
    d1 = datetime.strptime("1/1/2020 1:30 PM", "%m/%d/%Y %I:%M %p")
    d2 = datetime.strptime("1/1/2025 4:50 AM", "%m/%d/%Y %I:%M %p")

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Adoptions (
                    adoption_id INTEGER PRIMARY KEY, 
                    cat_id INTEGER NOT NULL, 
                    customer_id INTEGER NOT NULL, 
                    adoption_date TEXT NOT NULL,
                    FOREIGN KEY (cat_id) REFERENCES Cats(cat_id),
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                    
                    )"""
    )
    cursor.executemany(
        "insert into Adoptions (cat_id,customer_id,adoption_date) values (?,?,?)",
        [(random.randint(1, 50000), x, random_date(d1, d2)) for x in range(500)],
    )
    conn.commit()


def create_suppliers():
    supplier_names = [
        "PawPerfect Pet Foods",
        "WhiskerWell Supply Co.",
        "Feline Feast Industries",
        "CatCare Nutrition Ltd",
        "Purringtons Premium Foods",
    ]

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Suppliers (
                    supplier_id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL
                    )"""
    )
    cursor.executemany(
        "insert into Suppliers (name) values (?)",
        [(random.choice(supplier_names),) for x in range(5)],
    )
    conn.commit()


def create_food():
    food_names = [
        "Gourmet Salmon Feast",
        "Chicken Delight",
        "Tuna Supreme",
        "Beef Medley",
        "Ocean Fish Dinner",
        "Indoor Cat Formula",
        "Kitten Growth",
        "Senior Care Mix",
        "Hairball Control",
        "Weight Management",
        "Seafood Sensation",
        "Turkey & Giblets",
        "Lamb & Rice",
        "Duck Pate",
        "Shrimp Dinner",
        "Grain Free Classic",
        "Dental Health",
        "Protein Plus Mix",
        "Natural Balance",
        "Urinary Care",
        "Salmon Crunch",
        "Chicken Kibble",
        "Fish & Chips",
        "Meaty Bits",
        "Crunchy Treats",
        "Catnip Crisps",
        "Tender Morsels",
        "Wholesome Blend",
        "Savory Salmon",
        "Premium Pate",
        "Catnip Bites",
    ]
    categories = ["Wet Food", "Dry Food", "Treat"]

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Food (
                    food_id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL, 
                    category TEXT , 
                    price DECIMAL NOT NULL,
                    stock_quantity INTEGER NOT NULL,
                    supplier_id INTEGER,
                    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)                    
                    )"""
    )
    cursor.executemany(
        "insert into Food (name,category,price,stock_quantity,supplier_id) values (?,?,?,?,?)",
        [
            (
                random.choice(food_names),
                random.choice(categories),
                round(random.random() * 100, 2),
                random.randint(0, 300),
                random.choice(range(1, 5)),
            )
            for x in range(3000)
        ],
    )
    conn.commit()


if __name__ == "__main__":

    if "cat_cafe.db" not in os.listdir():
        print("Creating database and populating with data...")
        conn = sqlite3.connect("cat_cafe.db")
        cursor = conn.cursor()

        create_cats()
        create_customers()
        create_adoptions()
        create_suppliers()
        create_food()
        conn.close()
        print("Database created and populated.")
    else:
        print("Database already exists.")

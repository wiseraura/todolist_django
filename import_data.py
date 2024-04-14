import psycopg2

# Database connection details (replace with your own)
HOST = "localhost"
PORT = 5432
DATABASE = "todo"
USER = "postgres"
PASSWORD = "postgres"

# SQL statement (modify if needed)
INSERT_DATA_QUERY = """
INSERT INTO app2_user (name, dob, hometown, school)
VALUES (%s, %s, %s, %s);
"""

def connect_to_db():
  try:
    conn = psycopg2.connect(host=HOST, port=PORT, dbname=DATABASE, user=USER, password=PASSWORD)
    return conn
  except (Exception, psycopg2.Error) as error:
    print("Error connecting to database:", error)
    return None

def insert_data(conn, data):
  try:
    cursor = conn.cursor()
    for row in data:
      cursor.execute(INSERT_DATA_QUERY, row)
    conn.commit()
    print("Data imported successfully!")
  except (Exception, psycopg2.Error) as error:
    print("Error inserting data:", error)


conn = connect_to_db()
if conn:
# Replace this with your actual user data
    user_data = [
        ('Leo Mckee','2021-12-02','Naga','Ut Sagittis Lobortis LLP'),
        ('Malcolm Nash','2021-09-10','Serang','Sit Amet Institute'),
        ('Hayes Dorsey','2021-08-22','Monterrey','Maecenas Libero PC'),
        ('Zephr Hunt','2022-03-28','Mala','Sed Consulting'),
        ('Ann Richmond','2021-04-22','Bauchi','Justo Faucibus Lectus Consulting'),
        ('Tyrone Downs','2022-02-05','Lelystad','Amet Faucibus Ut Incorporated'),
        ('Lacy Stone','2020-03-22','Richmond','Nisi Dictum Augue PC'),
        ('Griffin Small','2021-09-02','Sheikhupura','Imperdiet Erat Consulting'),
        ('Trevor Bryant','2022-07-21','Hervey Bay','Et PC'),
        ('Christian Buck','2022-01-16','Saratov','Scelerisque Mollis LLP'),
        ('Cooper Willis','2020-02-14','Perk','Luctus Aliquet Odio Ltd'),
        ('Paula Velez','2021-02-13','Cork','Molestie Tortor Nibh Foundation'),
        ('Jamalia Cortez','2022-03-04','Iguala','Fringilla Mi LLC'),
        ('Brianna Marks','2021-09-22','Leersum','Consectetuer PC'),
        ('Brandon Baldwin','2021-06-29','Hồ Chí Minh City','Turpis Nec Ltd'),
        ('Brendan Farley','2023-03-04','Racine','Dignissim Lacus Aliquam Corporation'),
        ('Jenette Reese','2021-05-11','Landeck','Rutrum Urna Nec Corp.'),
        ('Colt Kramer','2022-04-09','Saint-Nazaire','Nascetur Ridiculus Mus Company'),
        ('Zenaida Melton','2021-10-12','Guadalupe','Eu Ligula LLC'),
        ('Iliana Mcguire','2022-12-24','Pasig','Cras Vulputate LLP')
    ]
    insert_data(conn, user_data)
    conn.close()
else:
    print("Failed to connect to database.")
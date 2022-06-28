import mysql.connector
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Isaac@18!",
  database ="car_service"
)
mycursor = conn.cursor()
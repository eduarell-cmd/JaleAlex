import os

def get_db_connection(): 
   try:
      DB_HOST = "localhost"
      DB_USER = "root"      
      DB_PASSWORD = ""       
      DB_NAME = "carros"
      
      SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
      SQLALCHEMY_TRACK_MODIFICATIONS = False
      
      print(f"Hola")
      return
   except Exception as e :
      print(f"Valio: {e}")


connection = get_db_connection()
connection = get_db_connection()
import pymysql
def get_db_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="carros",
            cursorclass=pymysql.cursors.DictCursor  # Devuelve resultados en formato diccionario
        )
        return conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

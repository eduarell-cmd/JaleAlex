from flask import *
from flask_sqlalchemy import SQLAlchemy
from conn import *
from models import *

app = Flask(__name__)

nissan = Agencia()
@app.route("/", methods=['GET'])
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM autos")
    autos = cursor.fetchall()
    nissan.inventario(autos)
    carros= nissan.carros
    
    return render_template('papu.html',autos=carros)

@app.route("/venta")
def venta():
    
    #carro = nissan.carros[0]
    
    #financiamientos = ProcesoVenta.validar_costo(carro)
    return render_template('venta.html')





if __name__ == "__main__":
    app.run(debug=True)

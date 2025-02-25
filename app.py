from flask import *
from flask_sqlalchemy import SQLAlchemy
from conn import *
from models import *

app = Flask(__name__)

nissan = Agencia()
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM autos")
autos2 = cursor.fetchall()
nissan.inventario(autos2)
carros= nissan.carros

@app.route("/", methods=['GET'])
def home():
    return render_template('papu.html',autos=carros)

@app.route('/venta')
def venta():
    button_id = request.args.get('id',0)
    print(button_id)
    if button_id ==0:
        return redirect('/')
    car = carros[int(button_id)-1]
    financiamiento = ProcesoVenta.validar_costo(car)
    return render_template('venta.html',financiamientos = financiamiento,car=car)

@app.route('/vender_carro', methods=['POST'])
def vender_carro():
    carro_id = request.form.get("carro_id")  
    cliente = "ClienteEjemplo"  
    carro_a_vender = next((carro for carro in nissan.carros if str(carro.id) == carro_id), None)
    if carro_a_vender:
        nissan.vender_carro(cliente, carro_a_vender)
        return render_template('papu.html',autos=carros)
    else:
        return "Error: Carro no encontrado", 404
    
    

if __name__ == "__main__":
    app.run(debug=True)

from flask import *
from flask_sqlalchemy import SQLAlchemy
from conn import *
app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM autos")
    autos = cursor.fetchall()
    return render_template('papu.html',autos=autos)

if __name__ == "__main__":
    app.run(debug=True)

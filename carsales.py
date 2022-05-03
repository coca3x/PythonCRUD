from flask import (Flask, render_template, jsonify)
import pyodbc

carsales = Flask(__name__)

def connection():
    server_name = 'localhost'
    database = 'CarSales' 
    user = 'SA'
    pass_ = 'Lem0nCode!'
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_name+';DATABASE='+database+';UID='+user+';PWD='+ pass_
    conn = pyodbc.connect(cstr)
    return conn

@carsales.route("/")
def main():
    data=[]
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.TblCars")
    data = cursor
    for row in cursor.fetchall():
        cars.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
    conn.close()
    cars = cars
    #return jsonify(cars) This is for return data in JSON to consume in other app, use POSTMAN for consume
    return render_template("carslist.html", cars = cars)

if(__name__ == "__main__"):
    carsales.run()
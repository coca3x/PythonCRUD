from flask import (Flask, render_template, jsonify, request, redirect)
import pyodbc

carsales = Flask(__name__)

#DB connection
def connection():
    server_name = 'localhost'
    database = 'CarSales' 
    user = 'SA'
    pass_ = 'Lem0nCode!'
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_name+';DATABASE='+database+';UID='+user+';PWD='+ pass_
    conn = pyodbc.connect(cstr)
    return conn

#Index and show all data
@carsales.route("/",methods = ['GET'])
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

#Add new car in other page
@carsales.route("/addcar", methods = ['GET','POST'])
def addcar():
    if request.method == 'GET':
        return render_template("addcar.html", car = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        year = int(request.form["year"])
        price = float(request.form["price"])
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dbo.TblCars (id, name, year, price) VALUES (?, ?, ?, ?)", id, name, year, price)
        conn.commit()
        conn.close()
        return redirect('/')

#Update existing register
@carsales.route('/updatecar/<int:id>',methods = ['GET','POST'])
def updatecar(id):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM dbo.TblCars WHERE id = ?", id)
        for row in cursor.fetchall():
            cr.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
        conn.close()
        return render_template("addcar.html", car = cr[0])
    if request.method == 'POST':
        name = str(request.form["name"])
        year = int(request.form["year"])
        price = float(request.form["price"])
        cursor.execute("UPDATE dbo.TblCars SET name = ?, year = ?, price = ? WHERE id = ?", name, year, price, id)
        conn.commit()
        conn.close()
        return redirect('/')

#Delete car
@carsales.route('/deletecar/<int:id>')
def deletecar(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dbo.TblCars WHERE id = ?", id)
    conn.commit()
    conn.close()
    return redirect('/')

if(__name__ == "__main__"):
    carsales.run()
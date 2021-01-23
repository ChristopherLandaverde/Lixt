import pymysql
from uuid import uuid4
import datetime
import uuid
from app import app
from db import mysql,db_connection
from flask import jsonify,request



@app.route("/v1/groceries",methods=["GET"])
def get_gaitems():
    try:
        cursor = db_connection()
        if request.method == "GET":
            cursor.execute("SELECT * FROM Grocery_List")
            row = cursor.fetchall()
            resp = jsonify(row)
            resp.status_code=200
            return resp
        else:
            resp = jsonify('User "id" not found in query string')
            resp.status_code = 500
            return resp
        
    except Exception as e:
        print(e)
        

        

@app.route("/v1/groceries",methods=["POST"])
def post_gaitems():
    try:
        if request.method == "POST":
            if request.mimetype == 'application/json':
                data = request.get_json(force=True)
                new_item=data['name']
                item_created_by=data['createdBy']
                return  "JSON value sent: " + "Name: " +new_item + " createdBy: "+ item_created_by
            else:
                today = datetime.datetime.now()
                new_item=request.form['name']
                item_created_by=request.form['createdBy']
                cursor = db_connection()
                cursor.execute("""INSERT INTO Grocery_List (name,createdBy,ID,createdAt) VALUES(%s,%s,%s,%s)""",(new_item,item_created_by,uuid.uuid4(),today))
                mysql.connection.commit()
                cursor.close()
                return ("Item has been added succesfully"),200
    except Exception as e:
        print(e)


@app.route("/v1/groceries",methods=["DELETE"])    
def delete_gaitems():
    try:
        if request.method == "DELETE":
            if request.mimetype =='application/json':
                data=request.get_json(force=True)
                new_item=data['name']
                item_created_by=data['createdBy']
                return  "JSON value deleted: " + "Name: " +new_item + " createdBy: "+ item_created_by
            else:
                new_item=request.form['name']
                item_created_by=request.form['createdBy']
                cursor.execute("""DELETE FROM Grocery_List WHERE name=%s and createdBy=%s""",(new_item,item_created_by))
                mysql.connection.commit()
                cursor.close()
                return ("Item has been deleted succesfully"),200
    except Exception as e:
        print(e)
        
@app.route("/v1/groceries/createdBy",methods=["PUT"])    
def put_gaitems():
    try:
        if request.method == "PUT":
            if request.mimetype =='application/json':
                data=request.get_json(force=True)
                new_item=data['name']
                item_created_by=data['createdBy']
                return  "JSON value updated: " + "Name: " +new_item + " createdBy: "+ item_created_by
            else:
                new_item=request.form['name']
                item_created_by=request.form['createdBy']
                cursor = db_connection()
                cursor.execute("""UPDATE Grocery_List SET name=%s WHERE createdBy=%s""",(new_item,item_created_by))
                mysql.connection.commit()
                cursor.close()
                return "Item has been edited succesfully",200
    except Exception as e:
        print(e)
    


@app.route("/v1/users",methods=["GET"])
def single_item():
    try:
        id = request.args.get('createdBy')
        if id:
            cursor = db_connection() 
            cursor.execute("""SELECT * FROM Grocery_List WHERE createdBy='%s'""" % (id))
            row = cursor.fetchall()
            resp = jsonify(row)
            resp.status_code=200
            return resp
        else:
            resp = jsonify('User "id" not found in query string')
            resp.status_code = 500
            return resp

    except Exception as e:
        print(e)

#server
if __name__ == '__main__':
    app.run(debug=True)
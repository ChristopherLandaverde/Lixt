from flask import Flask,request,jsonify
import datetime
from flask_mysqldb import MySQL 
import uuid
from uuid import uuid4
import pymysql




#Init App
app = Flask(__name__)
mysql = MySQL(app)


#Initalize Database Connection 
def db_connection():
    conn = None
    try:
        conn = pymysql.connect(host="us-cdbr-east-03.cleardb.com",database="heroku_f5879903a4c3f63",user="be28232db9c2a4",password='eb3b45b0',cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor() 
    except pymysql.Error as err:
        print("Something went wrong: {}".format(err))
    return conn
        

@app.route("/v1/",methods=["GET","POST","DELETE","PUT"])
def gaitems():
    today = datetime.datetime.now()
    conn = db_connection()
    cursor=conn.cursor()
    
    if request.method == "GET":
        cursor.execute("SELECT * FROM Grocery_List")
        items=[
            dict(id=row['ID'],userID=row['UserID'],Title=row['Title'],
                 createdAt=row['createdAt'],createdBy=row['createdBy'],lastEdited=row['lastEdited'],lastEditedBy=row['lastEditedBy'])
                 for row in cursor.fetchall()
                 ]
        if items is not None:
            return jsonify(items)
    
    if request.method == "POST":
        new_item=request.form['Title']
        item_created_by=request.form['createdBy']
        cursor.execute("""INSERT INTO Grocery_List (Title,createdBy,ID,createdAt)
        VALUES(%s,%s,%s,%s)""",(new_item,item_created_by,uuid.uuid4(),today))
        conn.commit()
        return ("Item has been added succesfully"),200
            
    
    if request.method == "DELETE":
        new_item=request.form['Title']
        item_created_by=request.form['createdBy']
        cursor.execute("""DELETE FROM Grocery_List WHERE Title=%s and createdBy=%s""",(new_item,item_created_by))
        conn.commit()
        return ("Item has been deleted succesfully"),200
    
    if request.method == "PUT":
        new_item=request.form['Title']
        item_created_by=request.form['createdBy']
        cursor.execute("""UPDATE Grocery_List SET Title=%s WHERE createdBy=%s""",(new_item,item_created_by))
        conn.commit()
        return "Item has been edited succesfully",200
    


@app.route("/v1/<createdBy>",methods=["GET","DELETE"])
def single_item(createdBy):
    today = datetime.datetime.now()
    conn = db_connection()
    cursor=conn.cursor()
    book = None
    
    if request.method == "GET":
        cursor.execute("""SELECT * FROM Grocery_List WHERE createdBy=%s""",(createdBy))
        items=[
            dict(id=row['ID'],userID=row['UserID'],Title=row['Title'],createdAt=row['createdAt'],createdBy=row['createdBy'],lastEdited=row['lastEdited'],lastEditedBy=row['lastEditedBy'])
            for row in cursor.fetchall()]
        for r in items:
            book = r
        if r is not None:
            return jsonify(items), 200
        else:
            return "Something is wrong", 404
        

#server
if __name__ == '__main__':
    app.run(debug=False)
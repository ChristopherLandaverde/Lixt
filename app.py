from flask import Flask,request,jsonify
from flask.views import View
import datetime
import configparser
from flask_mysqldb import MySQL 
import uuid
from uuid import uuid4





# Configuring Environment Variables

config = configparser.ConfigParser()
config.read('.env')

app = Flask(__name__)

# Local DB Configuration

app.config['MYSQL_USER'] = config['local']['user']
app.config['MYSQL_PASSWORD'] = config['local']['password']
app.config['MYSQL_DB'] = config['local']['database']
app.config['MYSQL_CURSORCLASS'] = config['local']['cursor']


### Heroku Configuration

#app.config['MYSQL_USER'] = config['heroku']['user']
#app.config['MYSQL_HOST'] = config['heroku']['host']
#app.config['MYSQL_PASSWORD'] = config['heroku']['password']
#app.config['MYSQL_DB'] = config['heroku']['database']
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



#Init App

mysql = MySQL(app)


#Initalize Database Connection 
    
def db_connection():
    try:
        cur = mysql.connection.cursor()
    except Exception as e:
        raise(e)
    return cur

        

@app.route("/v1/groceries",methods=["GET"])
def get_gaitems():
    today = datetime.datetime.now()
    cursor = db_connection()
    if request.method == "GET":
        cursor.execute("SELECT * FROM Grocery_List")
        items=[dict(id=row['ID'],userID=row['UserID'],name=row['name'],createdAt=row['createdAt'],createdBy=row['createdBy'],lastEdited=row['lastEdited'],lastEditedBy=row['lastEditedBy']) for row in cursor.fetchall()]
        if items is not None:
            return jsonify(items)

@app.route("/v1/groceries",methods=["POST"])
def post_gaitems():
    if request.method == "POST":
        if request.mimetype == 'application/json':
            data = request.get_json(force=True)
            new_item=data['name']
            item_created_by=data['createdBy']
        else:
            new_item=request.form['name']
            item_created_by=request.form['createdBy']
            cursor.execute("""INSERT INTO Grocery_List (name,createdBy,ID,createdAt) VALUES(%s,%s,%s,%s)""",(new_item,item_created_by,uuid.uuid4(),today))
            mysql.connection.commit()
            cursor.close()
            return ("Item has been added succesfully"),200

@app.route("/v1/groceries",methods=["DELETE"])    
def delete_gaitems():
    if request.method == "DELETE":
        new_item=request.form['name']
        item_created_by=request.form['createdBy']
        cursor.execute("""DELETE FROM Grocery_List WHERE name=%s and createdBy=%s""",(new_item,item_created_by))
        mysql.connection.commit()
        cursor.close()
        return ("Item has been deleted succesfully"),200

@app.route("/v1/groceries",methods=["PUT"])    
def put_gaitems():
    if request.method == "PUT":
        new_item=request.form['name']
        item_created_by=request.form['createdBy']
        cursor.execute("""UPDATE Grocery_List SET name=%s WHERE createdBy=%s""",(new_item,item_created_by))
        mysql.connection.commit()
        cursor.close()
        return "Item has been edited succesfully",200
    


@app.route("/v1/<createdBy>",methods=["GET"])
def single_item(createdBy):
    today = datetime.datetime.now()
    cursor = db_connection() 
    book = None
    
    if request.method == "GET":
        cursor.execute("""SELECT * FROM Grocery_List WHERE createdBy='%s'""" % (createdBy))
        items=[
            dict(id=row['ID'],userID=row['UserID'],name=row['name'],createdAt=row['createdAt'],createdBy=row['createdBy'],lastEdited=row['lastEdited'],lastEditedBy=row['lastEditedBy'])
            for row in cursor.fetchall()]
        for r in items:
            book = r
        if r is not None:
            return jsonify(items), 200
        else:
            return "Something is wrong", 404
        

#server
if __name__ == '__main__':
    app.run(debug=True)
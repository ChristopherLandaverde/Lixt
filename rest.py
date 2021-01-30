import uuid
import datetime
from flask import jsonify,request
from db import mysql,db_connection,app



def form(x):
    data = request.get_json(force=True)
    return data[x]

def cur(*args):
    cursor = db_connection()
    cursor.execute(*args)
    mysql.connection.commit()
    cursor.close()


def fetchall_cur(x):
    if x:
        cursor = db_connection()
        cursor.execute(x)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code=200
        return resp
    else:
        resp = jsonify('User "id" not found in query string')
        resp.status_code = 500
        return resp





@app.route("/v1/groceries",methods=["GET"])
def get_gaitems():
    if request.mimetype == 'application/json':
        all_items =fetchall_cur("""SELECT * FROM Grocery_List""")
        return all_items


@app.route("/v1/groceries",methods=["POST"])
def post_gaitems():
        if request.mimetype == 'application/json':
            new_item=form('name')
            item_created_by=form('createdBy')
            x = cur("""INSERT INTO Grocery_List (name,createdBy,ID,createdAt) VALUES (%s,%s,%s,%s)""",(new_item,item_created_by,uuid.uuid4(),datetime.datetime.now()))
            return ("Item has been added succesfully"),200



@app.route("/v1/groceries",methods=["DELETE"])
def delete_gaitems():
    if request.mimetype == 'application/json':
        new_item=form('name')
        item_created_by=form('createdBy')
        x = cur("""DELETE FROM Grocery_List WHERE name=%s and createdBy=%s""",(new_item,item_created_by))
        return ("Item has been deleted succesfully"),200

@app.route("/v1/groceries/createdBy",methods=["PUT"])
def put_gaitems():
    if request.mimetype == 'application/json':
        new_item=form('name')
        item_created_by=form('createdBy')
        time_created=form('timeCreated')
        cur("""UPDATE Grocery_List SET name=%s WHERE createdBy=%s AND timeCreated= %s""",(new_item,item_created_by,time_created))
        return "Item has been edited succesfully",200



@app.route("/v1/users",methods=["GET"])
def single_item():
    try:
        id = request.args.get('createdBy')
        if id:
            user_items = fetchall_cur("""SELECT * FROM Grocery_List WHERE createdBy='%s'""" % (id))
            return user_items

    except Exception as e:
        print(e)


#server
if __name__ == '__main__':
    app.run(debug=True)

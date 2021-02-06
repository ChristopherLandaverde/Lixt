import uuid
from flask import jsonify,request
from db import mysql,db_connection,app

def form(json_request):
    data = request.get_json(force=True)
    return data[json_request]
def cur(*args):
    cursor = db_connection()
    cursor.execute(*args)
    mysql.connection.commit()
    cursor.close()

def fetchall_cur(fetchall_query):
    cursor = db_connection()
    cursor.execute(fetchall_query)
    row = cursor.fetchall()
    resp = jsonify(row)
    resp.status_code=200
    return resp

@app.route("/v1/groceries",methods=["GET"])
def get_gaitems():
    if request.mimetype == 'application/json':
        all_items =fetchall_cur("""SELECT * FROM Grocery_List""")
        return all_items
    return ("Method is not JSON, please submit JSON"),500
@app.route("/v1/groceries",methods=["POST"])
def post_gaitems():
    if request.mimetype == 'application/json':
        new_item=form('name')
        item_created_by=request.headers['userID']
        cur("""INSERT INTO Grocery_List (name,createdBy,ID) VALUES (%s,%s,%s)""",
            (new_item,item_created_by,uuid.uuid4()))
        return ("Item has been added succesfully"),200
    return ("No item has been added"),500
@app.route("/v1/groceries",methods=["DELETE"])
def delete_gaitems():
    if request.mimetype == 'application/json':
        new_item=form('name')
        item_created_by=request.headers['userID']
        cur("""DELETE FROM Grocery_List WHERE name=%s and createdBy=%s""",
            (new_item,item_created_by))
        return ("Item has been deleted succesfully"),200
    return "No item has been deleted",500
@app.route("/v1/groceries/createdBy",methods=["PUT"])
def put_gaitems():
    if request.mimetype == 'application/json':
        new_item=form('name')
        item_created_by=request.headers['userID']
        cur("""UPDATE Grocery_List
            SET name=%s WHERE userID=%s""",
            (new_item,item_created_by))
        return "Item has been edited succesfully",200
    return "No item has been edited",500
@app.route("/v1/users",methods=["GET"])
def single_item():
    userid_queryparam = request.args.get('userID')
    if userid_queryparam:
        user_items = fetchall_cur("""SELECT *
                                  FROM Grocery_List
                                  WHERE createdBy='%s'""" %
                                  (userid_queryparam))
        return user_items
    return "No item has been found",500
#server
if __name__ == '__main__':
    app.run(debug=True)

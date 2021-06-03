import uuid
from flask import jsonify, request
from db import mysql, db_connection, app


# function allows for body json request
def json_body(json_request):
    data = request.get_json(force=True)
    return data[json_request]


# function allows for SQL request

def cursor_request(*args):
    cursor = db_connection()
    cursor.execute(*args)
    mysql.connection.commit()
    cursor.close()


# function allows for SQL request and retrieval of API response.

def fetchall_cursor(fetchall_query):
    cursor = db_connection()
    cursor.execute(fetchall_query)
    row = cursor.fetchall()
    resp = jsonify(row)
    resp.status_code = 200
    return resp

# Retrieves all of Grocery Items
@app.route("/v1/groceries",methods=["GET"])
def get_gaitems():
    if request.mimetype == "application/json":
        all_items = fetchall_cursor("""SELECT * FROM Grocery_List""")
        return all_items
    return ("Here are your items"),500


@app.route("/v1/groceries", methods=["POST"])
def post_gaitems():
    if request.mimetype == "application/json":
        new_item = json_body("name")
        item_created_by = request.headers["userID"]
        cursor_request(
            """INSERT INTO Grocery_List (Name,UserID,ID) VALUES (%s,%s,%s)""",
            (new_item, item_created_by, uuid.uuid4()),
        )
        return jsonify(new_item, item_created_by), 200
    return ("No item has been added"), 500


@app.route("/v1/groceries", methods=["DELETE"])
def delete_gaitems():
    if request.mimetype == "application/json":
        eventid_queryparam = request.args.get("ID")
        new_item = json_body("name")
        cursor_request(
            """DELETE FROM Grocery_List WHERE ID=%s AND name =%s """,
            (eventid_queryparam, new_item),
        )
        return jsonify(eventid_queryparam, new_item), 200
    return "No item has been deleted", 500

# Edits on an item from the Grocery List.
@app.route("/v1/groceries",methods=["PUT"])
def put_gaitems():
    if request.mimetype == "application/json":
        eventid_queryparam = request.args.get("ID")
        new_item = json_body("name")
        item_created_by = request.headers["userID"]
        cursor_request(
            """UPDATE Grocery_List
            SET name=%s,lastEditedBy=%s WHERE ID=%s""",
            (new_item, item_created_by, eventid_queryparam),
        )
        return jsonify(new_item, eventid_queryparam, item_created_by), 200
    return "No item has been edited", 500


# Retreives all grocery list from the Users.
@app.route("/v1/users",methods=["GET"])
def single_item():
    userid_queryparam = request.args.get("userID")
    if request.mimetype == "application/json":
        user_items = fetchall_cursor(
            """SELECT *
                                  FROM Grocery_List
                                  WHERE userID='%s'"""
            % (userid_queryparam)
        )
        return user_items
    return "No item has been found", 500


# server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



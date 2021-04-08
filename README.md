
![the art box-2](https://user-images.githubusercontent.com/22153509/113756574-8fd66d00-96df-11eb-9d8b-66b3feffafc3.png)




This is version 2 for Project Lixt.

Completed Tasks:
- Developer would be able to recieve all information in the app with a GET request.
- Developer will be able to post a grocery item with a POST request.
- Developer will be able to edit a grocery item with a PUT request.
- Developer will be able to delete a grocery item wtih a GET request.
- Developer will be able to retrieve all orders POST by a user with api parameter.



## How to Install & Run

Make Virtual Environment.

```python
virtualenv {virtual environment name}
```

Install and update using pip:
```python
pip install -r requirements.txt
```
Requirements
```python
astroid==2.4.2
attrs==20.3.0
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
Flask==1.1.2
Flask-MySQLdb==0.2.0
idna==2.10
iniconfig==1.1.1
isort==5.7.0
itsdangerous==1.1.0
Jinja2==2.11.3
lazy-object-proxy==1.4.3
MarkupSafe==1.1.1
mccabe==0.6.1
mysqlclient==2.0.3
packaging==20.9
pluggy==0.13.1
py==1.10.0
pylint==2.6.0
pyparsing==2.4.7
pytest==6.2.2
requests==2.25.1
six==1.15.0
toml==0.10.2
urllib3==1.26.3
Werkzeug==1.0.1
wrapt==1.12.1
```

Run Server:
```python
python rest.py
```
Run Pytest:
```python
python testapp.py
```
Run linting:
```bash
pylint src/*.py
```

## Initalize SQL DB locally

** Must be run within MySQL shell and not bash**

Migration Script:

```shell
mysql -u root -p
```

```SQL
source migration_script01292021.sql
```

SQL Dumps:

```shell
 mysql -u root -p FLAPI > flapischema.sql
```

## API Endpoint

```html
http://0.0.0.0:5000/v1/groceries

```

## Run Server Unit Test

```python
python rest.py
```

|        	|                                                                  	|                	|                 	|                          	|
|--------	|------------------------------------------------------------------	|----------------	|-----------------	|--------------------------	|
| Method 	| Action                                                           	| Entry Required 	| Header Required 	| Query Parameter Required 	|
| GET    	| Retrieves all items from the Grocery list.                       	| N/A            	| N/A             	| N/A                      	|
| POST   	| Creates Items, User,ID, Current Date to add to the shopping list 	| **name**           	| N/A             	| **userID**                  	|
| DELETE 	| Deletes Singular Item Created by Specific User.                  	|  **name**            	| N/A             	| **ID of Grocery Item**       	|
| PUT    	| Edits Singular Item Created by Specific User                     	|  **name**            	| **userID**          	| **ID of Grocery Item**       	|
| GET    	| Retrieves all items from specific user                           	| N/A            	| N/A             	| **userID**                 	|





### RETRIEVE ALL PRODUCTS

Request: `GET http://0.0.0.0:5000/v1/groceries`

### Response

```json
[
  {
    "ID": "2c7539a7-ca11-4532-ac91-e6add4ce2b44",
    "lastEdited": "Tue, 06 Apr 2021 20:17:32 GMT",
    "lastEditedBy": "Milan",
    "name": "Chorizo",
    "timeCreated": "Tue, 06 Apr 2021 20:17:32 GMT",
    "userID": "Milan"
  },
  {
    "ID": "5cc9c260-135f-4d5b-8100-f27823742c75",
    "lastEdited": "Tue, 06 Apr 2021 20:18:18 GMT",
    "lastEditedBy": "Chris",
    "name": "Sour Cream",
    "timeCreated": "Tue, 06 Apr 2021 20:18:18 GMT",
    "userID": "Chris"
  }
]

```

# Create A  GROCERY ITEM

Request : `POST http://127.0.0.1:5000/v1/groceries`

Response:

```json

200 OK

["{GroceryItem}"

 "{userID}"]

```


# DELETE A PRODUCT

Request: `DELETE  http://127.0.0.1:5000/v1/groceries`

Response:

```json
200 OK - [
  "{ID}",
  "{Grocery Item}"
].
```

# Edit A PRODUCT

Request: `PUT http://127.0.0.1:5000/v1/groceries`

Response

```json
200 OK - "[
  "{Grocery Item}",
  "{ID}",
  "{lastEditedBy}"
]".


```

# Get All Items Ordered by User

Request: `GET http://127.0.0.1:5000/v1/{user}`

Response

```json
  {
    "ID": "dd14ceeb-8296-4051-baa3-95b29f49a145",
    "lastEdited": "Thu, 08 Apr 2021 07:22:06 GMT",
    "lastEditedBy": "Milan",
    "name": "Pizza",
    "timeCreated": "Wed, 07 Apr 2021 15:23:37 GMT",
    "userID": "Milan"
  },
 

```

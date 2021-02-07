# Lixt

This is version 1 for Project Lixt.

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

Run linting:
```bash
pylint ./*.py
```

## Initalize SQL DB locally

** Must be run within MySQL shell and not bash**

Migration Script:

```shell
mysql -u root -p
```

```SQL
source migration_script.sql
```

SQL Dumps:

```shell
 mysql -u root -p FLAPI > flapischema.sql
```

## API Endpoint

```html
http://127.0.0.1:5000/v1/groceries


```

## Run Server Unit Test

```python
pytest testapp.py


```

## View List
| Method | Action                                                           | Entry Required                           |
|--------|------------------------------------------------------------------|------------------------------------------|
| GET    | Retrieves all items for the shopping list.                       | **name createdBy** Capitalization Required* |
| POST   | Creates Items, User,ID, Current Date to add to the shopping list | **name  createdBy** CapitalizationRequired* |
| DELETE | Deletes Singular Item Created by Specific User.                  | **name createdBy** CapitalizationRequired*  |
| PUT    | Edits Singular Item Created by Specific User.                    | **name createdBy** CapitalizationRequired*  |


### RETRIEVE ALL PRODUCTS

Request: `GET http://127.0.0.1:5000/v1/groceries`

### Response

```json
{
[
{
    "ID": "922e4d0f-b2c3-4121-896b-fc24f178340a",
    "createdBy": "Milan",
    "lastEdited": "Sat, 06 Feb 2021 13:05:27 GMT",
    "lastEditedBy": "Milan",
    "name": "Chicken Fingers",
    "timeCreated": "Wed, 03 Feb 2021 11:35:52 GMT",
    "userID": "Milan"
  },
  {
   "ID": "83b9a2d8-a160-4ad3-ad29-c70b4721948b",
    "createdBy": "Milan",
    "lastEdited": "Sat, 06 Feb 2021 13:18:44 GMT",
    "lastEditedBy": "Milan",
    "name": "Machine",
    "timeCreated": "Sat, 06 Feb 2021 13:18:44 GMT",
    "userID": "Milan"
  },
  ]
}
```

# Create A  GROCERY ITEM

Request : `POST http://127.0.0.1:5000/v1/groceries`

Response:

```json

200 OK - (ID,name)
```


# DELETE A PRODUCT

Request: `DELETE  http://127.0.0.1:5000/v1/groceries/{{ID}}`

Response:

```json
200 OK -(ID, name) 

```

# Edit A PRODUCT

Request: `PUT http://127.0.0.1:5000/v1/groceries/{{ID}}`

Response

```json
200 OK - (ID,name)


```

# Get All Items Ordered by User

Request: `GET http://127.0.0.1:5000/v1/users?={{userId}}

Response

```json
  {
    "ID": "922e4d0f-b2c3-4121-896b-fc24f178340a",
    "createdBy": "Milan",
    "lastEdited": "Sat, 06 Feb 2021 13:05:27 GMT",
    "lastEditedBy": "Milan",
    "name": "Chicken Fingers",
    "timeCreated": "Wed, 03 Feb 2021 11:35:52 GMT",
    "userID": "Milan"
  },


```

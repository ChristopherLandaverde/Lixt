
![the art box-2](https://user-images.githubusercontent.com/22153509/113756574-8fd66d00-96df-11eb-9d8b-66b3feffafc3.png)




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
source migration_script.sql
```

SQL Dumps:

```shell
 mysql -u root -p FLAPI > flapischema.sql
```

## API Endpoint

```html
http://127.0.0.1:5000/v1


```

## Run Server Unit Test

```python
python rest.py


```

## View List
| Method | Action                                                           | Entry Required                           |
|--------|------------------------------------------------------------------|------------------------------------------|
| GET    | Retrieves all items for the shopping list.                       | **name createdBy** Capitalization Required* |
| PUT    | Creates Items, User,ID, Current Date to add to the shopping list | **name  createdBy** CapitalizationRequired*  |
| DELETE | Deletes Singular Item Created by Specific User.                  | **name createdBy** CapitalizationRequired*  |
| PUT    | Edits Singular Item Created by Specific User.                    | **name createdBy** CapitalizationRequired*  |


### RETRIEVE ALL PRODUCTS

Request: `GET http://127.0.0.1:5000/v1/`

### Response

```json
{
[
{
    "name": "Whoa",
    "createdAt": "Wed, 13 Jan 2021 16:50:01 GMT",
    "createdBy": null,
    "id": "c2be757d-55aa-4a6f-8fcc-44aad50420c2",
    "lastEdited": "Wed, 13 Jan 2021 21:50:01 GMT",
    "lastEditedBy": null,
    "userID": null
  },
  {
    "name": "All Bran",
    "createdAt": "Wed, 13 Jan 2021 17:26:15 GMT",
    "createdBy": "Chris",
    "id": "db21455f-dd9a-45c1-93f0-4c1bda7edc60",
    "lastEdited": "Wed, 13 Jan 2021 22:26:15 GMT",
    "lastEditedBy": null,
    "userID": null
  },
  ]
}
```

# Create A  GROCERY ITEM

Request : `POST http://127.0.0.1:5000/v1/groceries`

Response:

```json

200 OK - "Item has been added Succesfully"
```


# DELETE A PRODUCT

Request: `DELETE  http://127.0.0.1:5000/v1/groceries`

Response:

```json
200 OK - "Item has been succesfully deleted".
```

# Edit A PRODUCT

Request: `PUT http://127.0.0.1:5000/v1/groceries/createdBy`

Response

```json
200 OK - "Item has been edited succesfully".


```

# Get All Items Ordered by User

Request: `GET http://127.0.0.1:5000/v1/{createdBy}`

Response

```json
{
    "name": "Nope",
    "createdAt": "Wed, 13 Jan 2021 16:39:35 GMT",
    "createdBy": "Chris",
    "id": "63a68dbf-a7a4-4d61-9cad-97bc19ebd55b",
    "lastEdited": "Wed, 13 Jan 2021 21:39:36 GMT",
    "lastEditedBy": null,
    "userID": null
  },
  {
    "name": "Sour",
    "createdAt": "Wed, 13 Jan 2021 16:39:39 GMT",
    "createdBy": "Chris",
    "id": "08d38769-0076-49fd-95fa-52232d677639",
    "lastEdited": "Wed, 13 Jan 2021 21:39:39 GMT",
    "lastEditedBy": null,
    "userID": null
  },
  {
    "name": "All Bran",
    "createdAt": "Wed, 13 Jan 2021 17:26:15 GMT",
    "createdBy": "Chris",
    "id": "db21455f-dd9a-45c1-93f0-4c1bda7edc60",
    "lastEdited": "Wed, 13 Jan 2021 22:26:15 GMT",
    "lastEditedBy": null,
    "userID": null
  },


```

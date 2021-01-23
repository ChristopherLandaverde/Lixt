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
python v3.9.1
mysql v8.0.22
```

Run Server:
```python
python app.py
```

Run linting:
```bash
pylint ./*.py
```

## Initalize SQL DB locally

Migration Script:

```shell
mysql -u root -p
```

```SQL
source file_name
```

SQL Dumps:

```shell
 mysql -u root -p FLAPI > flapischema.sql
```

## API Endpoint

```html
http://127.0.0.1:5000/v1


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

Request : `POST http://127.0.0.1:5000/v1`

Response:

```json

200 OK - "Item has been added Succesfully"
```


# DELETE A PRODUCT

Request: `DELETE  http://127.0.0.1:5000/v1`

Response:

```json
200 OK - "Item has been succesfully deleted".
```

# Edit A PRODUCT

Request: `PUT http://127.0.0.1:5000/v1`

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


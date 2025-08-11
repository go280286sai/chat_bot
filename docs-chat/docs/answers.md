## name: **Create a new answers :param ans: :return:**
### url: /api/answers/create
### method: POST
### json
````
{
  "name": "string",
  "category_id": 0,
  "language_id": 0
}
````
## name: **Get a specific answers :param idx: :return:**
### url: /api/answers/get/{idx}
### method: GET
### params:
````
idx: int
````
## name: **Update a specific answers :param ans: :param idx: :return:**
### url: /api/answers/update/{idx}
### method: POST
### params:
````
idx: int
````
### json
````
{
  "name": "string",
  "category_id": 0,
  "language_id": 0
}
````
## name: **Get all answers :return:**
### url: /api/answers/
### method: GET
## name: **Delete a specific answers :param idx: :return:**
### url: /api/answers/delete/{idx}
### method: POST
### params:
````
idx: int
````
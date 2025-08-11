## name: **Create a new questions :param ques: :return:**
### url: /api/questions/create
### method: POST
### json
````
{
  "name": "string",
  "category_id": 0,
  "language_id": 0
}
````
## name: **Get a specific questions :param idx: :return:**
### url: /api/questions/get/{idx}
### method: GET
### params:
````
idx: int
````
## name: **Update a specific questions :param ques: :param idx: :return:**
### url: /api/questions/update/{idx}
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
## name: **Get all questions :return:**
### url: /api/questions/
### method: GET
## name: **Delete a specific questions :param idx: :return:**
### url: /api/questions/delete/{idx}
### method: POST
### params:
````
idx: int
````
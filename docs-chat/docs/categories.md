## name: **Create a new category :param cat: :return:**
### url: /api/categories/create
### method: POST
### json
````
{
  "name": "string"
}
````
## name: **Get a specific category :param idx: :return:**
### url: /api/categories/get/{idx}
### method: GET
### params:
````
idx: int
````
## name: **Update a specific category :param idx: :param cat: :return:**
### url: /api/categories/update/{idx}
### params:
````
idx: int
````
### method: POST
### json
````
{
  "name": "string"
}
````
## name: **Get a specific category :param idx: :return:**
### url: /api/categories/
### method: GET
## name: **Delete a specific category :param idx: :return:**
### url: /api/categories/delete/{idx}
### params:
````
idx: int
````
### method: POST

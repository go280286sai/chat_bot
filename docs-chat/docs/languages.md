## name: **Create a new language :param lang: :return:**
### url: /api/languages/create
### method: POST
### json
````
{
  "name": "string"
}
````
## name: **Get a specific language :param idx: :return:**
### url: /api/languages/get/{idx}
### params: 
````
idx: int
````
### method: GET
## **name: Update a specific language :param idx: :param lang: :return:**
### url: /api/languages/update/{idx}
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
## **name: Get a specific language :param idx: :return:**
### url: /api/languages/
### method: GET
## name: **Delete a new language :param idx: :return:**
### url: /api/languages/delete/{idx}
### params: 
````
idx: int
````
### method: POST
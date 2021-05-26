## Get News Categories
List all available news categories

- **URL**
  
    /api/categories

- **Method**
 
    GET

- **URL Params**

    N/A

- **Sample Response**:
  
    Code: 200

    Content: 
    ```json
    {
        "data": [
            {"category":"transportasi","id":1},
            {"category":"kesehatan","id":2},
            {"category":"ekonomi","id":3},
            {"category":"kebudayaan","id":4},
            {"category":"hukum","id":5},
            {"category":"pendidikan","id":6},
            {"category":"teknologi","id":7},
            {"category":"pariwisata","id":8},
            {"category":"politik","id":9},
            {"category":"keamanan","id":10},
            {"category":"bencana alam","id":11}
        ],
        "message":"OK",
        "status":"Get categories OK"
    }
    ```

## Get News
Get all news by category and date

- **URL**
  
    /api/news

- **Method**
 
    GET

- **URL Params**

    **Required:**

    `id_category=[integer]` : News' category ID

    `time=[integer]` : News from ... days ago

- **Sample Response**:
  
    Code: 200

    Content: 
    ```json
    {
        "data": [
            {
                "category":1,
                "content":"cekcekcek",
                "date":"Tue, 25 May 2021 17:00:00 GMT",
                "id":1,
                "image":"tes.png",
                "link":"https://news.detik.com/berita/d-5557626/gugatan-soal-adart-gugur-kubu-moeldoko-dinilai-cuma-pepesan-kosong",
                "portal":"detik.com",
                "sentiment":0,
                "tags":[],
                "title":"tes"}
        ],
        "message":"OK",
        "status":"Get news OK"
    }
    ```

## Get Overall News Sentiment
Get overall news sentiment for the past N days for a specific category/all categories.

- **URL**
  
    /api/overall

- **Method**
 
    GET

- **URL Params**

    **Required:**

    `time=[integer]` : News from ... days ago

    **Optional:**

    `id_category=[integer]` : News' category ID

- **Sample Response**:
  
    Code: 200

    Content: 
    ```json
    {
        "data": {
            "negative":1,
            "neutral":1,
            "positive":1
        },
        "message":"OK",
        "status":"Get overall OK"
    }
    ```

## Get News Chart Data
Get sentiment of news for each day starting from a specific date and a category/all categories.

- **URL**
  
    /api/overall/chart

- **Method**
 
    GET

- **URL Params**

    **Required:**

    `time=[integer]` : News from ... days ago

    **Optional:**

    `id_category=[integer]` : News' category ID

- **Sample Response**:
  
    Code: 200

    Content: 
    ```json
    {
        "data": [
            {
                "negative":1,
                "neutral":1,
                "positive":1
            },
        ],
        "message":"OK",
        "status":"Get chart OK"
    }
    ```

# news-api
Backend API for VizNews Mobile App

## Requirements
- Python 3
- Windows, macOS, or Linux are supported

## Getting Started
Clone the repo and run the following command in a terminal
```
pip install -r requirements.txt
```
Rename [`secret.py.example`](secret.py) to `secret.py` and set up the local database. Ensure the configuration in `secret.py` is correct.

## Running the Dev Server
You can directly run the application using the following command (Do not use it in a production environment).
```
python main.py
```
or if you prefer using a WSGI server, you can use gunicorn which offers `-reload` option or waitress
```
gunicorn main:app --reload
```
```
waitress-serve main:app
```

## Runing the App in Production
This project includes `app.yaml` which can be used to deploy the app to Google App Engine. Ensure that you already selected a GCP project via `gcloud config set project $PROJECT_ID$`. Then, simply just run the following command:
```
gcloud app deploy
```

## API Docs
Please refer to [API.MD](API.md)

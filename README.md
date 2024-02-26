# NeoTour-project
NeoTour is an optimized application designed for convenient tour booking. Offering a range of categories, including a comprehensive list of tours and popular options, NeoTour provides a convenient platform for travelers. Whether exploring destinations through captivating photos, delving into detailed tour descriptions, or managing bookings through the query backend, NeoTour is the path to hassle-free and unforgettable travel experiences.

### Technologies
---
- Python
- Django Rest Framework
- Swagger UI
- Nginx
- Docker

### Install
---
#### Without docker
1. Clone repository to your local machine:
```
git clone ssh/https-key
```
2. Create virtual environment and activate virtual environment:
- On `Windows`:
```
python -m env venv
```
```
venv\Scripts\activate.bat
```
- On `Linux/MacOs`
```
python3 -m env venv
```
```
source venv/bin/activate
```
3. Add `.env` file to the root and fill with your data next variables:
```
CLOUD_NAME = 
API_KEY = 
API_SECRET = 
SECRET_KEY =
DJANGO_DEBUG = 1
```
4. Install all dependecies:
```
pip install -r requirements.txt
```
5. Run the project on your local host:
```
python/python3 manage.py runserver
```
### Authors
---
[Nursultan Kozhogulov, 2024](https://github.com/Nursultank00)
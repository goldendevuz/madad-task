30.10.2024 - Project has major problems. It is upgraded Step by step. Be patient, thank you!

# Aiogram 3 + django 5 + webhook app

### 1. Create a Virtual Environment: Create a virtual environment in your project directory:
   ```python3 -m venv myenv```
### 2. Activate environment
   ```source venv/bin/activate```
### 3. Install all required packages
   ```pip install -r requirements.txt```
### 4. Create migration files based on changes made to Django models and to apply the changes to the database
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
### 5. To create an admin user in Django
   ```python3 manage.py createsuperuser```
### 6. To gather all static files from your project and its apps into a single directory
   ```python3 manage.py collectstatic```
### 7. To create a public URL for your local web server, allowing external access to it over the internet.
   ```ngrok http 8000```
### 8. Create .env file and configure environment variables as like .env.example
### 9. Set webhook to your bot
   ```python3 manage.py setwebhook```
### 10. Run an ASGI (Asynchronous Server Gateway Interface) application with Uvicorn
   ```uvicorn core.asgi:application --host 0.0.0.0 --port 8000```


## If you have questions for this project, join and ask to me: 
https://t.me/pipcoder

<p align="center">
<img style="width: 60%;" src="https://i.postimg.cc/nzykWKNd/result.gif">
</p>
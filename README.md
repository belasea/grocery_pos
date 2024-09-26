<!-- ![ecommerce](https://github.com/jibon969/eCommerce/assets/21084550/477f146e-e1a5-4293-a365-15bcbc12a3dd) -->
<img
src='static/img/eCommerce.jpg'
alt='Jayed Hossain Jibon'
/>
<h1 align="center" id='header'>POS System Web Application</h1>
<div align="center">
<!-- Gmail Account -->
<a href="mailto:jayed.swe@gmail.com">
<img src='https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
<a href="tel:+8801987132107">
<img
src='https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white'
alt='Jayed Hossain Jibon'
/>
<a href="#" target="_blank">
<img
src='https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
<a href="https://www.facebook.com/jibon969" target="_blank">
<img
src='https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white'
alt='Jayed Hossain Jibon'
/>

<a href="https://www.linkedin.com/in/jibon969/" target="_blank">
<img
src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
<a href="https://github.com/jibon969" target="_blank">
<img
src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
</div>

<hr/>


#### 01. How to create new project or run existing project

```
How to create new project or run existing project
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
pip install django

django-admin startproject pos_system
cd pos_system

python manage.py startapp sales 


python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows


# OR  Clone project
git clone git@github.com:belasea/pos_system.git


# Step 3 : Install Packages
pip install -r requirements.txt

# Step 4 : Run this project
python manage.py runserver

# Step 5 : makemigrations
python manage.py makemigrations products sales
```
</details>

#### 02. Delete __pycache__', 'migrations' Root directory of your Django project

```
Delete __pycache__', 'migrations'
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
import os
import shutil

# Root directory of your Django project
project_root = '/Users/j.ahmed/coding/webs/eCommerce/eCommerce'

# List of directories to delete
directories_to_delete = ['__pycache__', 'migrations']

def delete_directories(root, directories):
    for dirpath, dirnames, filenames in os.walk(root):
        for dirname in dirnames:
            if dirname in directories:
                dir_to_delete = os.path.join(dirpath, dirname)
                print(f"Deleting directory: {dir_to_delete}")
                shutil.rmtree(dir_to_delete)

if __name__ == "__main__":
    delete_directories(project_root, directories_to_delete)
    print("Deletion completed.")
```
</details>
  

  
#### 03. Django PostgreSQL

```
Django PostgreSQL
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
# create database local_db
postgres=# create database local_db;
CREATE DATABASE
postgres=# \l

# Connect DB
postgres=# \c local_db;
You are now connected to database "local_db" as user "postgres".
# Show relations
local_db=# \d

# Django Settings.py 
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'local_db',
       'USER': 'postgres',
       'PASSWORD': 'root',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}
```
</details>




#### 04.Django Programming error column does not exist even after running migrations

```
Migrations issues
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
python manage.py migrate app_name zero  # Rollback all migrations
python manage.py migrate                # Apply migrations again
```
</details>

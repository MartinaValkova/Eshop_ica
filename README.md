# Eshop_ica
E-shop web application project

Project's Title:

E-Shop

Project Description:

Fully functional E-shop website. Right form listing products, searching them, adding them to the cart, and checkout we implement each and every feature from scratch.

The website was deployed, to see it go to: https://eshop-uz89.onrender.com/

Or you can run the Django development server by following the steps bellow.


Requirements:

Python 3.9 Django 4.1.7

How to Install and Run the Project:

The first thing to do is to clone the repository

$ git clone https://github.com/MartinaValkova/Eshop_ica.git $ cd Eshop_ica

Create a virtual environment to install dependencies in and activate it:

On Mac:

$ python -m venv venv $ source venv/bin/activate 


On Windows:

$ python -m venv venv $ .\venv\Scripts\activate  


Then intall django:

$pip install django


Then install the dependencies:

(env)$ cd Eshop

(env)$ pip install -r requirements.txt Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Every Django project has a unique secret key. The secret is not exposed online. Ask for the secret key.

Make your migrations if some: $ python manage.py makemigrations $ python manage.py migrate


Once pip has finished downloading the dependencies:

(env)$ cd Eshop_ica

(env)$ python manage.py runserver And navigate to http://127.0.0.1:8000/?page=1

License

Copyright © 2022 Martina V., Jovan B., Jeremy J., Alibay B.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

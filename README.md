# Eshop_ica
E-shop web application project


Project's Title:

E-Shop


Project Description:

Fully functional E-shop website. Right form listing products, searching them, adding them to the cart, and checkout we implement each and every feature from scratch.


Requirements:

Python 3.9
Django 4.1.7


How to Install and Run the Project:

The first thing to do is to clone the repository

$ git clone https://github.com/MartinaValkova/Eshop_ica.git
$ cd Eshop
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/ 

In order to test the purchase flows, fill in the account details in project/gc_app/views.py to match your SANDBOX developer credentials.



License

Copyright © 2022 Martina V., Jovan B., Jeremy J., Alibay B.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

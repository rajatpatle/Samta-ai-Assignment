# Samta-ai-Assignment
----------------------
DRF Project --> Authentication, Admin , Management user, API Design, Testing
---------------------------
Steps To Run The Project
---------------------------
1.virtualenv venv
2.venv\scripts\activate
3.cd project1
4.py manage.py runserver

API TESTING LINK
------------------------------------------------------------------------------------------------------------------------------------------
1. http://127.0.0.1:8000/first/data/        ----> Admin can register User 
2. http://127.0.0.1:8000/token/             -----> Management user can login (token is generated)---> Can retrive all data from database
3. http://127.0.0.1:8000/first/eastdata/    ------> Perticular region data retrival
4. http://127.0.0.1:8000/first/per/         --------> Per salesperson per manager retrival
------------------------------------------------------------------------------------------------------------------------------------------

Methods used
--------------
1.Generics
2.User Model for registration.
3.Validations
4.Token Authentication
5.Per view Authentication
6.Pandas library to read csv file
7.To encrypt Password implemented CREAT Method in serializers
8.Admin can add csv file and management user can view data
9.Used django ORM to retrive data from database

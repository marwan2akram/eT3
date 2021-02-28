# eT3
A web application for Employees to submit requests for leave and for managers to approve the requests.

# Requirements

* Python (3.5, 3.6, 3.7, 3.8, 3.9)
* Django (2.2, 3.0, 3.1)

it's **highly recommend** and only officially support the latest patch release of
each Python and Django series.

# Creating Migrations


	* python manage.py makemigrations 
   
	* python manage.py migrate

# Run Server


	* python manage.py runserver

# create superuser


	* python manage.py createsuperuser

# Testing
To run the tests, run


	* python manage.py test leaverequests

#URL home page 
* /leaverequests/

#URL signup page 
* /accounts/signup/

#url login 
* /accounts/login/

#url create profile
* /leaverequests/create-profile

#url create leave request
* /leaverequests/create-request

#url view my leave requests 
* /leaverequests/history-log

#url manager can view all the leave requests
* /leaverequests/create-profile

# url manager can accept the leave request
* /<int:id>/approve-request

# url manager can reject the leave request
* /<int:id>/reject-request

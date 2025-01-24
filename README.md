# e-commerce
An e-commerce backend is a backend system that to buy products over the internet. It provide a secure purchase porcess with safety payment

## Table of Contents
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
### [Design](#design-1)
* [Data Model](#data-models)
* [Database Scheme](#database-scheme)
### [Deployment and Local developement](#deployment-and-local-developement-1)
* [Local Developement](#local-developement)
* [Postgress Database](#postgress-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)

### [Testing](#testing-1)
### [References](#references-1)
* [Docs](#docs)
* [Content](#content)
* [Acknowledgments](#acknowledgments)

## Technologies Used

### Languages Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used

* [Postgress](https://www.elephantsql.com/) - Postgres database
* [Cloudinary](https://cloudinary.com/) - Online static file storage

### Frameworks Used

* [Django](https://www.djangoproject.com/) - Python framework

### Programs Used

* [Github](https://github.com/) - Storing the code online
* [Code Institute IDE](https://codeinstitute-ide.net/workspaces) - To create work space and write code
* [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
* [Git](https://git-scm.com/) - Version control
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python

### Data Models

1. AllAuth User Model
    * Django Allauth, the User model is the default user model provided by the Django authentication system
    * The User entity has a one-to-one relationship with the Profile entity. This means every User has a profile
2. Profile Model
    * Has additional information about the customer in addition to one-to-one relationship with the AllAuth User Model 
    * created_at - updated_at - name - image - street - street_number - zipcode - city - state -country - email
3. Product Model
    * It describes the product and has many-to-one relationship with the category. 
    * The fields are: name - category - created_at - updated_at - image - price - description - color - size - color

4. Category Model
    * It describes the category and has one-to-many relationship with the product
    * The fields are: id - name

4. Order Model
    * It describes the order and has many-to-one relationship with the user
    * The fields are: created_at - total_price - customer - delivery_place  

5. Order_Product Model
    * Its many-to-many relationship between the order and the product
    * The fields are: product - order - count - price - total_price  
---

### Database Scheme
[Database Scheme](documentation/Entity%20Diagram/E-commerce.png)


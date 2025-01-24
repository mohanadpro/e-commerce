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

## Deployment and Local Developement

Live deployment can be found on this [EBuy](https://ebuy-17fcffc62fb3.herokuapp.com/)

### Local Developement

#### How to Fork
1. Log in(or Sign Up) to Github
2. Go to repository for this project [E-Commerce Backend](https://github.com/mohanadpro/e-commerce)
3. Click the fork button in the top right corner

#### How to Clone
1. Log in(or Sign Up) to Github
2. Go to repository for this project [E-Commerce](https://github.com/mohanadpro/e-commerce)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt
8. To run the app type python3 manage.py runserver


### Postgress Database
* The storage of the database is provided from the Code institut

### Cloudinary
The website is using [Cloudinary](https://cloudinary.com/)
1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.

### Deploy to Heroku 
    1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com/).
    2. Create a new Heroku application on the following page here New [Heroku App](https://dashboard.heroku.com/apps)
    3. Go to the Deploy tab
    4. Link your GitHub account and connect the application to the repository you created.
    5. Go to the Settings tab
    6. Click "Add buildpack"
    7. Add the Python buildpacks in the following order
    8. Click Reveal Config Vars
    9. Add Config Vars
    10. Click Deploy Branch
    11. Click View to launch the application inside a web page.

## References
### Docs

* [Stack Overflow](https://stackoverflow.com/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Django docs](https://docs.djangoproject.com/en/4.2/releases/3.2/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Cloudinary](https://cloudinary.com/documentation/diagnosing_error_codes_tutorial)
* [Google](https://www.google.com/)

### Acknowledgments

* I would like to thank my mentor for support and feedback throughout this project, Mitko Bachvarov.
* I would also like to extend my appreciation to code institue tutors for their helping
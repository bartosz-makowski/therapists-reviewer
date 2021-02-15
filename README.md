# Therapists Reviewer :open_file_folder:
![Multiple screen view](https://github.com/bartosz-makowski/therapists-reviewer/blob/master/wireframes/multiple-screens-view.png)
Project of the web application designed to promote health therapists based in the area of Hertfordshire UK. User of the website is able to search for therapists see their reviews and after creating an account also to write reviews for therapists.

## Contents:book:
### UX:superhero_man:	
  * **Project Goals** :jigsaw:	
  * **Target Audience Goals** 	:dart:
  * **Site Owner Goals**  	:dart:
  * **User Requirements and Expectations** 	:dart:
  * **Design Choices** :framed_picture:
    * Fonts
    * Icons
    * Colours
  * **Wireframes** :straight_ruler:
  * **Database Structure** :straight_ruler:
  * **Features** :abacus:	
    * Features that have been developed
    * Features that will be implemented in the future
  * **Technologies Used** :computer:	
    * Languages
    * Tools & Libraries
  * **Testing** :magnet:
  * **Bugs** :mosquito:
  * **Deployment** :surfer:
  * **Acknowledgements** :clap:
  
## UX ( User Experience)
### Project Goals :jigsaw:	
The goal of this project is to provide the users with a website where they can see or leave a review for a health practitioner based in the area of Hertfordshire UK

### User Goals :jigsaw: 
* Ability to set up an account
* Ability to log in and log out
* Ability to see my previous reviews
* ability to search for therapist by location 
* Visual interaction and feedback
* Interact with the website on Desktop tablet and mobile

## User stories 	:dart:
1. As a user I expect to **setup an account to be able to leave reviews**
2. As a user I expect to **be able to log in and out of my account**
3. As a user I want to be able to **search practitioners by location or therapies**
4. As a user I want to be able to **see reviews of different therapists**
5. As a user I want to be able to **see profiles of the therapists**
6. As a user I expect to **be able to create, read, update and delete my reviews**

## Site Owner Goals	:dart:

* Collect data about local therapists
* Promote therapists in the local area

## User Requirements and Expectations 	:dart:

* **Requirements**
  * Navigate the website using the menu buttons and drop down selector
  * Ability to use this application on mobile and desktop devices
  * Content displayed in a visually appealing manor
  
* **Expectations**
  * Content is visually satisfying and informative on all screen sizes
  * No information overload
  * Navigation takes user to specific parts of the website
  
## Design choices :framed_picture:	
  
**Fonts**

I chose to use the font **Lato** as it was designed with a neutral, yet friendly appearance which compliments the general attitude of this project's design and it's desired function. it can be found [here](https://fonts.google.com/specimen/Lato?sidebar.open=true&selection.family=Lato&preview.text_type=custom#standard-styles).The semi-rounded details of the letters give **Lato** a feeling of warmth, while the strong structure provides stability and seriousness. “Male and female, serious but friendly. With the feeling of the Summer,” says Łukasz.

**Icons**

Icons used in this project come from [FontAwesome](https://fontawesome.com/). They represent widely known social network websites and are located in the footer.

**Colours**

Using learned knowledge from prior research, bright and vibrant colours have a higher influence in terms of positivity and therefore more potential interactions. [Link to the colour palette](https://coolors.co/072ac8-1e96fc-c80707-f0c14b-fafafa). Screenshot of the colour palette has been added to the wireframes [folder](https://github.com/bartosz-makowski/therapists-reviewer/blob/master/wireframes/therapists-reviewer-palette.png).

**Colours used**
![color theme](https://github.com/bartosz-makowski/therapists-reviewer/blob/master/wireframes/therapists-reviewer-palette.png)


## Wireframes :straight_ruler:
I built the wireframes for this project using <a href="https://balsamiq.com/">Balsamiq</a>. Started by doing a very basic wireframe for Mobile/Tablet/Desktop - these were to get a basic understanding of how structurally elements would appear on the page. You can view those in a wireframes [folder](https://github.com/bartosz-makowski/therapists-reviewer/tree/master/wireframes).

## **Database Structure**

I have used MongoDB to set up the database for this project with the following collections: 

#### **Users:**

Key      | Value
---------|-----------
_id      | ObjectId
username | String
password | String

#### **Therapists:**

Key             | Value
----------------|-----------
_id             | ObjectId
therapist_id    | String
first_name      | String
second_name     | String
email           | String
webpage         | String
main_therapy    | String
other_therapies | String
location        | String
bio             | String

#### **Reviews:**

Key                | Value
-------------------|-----------
_id                | ObjectId
user               | String
title              | String
email              | String
review_description | String
therapist_id       | String

## Features :abacus:

**Features that have been developed:**
* Registration of a new user
* Log in / Log out function
* Password and username validation
* CRUD functionality for the reviews
* Visible feedback when hover over buttons, links and icons
* Buttons `<a>` tags form input areas and cards styled using [neumorphism](https://css-tricks.com/neumorphism-and-css/) style

**Features to be implemented in the future**
* Validation of review form to prevent from using only white spaces in the review description and review title input
* Add a confirmation message after pressing `delete review button`
* Have `forget my password` functionality
* Login for therapists with an option to modify their details in the database
* Add pagination so the list of reviews will be displayed with a max of 20 logs per page.

## Technologies Used :computer:

### Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.w3schools.com/js/)
* [Python](https://www.python.org/)

### Tools & Libraries
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [MongoDB](https://www.mongodb.com/)
* [PyMongo](https://docs.mongodb.com/drivers/pymongo/)
* [Jinja](https://palletsprojects.com/p/jinja/)
* [PopperJS](https://popper.js.org/)
* [jQuery](https://jquery.com/)
* [Git](https://git-scm.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [FontAwesome](https://fontawesome.com/)
* [Balsamiq](https://balsamiq.com/)
* [AmIresponsive](http://ami.responsivedesign.is/) - used to generate multi screen view of the webiste on different devices


### Testing :magnet:

#### User story : As a user I want to be able to **setup an account to be able to leave reviews** :key:

##### Plan:

I want to create a page where a user can register for their personal account that is accessibale only by this user. After a succesful registration a message confirmation would appear and user would be redirected to their blank myaccount page.

##### Implementation:

I created a form where the user can choose a username and a password. I have used the pattern attribute to only allow certain characters and length for the username and password. Correct feedback will be displayed whenever the user doesn't meet the pattern critera. Before creating the new account, I will check in the database if the username already exists. If so, correct feedback will be displayed to the user. Password will be stored with the help of the password generate hash so it is stored safely. After the registration was succesfull, the user will be redirected to the blank myaccount page. In case the user wrongfully clicked on register instead of sign-in, a link to the sign-in page is provided so the user doesn't have to go back. I have also implemented a 'Go back to the homepage' link in the navbar so the user doesn't have to use the back button of the browser in case they decide to go back to the homepage.

I have used a variable (register) to make the difference between the register and sign-in form. When register is equal to True, I added labels explains the requested username and password characters and their length. By implementing this, I have managed to merge theauthentication form into 1 form which simplifies my templates.

##### Test:

I have tried to create an account with an already existing username. Correct feedback is displayed. Whenever I didn't meet the pattern criteria, the correct feedback was displayed, explaining which charachters etc are allowed. User acccount is created whenever all criteria was met and user is being redirect to blank dashboard.

##### Result:

Registration form is working as planned and user information is stored safely in the mongodb Users collection. Feedback provided stands out nicely to inform the user. Redirection to blank dashboard works as planned.

#### User story : As a user I expect to **be able to log in and out of my account** :door:

* **Plan**  
My plan is to create a login form where the user can fill in its username and password.
After signing in, the user will be redirected to the my account page where the user can see the previously writen reviews also a welcome message will be shown to the user.
A menu option to log out will become available to the user.

* **Implementation**  
I created a form where the user can fill in its username and password which will be verified with the information stored in the database. 
When the wrong information is being filled in, the correct feedback will be provided to the user. 
In case the user wrongfully clicked on sign-in instead of register, a link to the register page is provided so the user doesn't have to go back. 

* **Test**  
Signing in with the correct username and password works as planned and the user will be redirected to correct page. 
When the user fills in the wrong username and/or password, the correct message is being displayed on the screen.  
Redirecting to register page  link works correctly.
After pressing log out menu option session cookies are cleared and menu options available to logged users become unavailable.

* **Result**  
Application works as planned

#### User story :  As a user I expect to **be able to create, read, update and delete my reviews** :+1:

##### Plan:

I want the users to be able to leave reviews for therapists available on the website. For great user experience all crud operations are neccessary.

##### Implementation:

After a user logged in to his profile they gain access to write a review page. I created a form where the user can choose a therapist as well as add their email address for contact, however this is not required. There is an input area to add a review title and the review description.

After accessing my account page, user is able to see all their reviews and decide if wants to remove or update them. I have used same review form as for writing a review, however by using a variable (update)  I was able to select to populate input areas with information from the review. After finishing user has option to update the review or cancel changes. If dcides to press cancel button they will e redirected to my account page

When user is on my account page they will have a **red** cancel button that allows them to remove the review from the database. After pressing it the review will be removed from the MongoDb collection of reviews.

##### Test:

I have tried to write a new review, this uncovered a bug allowing to use a spacebar to leave an empty review. This issue couldn't be fixed with the **pattern** attribute. I will need to research this issue and improve it in the next release of this application. 
I was able to see all my reviews when accessed my account page.
I have tried to update one of the reviews, no problems were detected.
I tried to delete one of the reviews, this test uncovered a need for a confirmation alert to avoid accidental removal of the review from database.

##### Result:

All crude operations are working correctly, however a few modifcations are needed

#### User story :  **As a user I expect to **be able to see profiles of the therapists and their reviews** :eyes:

##### Plan:

I want the users to be able to see reviews of therapists available on the website to promote them.

##### Implementation:

I want to create an app allowing users to see reviews of the local therapists in the area of Hertfordshire UK. In order to do that all userws of the website should be able to see therapists profiles and their reviews. This part of the application is accessible for all visitors of the website.

##### Test:

I tried to access this application from different devices and was always able to see expected information about the therapists.

##### Result:

Application works as planned

#### User story : As a user I expect to **search practitioners by location or therapies** :mag:

##### Plan:

I want the users to be able to search for therapists based on their location or therapy that they practice.

##### Implementation:

I want the users of this project to be able to use a search bar located at home page to look for therapists within a database based on their location and therapies that they do.
After searching user should be able to see available therapists and if there are none an apropriate message should be displayed for the user.

##### Test:

I tried to use different search queries in the search bar. When no results are available the user can see a message saying that no available therapists has been found using this criteria. If successful the user will see all available therapists with the selected criteria.

##### Result:

Application works as planned


### Bugs :mosquito:
#### New user registration form issue :spider:
* **Issue:** Form allowing registration for username and password using white spaces
* **Fix:** Adding  attributes `pattern="^[A-Za-z0-9]{5,15}$"` and `required` to username and password input fix this issue

#### Google dev tools - empty div in the head issue at home page :ant:
* **Issue:** When checked the home page with google dev tools there was an empty div pushed into the head element.
* **Fix:** Empty div was `{% include 'components/flash_messages/flash-messages.html' %}`, moving it in to `{% block content %}` fixed this issue 

### Deployment :surfer:

#### To deploy Therapists reviewer locally

I have created this project using Github, from there I used [Gitpod](https://gitpod.io/) to write my code. 
Then I used commits to git followed by "git push" to my GitHub repository. 
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku. 

This project can be ran locally by following the following steps: (
I used Gitpod for development, so the following steps will be specific to Gitpod. 
You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/bartosz-makowski/therapists-reviewer.git
    ``` 

1. Access the folder in your terminal window and install the application's [required modules](https://github.com/bartosz-makowski/therapists-reviewer/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. Sign-in or sign-up to [MongoDB](https://www.mongodb.com/) and create a new cluster
    * Within the Sandbox, click the collections button and after click Create Database called therapists-reviewer
    * Set up the following collections: users, therapists, reviews, exact data structure can be found in the readme.md
    * Under the Security Menu on the left, select Database Access.
    * Add a new database user, and keep the credentials secure
    * Within the Network Access option, add IP Address 0.0.0.0

1. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ["IP"] = "0.0.0.0"
    os.environ["PORT"] = "5000"
    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"
    os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
    os.environ["MONGO_DBNAME"]= "DATABASE_NAME" 
    ```

    Please note that you will need to update the **SECRET_KEY** with your own secret key, as well as the **MONGO_URI** and **MONGO_DBNAME** variables with those provided by [MongoDB](https://www.mongodb.com/)
    To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. 
    Don't forget to update the necessary fields like password and database name. 

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

1. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 app.py. 
    ```

#### To deploy your project on Heroku, use the following steps: 

1. Login to your Heroku account and create a new app. Choose your region. 
1. Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.  
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: python app.py
    ```

1. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
1. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME):
    !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website. 

    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = YOUR_SECRET_KEY
    MONGO_URI = YOUR_MONGODB_URI
    MONGO_DBNAME = DATABASE_NAME
    ```

1. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 
    
#### Running Therapist Reviewer Locally

### Acknowledgements :clap:
* My The Greatest Of All Time (GOAT) mentor [Eventyret](https://github.com/Eventyret) for his great help, support and ideas.
* [StackOverflow](https://stackoverflow.com/) community for fantastic resource when in need.
* [Unsplash](https://unsplash.com/) community for access to free high quality images.

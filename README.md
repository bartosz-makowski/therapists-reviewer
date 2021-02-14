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
* **1** As a user I expect to **see reviews of different therapists**
* **2** As a user I want to be able to **search practitioners by location or therapies**
* **3** As a user I want to be able to **setup an account to be able to leave reviews**
* **4** As a user I want to be able to **see profiles of the therapists**
* **5** As a user I expect to **be able to create, read, update and delete my reviews**

## Site Owner Goals	:dart:

* Collect data about local therapists
* Promote therapists in the local area

## User Requirements and Expectations 	:dart:

* **Requirements**
  * Navigate the website using the menu buttons and drop down selector
  * Ability to use this application on mobile and desktop devices
  * Contnent displayed in a visually appealing manor
  
* **Expectations**
  * Content is visually satisfying and informative on all screen sizes
  * No information overload
  * Navigation takes user to specific parts of the website
  
## Design choices :framed_picture:	
  
**Fonts**

I chose to use the font **Lato** as it was designed with a neutral, yet friendly appearance which compliments the general attitude of this project's design and it's desired function. it can be found [here](https://fonts.google.com/specimen/Lato?sidebar.open=true&selection.family=Lato&preview.text_type=custom#standard-styles).The semi-rounded details of the letters give **Lato** a feeling of warmth, while the strong structure provides stability and seriousness. “Male and female, serious but friendly. With the feeling of the Summer,” says Łukasz.

**Colours**

Using learned knowledge from prior research, bright and vibrant colours have a higher influence in terms of positivity and therefore more potential interactions. [Link to the colour palette](https://coolors.co/072ac8-1e96fc-c80707-f0c14b-fafafa). Screenshot of the colour palette has been added to the wireframes [folder](https://github.com/bartosz-makowski/therapists-reviewer/blob/master/wireframes/therapists-reviewer-palette.png).

**Colours used**
![color theme](https://github.com/bartosz-makowski/therapists-reviewer/blob/master/wireframes/therapists-reviewer-palette.png)


## Wireframes :straight_ruler:
I built the wireframes for this project using <a href="https://balsamiq.com/">Balsamiq</a>. Started by doing a very basic wireframe for Mobile/Tablet/Desktop - these were to get a basic understanding of how structurally elements would appear on the page. You can view those in a wireframes [folder](https://github.com/bartosz-makowski/therapists-reviewer/tree/master/wireframes).
![color theme]()

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
* Buttons and `<a>` tags styled using [neumorphism](https://css-tricks.com/neumorphism-and-css/) style

**Features to be implemented in the future**


## Technologies Used :computer:

### Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.w3schools.com/js/)
* [Python](https://www.python.org/)

### Tools & Libraries
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [MongoDB](https://www.mongodb.com/)
* [PopperJS](https://popper.js.org/)
* [jQuery](https://jquery.com/)
* [Git](https://git-scm.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [Balsamiq](https://balsamiq.com/)
* [AmIresponsive](http://ami.responsivedesign.is/) - used to generate multi screen view of the webiste on different devices


### Testing :magnet:

#### User story : As a user I want to be able to **setup an account to be able to leave reviews**

##### Plan:

I want to create a page where a user can register for their personal account that is accessibale only by this user. After a succesful registration a message confirmation would appear and user would be redirected to their blank myaccount page.

##### Implementation:

I created a form where the user can choose a username and a password. I have used the pattern attribute to only allow certain characters and length for the username and password. Correct feedback will be displayed whenever the user doesn't meet the pattern critera. Before creating the new account, I will check in the database if the username already exists. If so, correct feedback will be displayed to the user. Password will be stored with the help of the password generate hash so it is stored safely. After the registration was succesfull, the user will be redirected to the blank myaccount page. In case the user wrongfully clicked on register instead of sign-in, a link to the sign-in page is provided so the user doesn't have to go back. I have also implemented a 'Go back to the homepage' link in the navbar so the user doesn't have to use the back button of the browser in case they decide to go back to the homepage.

I have used a variable (register) to make the difference between the register and sign-in form. When register is equal to True, I added labels explains the requested username and password characters and their length. By implementing this, I have managed to merge theauthentication form into 1 form which simplifies my templates.

##### Test:

I have tried to create an account with an already existing username. Correct feedback is displayed. Whenever I didn't meet the pattern criteria, the correct feedback was displayed, explaining which charachters etc are allowed. User acccount is created whenever all criteria was met and user is being redirect to blank dashboard.

##### Result:

Registration form is working as planned and user information is stored safely in the mongodb Users collection. Feedback provided stands out nicely to inform the user. Redirection to blank dashboard works as planned.


#### User story :  As a user I expect to **be able to create, read, update and delete my reviews**

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

#### User story :  As a user I expect to **be able to see profiles of the therapists and their reviews**

##### Plan:

I want the users to be able to see reviews of therapists available on the website to promote them.

##### Implementation:

I want to create an app allowing users to see reviews of the local therapists in the area of Hertfordshire UK. In order to do that all userws of the website should be able to see therapists profiles and their reviews. This part of the application is accessible for all visitors of the website.

##### Test:

I tried to access this application from different devices and was always able to see expected information about the therapists.

##### Result:

Application works as planned


#### Tests
##### Using W3C Markup Validator
###### Test 1 :writing_hand:
* **Error:** 
* **Solution:** 
###### Test 2 :mag_right:
* **Warning:**  
* **Solution:** 
###### Test 3 :chart_with_upwards_trend:
* **Error:** 
* **Solution** 

### Bugs :mosquito:
#### New user registration form issue :spider:
* **Issue:** Form allowing registration for username and password using white spaces
* **Fix:** Adding  attributes `pattern="^[A-Za-z0-9]{5,15}$"` and `required` to username and password input fix this issue

####  :ant:
* **Issue:** 
* **Fix:** 

### Deployment :surfer:

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
* [Unsplash](https://unsplash.com/) community for access to free high quality images.

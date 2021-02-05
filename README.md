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
* As a user I expect to **see reviews of different therapists**
* As a user I want to be able to **search practitioners by location or therapies**
* As a user I want to be able to **setup an account to be able to leave reviews**
* As a user I want to be able to **see profiles of the therapists**
* As a user I expect to **be able to say if I recommend the therapist**

## Site Owner Goals	:dart:

* Collect data about local therapists
* Promote therapists in the local area
* Promote a range of exercise, massage tools and make a profit using affiliate links to those products at [Amazon](https://www.amazon.co.uk/)

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
therapist_bio   | String

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

#### Plan


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
##### Manual testing
###### Test1 :magnet:
* **Error:** 
* **Solution** 
###### Test 2 :chart_with_downwards_trend:
* **Error:** 
* **Solution**  
### Bugs :mosquito:
####  :spider:
* **Issue:** 
* **Fix:** 
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

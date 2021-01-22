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
    * Sounds
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


**Colours**


**Colours used**

**Sounds**

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
first_name      | String
second_name     | String
email           | String
webpage         | String
main_therapy    | String
other_therapies | String
location        | String
reviews         | Array

#### **Reviews:**

Key                | Value
-------------------|-----------
_id                | ObjectId
user               | String
title              | String
rating             | String
review_description | String
would_recommend    | String


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

#### Running Therapist Reviewer Locally

### Acknowledgements :clap:

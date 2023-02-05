## CAREHUB
The website is aimed at people require care services, and carers who may be searching for the information for them.
The app provides a list of Care Providers, their services information and contact details. Registered users are able to rate their services, and also leave comments on the service they received.
The design is aimed to be simple and easy to navigate. Accessiblity was a major factor in the site design. 

Link to the site here https://carehub-caresearch2023.herokuapp.com/

## Am I Responsive mockups
![Responsive Mockup](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/docs/readmeimages/amiresponsive.jpg)

## Contents
* [Design and User Experience](#Design-and-User-Experience)
* [Features](#Features)
* [Technologies Used](#Technologies-Used)
* [Agile Methodology](#Agile)
* [Fixed and Unfixed Bugs](#Fixed-and-Unfixed-Bugs)
* [Validation](#Validation)
* [Testing](#Testing)
* [Project Creation and Deployment](#Project-Creation-and-Deployment)
* [Credits](#Credits)

## Design and User Experience
The site was aimed at the elderly, and their carers, so they can find information about care providers quickly and easily.

Initially a flow chart was created to work out how the user navigates the site. It shows where the user should input data, how to validate that data, and what happens for a correct or incorrect entry.  
![Flowchart](https://github.com/RozWelch/ ADD FLOW CHART HERE)

* Accessibility:
    * To ensure maximum user accessibility, the contrast between the background colour and text was kept to a high contrast.
    * Font size was kept large to ensure high legibility
    * Atkinson Hyperlegible is used as the main text font, as it is recommended as being highly legible.
    * The overall design was kept simple and easy to follow. Call-to-action buttons were made easy to view and locate on the page.

* Colour pallet:
    * The main colours choosen gave the site a medical feel, with warm accent colours to give an approchable feel.  
    ![Colour Pallett](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/docs/readmeimages/colour_scheme.jpg)

* Wireframes:
    <details>
    <summary>Home Page Wireframe</summary>
    <br>
    This is how you dropdown.
    </details>


* User Stories:
* Epic: First Time User - Site design and navigation
    * As a First time User, I can view information on the Home Page so that I can clearly see the purpose of the site and how to use it
    * As a First Time User, I can easily understand the main purpose of the app, so that I can find the infomation I require easily
    * As a First Time User, I can navigate the site so that I can navigate to the information I require in an effective and intuitive fashion
    * As a First Time User,  I can view care providers, so that I can browse a list of care providers
    * As a First Time User,  I can view care providers full profile, so that I can see all of their details and ratings 
 
* Epic: Frequent User - account functions
    * As a Frequent User, I can create a new account so that I can access all functions provided by the app
    * As a Frequent User,  I can login and logout, so that I can access my details 
    * As a Frequent User, I can see my login status so that I can know if I am logged in or out
    * As a Frequent User,  I can view care providers by area or by service provided, so that I can see care providers that suit my needs 
    * As a Frequent User,  I can update my account details, so that I can manage my account content
    * As a Frequent User,  I can delete my account details, so that I can manage my account 
    * As a Frequent User,  I can login and rate and comment on a care provider, so that I can review and give my feedback on their service
    * As a Frequent User,  I can update or delete my ratings and comment on a care provider, so that I can update my reviews

* Epic: Care Provider Account
    * As a care provider,  I can create an account, so that I can add my details 
    * As a care provider,  I can login and logout, so that I can access my details
    * As a care provider,  I can see my login status so that I can know if I am logged in or out 
    * As a care provider,  I can update my account details, so that I can manage my account content
    * As a care provider,  I can delete my account details, so that I can manage my account 

* Epic: Site Admin
    * As a Site Admin,  I can approve care provider’s accounts, so that I can check they are authentic care providers
    * As a Site Admin,  I can update or delete a care provider’s accounts, so that I can manage my care providers content
    * As a Site Admin,  I can approve comments, so that I can filter out objectionable comments
    * As a Site Admin, I can update comments, so that I can manage my care providers content
    * As a Site Admin, I can delete comments, so that I can manage my care providers content

* Epic: Future Features
    * As a Frequent User,  I can login to make an appointment, so that I can make an appointment with a care provider
    * As a Frequent User,  I can create an account using my google or facebook account, so that I can sign up quickly



## Features

* Home Page:
    * ADD TEXT HERE
    * UX: as a first time user I want to ADD TEXT HERE

![Mainscreen](https://github.com/RozWelch/ADD TEXT HERE)
    
* The user is asked to select a difficulty level
    * UX: as a first time or returning user, I want to easily select a difficulty level

![Navigation Bar](https://github.com/RozWelch/ADD TEXT HERE

    * UX: as a first time or returning user, I want to ADD TEXT HERE


* Future Features: 
    * Make an appointment, so that a logged in user can make an appointment with a care provider
    * Create an account using a google or facebook account, so that a user can sign up quickly
s
## Technologies Used
* Languages: Python, HTML, CSS, Javascript
* Libraries:  
    * Django: Main python framework 
    * Django-allauth: authentication library used to create user accounts
    * Elephant PostgreSQL: database
    * Heroku: cloud based platform to deploy the site
    * Balsamiq: to draw wireframes
    * Chrome Dev Tools - for testing responsiveness, performance and for debugging
    * Font Awesome: icons on home page
    * GitHub: version control and agile Kanban boards
    * Google Fonts: fonts used on site
    * Favicon: to create a favicon for the site
    * Summernote: WYSIWYG editor to for users to create comments 
    * Crispy Forms: for Django forms
    * Cloudinary: the image hosting service used to upload images
    * Bootstrap: CSS Framework for developing the site
    * Secret Key Generator: https://djecrety.ir/
* Validators:
    * W3C: validate html and css
    * PEP8: validate python code
    * Jshint: validate javascript

## Agile

## Fixed and Unfixed Bugs

* Fixed bugs:
    * When initial commit was made, it failed as I had divergent branches, there was remote work that was not local. I found the answer on Slack. I integrated the remote changes by using the 'git config pull.rebase false' command to tell git how to merge the changes 'git pull' command to get the changes from the local branch, and then it was possible to 'git push' my commit.

* No known unfixed bugs

## Validation 

ADD TEXT HERE
* When tested the website generally recommended pep8online.com was down. 
    * As a workaround, a PEP8 validator was used in the Gitpod Workspace directly by following these steps:
    * Run the command pip3 install pycodestyle (Note that this extension may already be installed, in which case this command will do nothing.)
    * In my workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
    * Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results.
    * Select pycodestyle from the list.
    * PEP8 errors would be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

* Fixed: Extra spaces in code. Comments incorrectly added. Removed extra trailing spaces as hilighted.   

## Testing

* Tested on the local terminal, and tested the deployed site on Google Chrome on a mac and also a laptop

* Home Page:
    * Tested: ADD TEXT HERE

* Navigation:
    * Tested: ADD TEXT HERE

## Project Creation and Deployment

The project was created in Git Hub using the Code Institute template.

The following commands were used throughout the project:
* git add . - This command was used to add files to the staging area before committing.
* git commit -m "I add commit message here" - This command was used to to commit changes to the local repository.
* git push - This command is used to push all committed changes to the GitHub repository. 

* Deployment from Heroku:    
    * Navigate to Deploy tab 
    * Click on Github for deployment method
    * Search and connect to app name (CareHub-Project4-2023)
    * Scroll to bottom and click 'Deploy Branch'
    * On successful deploy, I clicked on 'View app' and got a successful deploy message

## Credits

All images used are from www.freepix.com

## Acknowledgements
Thanks to my mentor, my facilitator, my fellow students on Slack, tutoring support and to my friends for helping test the site.
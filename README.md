## CAREHUB
The website is aimed at people require care services, and carers who may be searching for the information for them.
The app provides a list of Care Providers, their services information and contact details. Registered users are able to rate their services, and also leave comments on the service they received.
The design is aimed to be simple and easy to navigate. Accessiblity was a major factor in the site design. 

Link to the site here https://carehub-caresearch2023.herokuapp.com/

## Am I Responsive mockups
![Responsive Mockup](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/amiresponsive.jpg)

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

* Accessibility:
    * To ensure maximum user accessibility, the contrast between the background colour and text was kept to a high contrast.
    * Font size was kept large to ensure high legibility
    * Atkinson Hyperlegible is used as the main text font, as it is recommended as being highly legible.
    * The overall design was kept simple and easy to follow. Call-to-action buttons were made easy to view and locate on the page.

* Colour pallet:
    * The main colours choosen gave the site a medical feel, with warm accent colours to give an approchable feel.  
    ![Colour Pallett](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/colour_scheme.jpg)

* Wireframes:
    <details>
    <summary>Balsamiq wireframes</summary>
    
    * Home Page Wireframe
    ![Home Page](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/homepage.jpg)

    * Care Providers list Wireframe 
    ![|List Page](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/providerlist.jpg)

    * Care Providers details Wireframe
    ![Detail Page](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/providerdetails.jpg)
    
    * Add Care Provider page Wireframe
    ![Add Page](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/addprovider.jpg)

* Database Drawing:
    <details>
    <summary>Database schema</summary>

    * Database
    
    ![Database](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/database_schema_drawing.jpg)

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
* Header and footer
    ![header](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/header_logo_nav.jpg)
    * Logo: This logo is positioned in the top left of the navigation bar. The logo is linked to the home page so the user can easily navigate back to the home page.
    * Navigation Bar: The navigation bar is present at the top of every page and includes links to other pages.
When logged in, the user will see an icon and their user name. If not logged in they will see a link to sign up or log in.
The navigation bar is fully responsive, collapsing into a hamburger menu for smaller devices. The links show the user their current page by displaying a different colour and an underline, this is also used when the user hovers over a link so they can see what page they will navigate to.
    ![footer](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/footer.jpg)
    * Footer: The footer section has links to Carehub's Facebook, Instagram, Twitter and Youtube pages.
These open in a separate browser window to avoid taking the user away from the site.

* Home page
    * The call to action section
    ![cta_in](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/cta_section_loggedin.jpg)
    ![cta_out](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/cta_section_notloggedin.jpg)
    * The call to action section shows a relevant image, and a easy to locate call to action button: sign up button if not logged in, or find care button if already logged in.
    * The about section
    ![about](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/about_section.jpg)
    * The about section gives a brief description of who the site is for and what type of care a user can find there. 

* Account pages
    * Sign In
    ![signin](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_in.jpg)
    * Sign up
    ![signup](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_up.jpg)
    * Log out
    ![logout](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_out.jpg)
    * Allauth was used to create the Sign up / Log in / Log out functions. A success message is displayed when the user has signed in / signed out / or created and account sucessfully.

* Care Providers' list view
    ![providerlist](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/providers_list.jpg)
    * Shows a list of Care Providers that have been approved by the site Admin, ordered by business name. The page paginates after every 6 providers are listed. Clicking on the 'Care providers Detail' button will bring the user to the full details for that provider.

* Care Provider Detail view
    ![providerdetail](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/provider_details.jpg)
    * Shows the full details for that provider
    * If the user is the author of the provider listing, they will see the buttons to edit or delete that provider
    ![editdeleteprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/edit_delete_provider.jpg)

* Care Provider Detail - Comments section
    ![comments](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/comments.jpg)
    * Shows comments that have been approved by the site Admin for that Care Provider. If the user is signed in, a comment box is shown where they can leave a commnet. They are shown a message to show they have sucessfully left a comment, and it awaits approval by admin.

* Add a care provider page
    ![comments](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/add_provider.jpg)
    * If logged in, a user will see a form to add a care provider. A care provider can add an image, or a default placeholder image will be used. The user will receive a success message. The care provider details then await approval by the site Admin.

* Edit care provider page
    ![comments](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/edit_provider.jpg)
    * If logged in, and the user is the author of the Care Provider, they can see the edit button, which brings them to an edit provider page. The form is pre populated with all fields from the original provider details. When changes are submitted, the user will receive a message that the details have been sucessfully updated.

* Delete care provider page
    ![comments](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/delete_provider.jpg)
    * If logged in, and the user is the author of the Care Provider, they can see the delete button. If clicked, they will be asked to confirm they wish to delete the provider, or they can cancel. If they click delete, the user will receive a message to say the provider has successfully been deleted.

* Future Features
    * Have different user types for a care provider or a care seeker, so they can be restricted to certain areas of the website
    * Care providers can be filtered by county or by speciality
    * Bookmarks page, so logged in user can bookmark providers, and see a page of their bookmarked providers

## Technologies Used
* Languages: Python, HTML, CSS, Javascript
* Other technologies used:  
    * Django: Main python framework 
    * Django-allauth: authentication library used to create user accounts
    * Elephant PostgreSQL: database
    * Heroku: cloud based platform to deploy the site
    * Balsamiq: to draw wireframes
    * Chrome Dev Tools - for testing responsiveness, performance and for debugging
    * Font Awesome: icons used on the site
    * GitHub: version control and agile Kanban boards
    * Google Fonts: for fonts used on site
    * Favicon: to create a favicon for the site
    * Summernote: WYSIWYG editor - for users to create comments 
    * Crispy Forms: for Django forms
    * Cloudinary: image hosting service 
    * Bootstrap: CSS Framework for developing the site
    * Secret Key Generator: https://djecrety.ir/
    * Database schema drawing toool: https://drawsql.app
* Validators:
    * W3C: to validate html and css
    * PEP8: to validate Python code
    * Jshint: to validate Javascript

## Agile

## Fixed and Unfixed Bugs

* Fixed bugs:

    * The care providers list was misaligned, the loop was in the wrong place, it had an opening div before it, and closing div after, leaving the styling crossing over into the next iteration, causing the next iteration to be moved out by 12px each time. It was resolved by moving the closing div tag.

    * When a success message was added to the DeleteProvider view, it was not showing up. A bug in Django which has yet to be fixed meant Message Mixins didn't work with Delete Views.
    The workaround was found on Stack: https://stackoverflow.com/a/42656041

    * When initial commit was made, it failed as I had divergent branches, there was remote work that was not local. I found the answer on Slack. I integrated the remote changes by using the 'git config pull.rebase false' command to tell git how to merge the changes 'git pull' command to get the changes from the local branch, and then it was possible to 'git push' my commit.

    * When site was deployed to Heroku, the css file was not linking. After speaking with tutor support, a workaround was that in the env.py file add a var DEV,  with a value of '1', then DEBUG was set to DEBUG = 'DEV' in os.environ. Then disable collect static variable was removed from Heroku vars. The deployed site then ran with css working.

* No known unfixed bugs

## Validation 

ADD TEXT HERE
* Add

* Fixed: Add  

## Testing

* Add link

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
* Code Institue's 'I think therefore I blog' tutorial
* All images used are from www.freepix.com

## Acknowledgements
Thanks to my mentor, my facilitator, my fellow students on Slack, tutoring support and to my friends for helping test the site.
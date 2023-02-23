# Carehub Testing - Contents:
- [User Story Testing](#user-story-testing)
- [Browser and Devices Tests](#browser-tests)
- [Manual Tests](#manual-tests)
  * [Home Page](#home-page)
  * [Site Navigation](#site-nav)
  * [Care Providers List](#providers-list)
  * [Care Providers Detail](#providers-detail)
  * [Add a Care Provider](#add-provider)
  * [Update a Care Provider](#update-provider)
  * [Confirm Delete a Care Provider](#confirm-delete-provider)
  * [Django All Auth Pages](#django-all-auth-pages)

## User Story Testing

### EPIC | First Time User - Site design and navigation
* As a First time User, I can view information on the Home Page so that I can clearly see the purpose of the site 
* As a First Time User, I can easily understand the main purpose of the app, so that I can find the infomation I require easily
    <details>
    <summary>Site purpose</summary>
    * Appropriate hero image on main page
    * Hero heading outlining main purpose of the site
    * Main paragraph and heading explains main purpose of the site
    * About section content, headings and icon explains purpose and features of the site
    ![sitepurpose1](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/cta_section_notloggedin.jpg)
    ![sitepurpose2](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/about_section.jpg)

  * As a First Time User, I can navigate the site so that I can navigate to the information I require in an effective and intuitive fashion
    <details>
    <summary>Navigation</summary>
    * Navbar is easy to read
    * Navbar is available on every page
    * Navbar is responsive, collapses to a burger for smaller size devices
    * Navbar item is a different colour and underlined to show the current page, or on hovering the mouse over a link
    * A link is provided in the navbar to sign up, and also a signup button CTA is displayed on the main page if the user is not logged in.
    ![nav1](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/nav_loggedout.jpg)

  * As a First Time User,  I can view care providers, so that I can browse a list of care providers
    <details>
    <summary>List of Care Providers</summary>
    * A list of Care Providers, with an image and summary details is displayed
    * A CTA button is displayed to view the Care Provider's full details
    ![list](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/providers_list.jpg)
  * As a First Time User,  I can view care providers full profile, so that I can see all of their details and comments 
    <details>
    <summary>Care Providers Details</summary>
    * A detailed view of the Care Provider, with an image is displayed
    * A list of comments made about this provider is displayed at the end of the listing
    ![detail](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/providerdetails.jpg)


### EPIC | Frequent User - account functions
* As a Frequent User, I can create a new account so that I can access all functions provided by the app
    <details>
    <summary>Sign up</summary>
    * A link is provided in the navbar to sign up, and also a signup button CTA is displayed on the main page if the user is not logged in.
    ![signup](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_up.jpg)

* As a Frequent User,  I can login and logout, so that I can access my details 
    <details>
    <summary>Log in /out</summary>
    * A link is provided in the navbar to log in or log out
    * If login is selected, A login form is then available
    * If logout is selected, the user is asked if they are sure they wish to logout
    ![signin](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_in.jpg)
    ![signout](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_out.jpg)

* As a Frequent User, I can see my login status so that I can know if I am logged in or out
    <details>
    <summary>Logged in status</summary>
    * An icon and user name is displayed if the user is logged in
    * If the user is not logged: register and login menu items are displayed
    ![status](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/testingimages/loggedin.jpg)
    ![nav1](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/nav_loggedout.jpg)
    
* As a Frequent User,  I can view care providers and service provided, so that I can see care providers that suit my needs 
    <details>
    <summary>List of Care Providers</summary>
    * A list of Care Providers, with an image and summary details is displayed
    * A CTA button is displayed to view the Care Provider's full details
    ![list](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/providers_list.jpg)
    * A detailed view of the Care Provider, with an image is displayed
    * A list of comments made about this provider is displayed at the end of the listing
    ![detail](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/providerdetails.jpg)

* As a Frequent User,  I can login and comment on a care provider, so that I can give my feedback on their service
    <details>
    <summary>Comments box</summary>
    * A comment box is displayed under the Care Provider details section, if the user is logged in
    ![comments](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/comments.jpg)

### EPIC | Care Provider Account
* As a care provider,  I can login and logout, so that I can access my details
    <details>
    <summary>Log in /out</summary>
    * A link is provided in the navbar to log in or log out
    * If login is selected, A login form is then available
    * If logout is selected, the user is asked if they are sure they wish to logout
    ![signin](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_in.jpg)
    ![signout](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_out.jpg)

    * As a care provider,  I can see my login status so that I can know if I am logged in or out 
    <details>
    <summary>Logged in status</summary>
    * An icon and user name is displayed if the user is logged in
    * If the user is not logged: register and login menu items are displayed
    ![status](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/testingimages/loggedin.jpg)
    ![nav1](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/nav_loggedout.jpg)

    * As a care provider,  I can create an account, so that I can add my details 
    <details>
    <summary>Add a care provider</summary>
    * If the user is logged in, a new care provider account can be created, which is approved by Admin
    ![addprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/add_provider.jpg)  

    * As a care provider,  I can update my account details, so that I can manage my account content
    <details>
    <summary>Edit a care provider</summary>
    * If the user is logged in, Edit button is displayed under the Care Provider details created by that user
    * If the user is logged in, a care provider can edit a Care Provider which was created by them
    ![editprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/edit_provider.jpg) 

    * As a care provider,  I can delete my account details, so that I can manage my account 

    https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/delete_provider.jpg
    <details>
    <summary>Delete a care provider</summary>
    * If the user is logged in, Delete button is displayed under the Care Provider details created by that user
    * If the user is logged in, a care provider can delete a Care Provider which was created by them
    * They will be asked to confirm they wish to delete
    ![deleteprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/delete_provider.jpg) 


### EPIC |  Site Admin
* As a Site Admin,  I can approve care provider’s accounts, so that I can check they are authentic care providers
    <details>
    <summary>Approve care provider</summary>
    * From the admin panel, the Site Admin can approve a provider
    ![adminappprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/testingimages/admin_approve_careprovider.jpg) 
* As a Site Admin,  I can add a care provider account, so that I can add to the site content's list of care providers
    <details>
    <summary>Add care provider</summary>
    * From the admin panel, the Site Admin can add a provider
    ![adminaddprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/testingimages/admin_add_provider.jpg)
* As a Site Admin,  I can update or delete a care provider’s accounts, so that I can manage my care providers content
    <details>
    <summary>Admin update or delete care provider</summary>
    * From the admin panel, the Site Admin can update or delete a provider
    ![admindelprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/testingimages/admin_delete_provider.jpg)
    ![admineditprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/testingimages/admin_update_careprovider.jpg)
* As a Site Admin,  I can approve comments, so that I can filter out objectionable comments
    <details>
    <summary>Approve comments</summary>
    * From the admin panel, the Site Admin can approve comments
    ![adminappcomms](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/testingimages/admin_approve_delete_coms.jpg)
* As a Site Admin, I can update comments, so that I can manage my care providers content
    <details>
    <summary>Update comments</summary>
    * From the admin panel, the Site Admin can update comments
    ![adminupdatecomms](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/testingimages/admin_edit_provider.jpg)
* As a Site Admin, I can delete comments, so that I can manage my care providers content
    <details>
    <summary>Delete comments</summary>
    * From the admin panel, the Site Admin can delete comments
    ![admindelcomms](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/testingimages/admin_approve_delete_coms.jpg)


## Browser and Devices Tests
* Browsers: tested on Google Chrome and Safari browsers with no issues noted.
* Devices: viewed on the following devices to check responsiveness: iPhone 11 Pro, iPhone 14, Samsung Galaxy, iPad, iMac pro 15in screen, iMac 27in screen
* Chrome Developer tools: checked multiple devices to check responsiveness


## Manual Tests

### Home Page
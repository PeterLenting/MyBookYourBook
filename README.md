# MyBookYourBook

## Introduction
Reading is fun and reading books creates understanding. 
So it’s important to give everyone the opportunity to read as many books as they want. 
MyBookYourBook will help people achieve that.

- [View the page here](https://mbyb-app.herokuapp.com/). This application is hosted on Heroku using a Postgres (MySQL Database).
- [View the Github Repository here](https://github.com/PeterLenting/MyBookYourBook)

## Contents table
1. [UX](https://github.com/PeterLenting/MyBookYourBook#ux)
   - [What is it?](https://github.com/PeterLenting/MyBookYourBook#what-is-it)
   - [Who is the target audience](https://github.com/PeterLenting/MyBookYourBook#who-is-the-target-audience)
   - [The Goal](https://github.com/PeterLenting/MyBookYourBook#the-goal)
   - [Mock-ups](https://github.com/PeterLenting/MSP3#mock-ups)
   - [User stories](https://github.com/PeterLenting/MyBookYourBook#user-stories)
   - [Design](https://github.com/PeterLenting/MyBookYourBook#design)
2. [Features](https://github.com/PeterLenting/MyBookYourBook#features)
   - [Existing features](https://github.com/PeterLenting/MyBookYourBook#existing-features)
   - [Features left to implement](https://github.com/PeterLenting/MyBookYourBook#features-left-to-implement)
3. [Technologies used](https://github.com/PeterLenting/MyBookYourBook#technologies-used)
4. [Testing](https://github.com/PeterLenting/MyBookYourBook#testing)
   - [Resonsive testing](https://github.com/PeterLenting/MyBookYourBook#responsive-testing)
   - [Manual testing](https://github.com/PeterLenting/MyBookYourBook#manual-testing)
   - [Improvements after testing](https://github.com/PeterLenting/MSP3#improvements-after-testing)
   - [Browsers](https://github.com/PeterLenting/MyBookYourBook#browsers)
   - [Automated testing](https://github.com/PeterLenting/MyBookYourBook#automated-testing)
5. [Deployment](https://github.com/PeterLenting/MSP3#deployment)
   - [How to add this project to your local workspace](https://github.com/PeterLenting/MyBookYourBook#How-to-add-this-project-to-your-local-workspace)
6. [Credits](https://github.com/PeterLenting/MyBookYourBook#credits)
   - [Content](https://github.com/PeterLenting/MyBookYourBook#content)
   - [Media](https://github.com/PeterLenting/MyBookYourBook#media)
   - [Code](https://github.com/PeterLenting/MyBookYourBook#code)
   - [Acknowledgements](https://github.com/PeterLenting/MyBookYourBook#acknowledgements)
7. [Disclaimer](https://github.com/PeterLenting/MyBookYourBook#disclaimer)

## UX

### What is it?
MyBookYourBook is a fictional platform for people who love books. Everyone can sign up for an account and with that account the user can offer his own books to other people. 
The books can be sold, but also rented out to other users. 
There are multiple platforms where anybody can sell or buy books. The renting-part of MyBookYourBook is something new. 
It is different from a library, because by stimulating people to rent out their own books the supply of popular books will be a lot bigger. 
In libraries the waiting list for popular books can be very long. 

### Who is the target audience?
People who love to read paper books. 

### The Goal
I really like to read. Some books I like to read, but have no need to keep them. This site is a platform to sell the book on, but also to rent out a book. 
This way, the person who bought the book can earn a little bit of money back and someone with a smaller budget can read a book for a small amount of money. 

### User stories
As a visitor, I want:

1. To search for certain books, in order to rent them.
2. To search for certain books, in order to buy them.
3. To send a message to MyBookYourBook, in order to get answers to my questions.
4. To make a deposit, in order to be able to rent books.
5. To send a message to another user who is offering a book, in order to but it.
6. To add a book to the site, in order to sell it.
7. To update my profile, in order to change my emailaddress.

### Design

The design is based on comparable webshops like Bookdepository.com, Amazon.com and the Dutch Bol.com. Using a similar design gives the users a familiar feeling. 
An important part of all these sites is the Search-bar. Users come here and know what they want, which book they want to read. The search-bar makes it very easy to find the right book
The colorschema is basic and neutral with the 'Bright Cyan' (#17a2b8) sticking out. The images (covers of the books) are quite noisy and divers, so the rest of the site should have a clean look and feel.
The Roboto-font is easy on the eye and has a nice, clean look.

## Features

### Existing features

**Navigation bar**

Tha navigation bar contains links to all the important pages: 
Home, About, Contact, Books (dropdown with 'All books', 'Books for sale', 'Books for rent' and 'My books'), Login and Register when the user is not logged in. 
Home, About, Contact, Books (dropdown with 'All books', 'Books for sale', 'Books for rent' and 'My books'), Add a book, Make (new) deposite, Profile, Logout, a welcome message and a shoppingcart when the user is logged in. 
'Make deposite' is shown when the user hasn't made a deposite yet. When the user has made a prior deposite 'Make new deposite' is shown.
On mobile and tablet the navigation bar is a navbar-toggler (Bootstrap), on desktop the navbar is fully shown op top of the page. 
The fixed-top class (Bootstrap) is added to keep the footer sticked to the top at all time.

**Footer**

Contains links to (not yet existing) social media pages: Twitter, Facebook, Instagram and Youtube.

**Homepage(products)**

Shows all the books on offer, except for the books of the user that is logged in. Not all the information of each book is shown for clarity-reasons. 
To read more about a book, simply click on the title, the image or ‘more…’ at the end of the summary.
To buy a book, simply click on the ‘Buy-button’. The logged-in user will be taken to the [Usercontact-page](https://github.com/PeterLenting/MyBookYourBook#UserContactPage). If the user is not logged-in, he will be taken to the login-page.
To rent a book, simply click on the ‘Rent-button’. If the user is logged in, the book will be added to the shoppingcart and the button changes to 'Remove book'. If the user is not logged-in, he will be taken to the login-page.

**UserContactPage**

On clicking the Buy-button for a book the user is taken to the usercontactpage. 
There a default email is set up using the email and first name of the request.user and the provider of the book and the title of the book.
Besides that the book the request.user wants to buy is shown.
The email is send to the provider of the book. It’s up to them to get it all done.

**Rentpage**

Shows the number of books in the shoppingcart, the total rentprice per week and the books that are in the cart. Gives option to remove each book from the cart. 
"Let's rent"-button takes user to the rent page.
If cart is empty: "There are no items in your cart..."

**Rentpage**

Shows the username of request.user, his email, the number of books in the cart and the total rentprice per week. Besides that the books in the cart are shown.
On clicking the "send"-button, a form is send to MyBookYourBook.com with all the details.
The user is send to the homepage and sees a message: 
"Great, we recieved your order!
We will contact the owners of the books you want to rent and have them contact you.
Have a great day!"

**Registrationpage**

User gets a form to fill in some basic data. 
At the end the checkbox states “I want to be able to rent books”. If checked after sending in the form the user is led to the [Checkout-page](https://github.com/PeterLenting/MyBookYourBook#Checkoutpage). 
If not checked, the registration is completed after sending in the form. The user is led his [Profile-page](https://github.com/PeterLenting/MyBookYourBook#Profilepage) and encouraged to upload his first book.

**Checkoutpage**

User gets a form to make a deposit of 30 euro. There are two possible messages at the top of the page. One for the user that makes his first deposit and oen for the user that has made a deposit before. 
After sending in the form, the user gets a message that his payment was successfull (or that it wasn’t). And he is encouraged to start renting.

**Aboutpage**

Shows the user why the MyBookYourBook is set up and how the buying and renting works.

**Profilepage**

Shows the users profile and the books he has on offer. 
On this page the user can edit his profile and edit and delete his books.

**Contactpage**

User can use this form to send a message (email) to MyBookYourBook. From email is filled in by default.

**Loginpage**

Allows the user with an account to login. User can also request a new password, or sign up when he is a new user.

**Reset-passwordpage**

If the user has forgotten his password or simply wants to change it, can can request an email and after clicking on the link in the email change his password.

### Features left to implement
There are loads of extra feature that could be build to make this platform even more appealing:

**Implement Google maps** - So users can search on proximity of books on offer. This makes it easier for the users to take care of the logistics.

**Automate rent-process** - So user can see his saldo.

**Swap Option** - Build an option for users to swap books (I have this books on offer and am looking for that book).

**Community** - Build a community so users can discuss books and readingtips.

**Recommended list** - Give suggestions to users which books they might like, based on the books they bought, rented and have on sale.

**Wish list** - Let user add books they would like in a wish list and email them when the book is being offered.


## Technologies used

•	HTML, CSS, JavaScript, Python

•	IDE: [Gitpod](https://gitpod.io/).

•	[Bootstrap](https://getbootstrap.com/) for the grid system of the page.

•	[Google Fonts](https://fonts.google.com/) for the fonts.

•	[Font Awesome](https://fontawesome.com/) for the icons in the footer of the website.

•   [Django 1.11.24](https://www.djangoproject.com/) for rapid development and use of database.

•	[Github](https://github.com/) for version control and for users to view the deployed version of the website.

•   [Heroku](https://www.heroku.com/) to deploy the project.

•   [PostgreSQL](https://www.postgresql.org/) for the database, provided by heroku.

•   [Stripe](https://www.stripe.com/) as payment platform to validate and accept credit card payments securely.

•   [Travis](https://travis-ci.org/) for continuous integration.

•	Paint to edit the images used.

•	Google Chrome developer tools.


### Browsers
The page was tested in Chrome, Internet Explorer and Firefox.

## Testing

### Responsive testing
The responsiveness of the page was tested at all times during the development of the site. Locally as well as in preview using Google Inspect.

### Manual testing

I created, updated, deleted, rented, bought, signed in and out, and contacted myself and had other people testing the project as well during the development. This is a reliable way of discovering whether everything works as it should:

**Search** - To search for certain books, in order to rent them.
**Buy a book** - 
**Rent a book** - 
**Ask a question** - 
**Sign up** - 
**Sign in** - 
**Sign out** - 
**Update Profile** - 
**Add a book** - 
**Edit a book** - 
**Delete a book** - 
**Change my password** - 
**Make deposit** - 


### Automated Testing
The following **validation services** were used to check the validity of the code:

•	W3C Markup Validation Service was used to validate HTML.

•	W3C CSS validation was used to validate CSS.

•	JSHint was used to validate JavaScript.

### Improvements after testing

As said, testing was done all through the development of the project, so lot of improvements were made during and after testing. A few examples:

•   **Messages** The messages shown after the user had done something (like paid successfully), didn't stand out. By changing the styles the do now.

•   **Rent only after paying** Only if the user has paid his deposit he is able to send in the rent-request. At first every user could send in the form, which was off course not the way it was intended. 
So by adding if user.uprofile.have_paid == True to rent.html the user who has not paid yet, is asked to make a deposit first. If the user has paid he can proceed with sending in the form.

•   **Update want_to_rent** At first it was not possible for a user updating his profile to update his answer on "want_to_rent" (which is required to be able to pay the deposit which is required to rent books.)
I fixed that by adding to the update_profile view:


            ```
             if user.uprofile.have_paid is True and user.uprofile.want_to_rent is True:
                return redirect(reverse("profile"))
            elif user.uprofile.have_paid is False and user.uprofile.want_to_rent is True:
                return redirect('checkout')
            else:
                return redirect(reverse("profile"))
            ```

•   **Responsiveness** While testing it appeared not all devices showed the grid as expected, so adjustments had to be made using CSS Media Queries.


## Deployment
The repository for the project is available on [GitHub](https://github.com/PeterLenting/MyBookYourBook).

The project was built using Gitpod. I committed the project and pushed it up to Github. Then I made a connection between Github and Heroku to deploy the project.

**Requirements and Procfile** - A requirements.txt file is used to specify the dependencies required for the application. A Procfile is used to specify to Heroku the commands that are executed by the app on startup.

**Connection between Github and Heroku** - On Heroku Dashboard the “Deploy” tab was chosen and the "GitHub" pane selected. Then the option to auto-deploy the project whenever it’s pushed to on Github was activated, the IP, PORT and my connection string in Heroku settings specified and finally, when scrolled down to "Manual deploy" "Master" branch was deployed.

### How to add this project to your local workspace
To clone this project from GitHub:

• Go to the project's repository.

• Under the repository name, click "Clone or download".

• In the "Clone with HTTPs" section, copy the URL.

• In your IDE open Git Bash.

• Change your current working directory to the location you want the cloned directory to be made in.

• Type git clone, and paste the URL you copied before.

• Hit Enter. The process of cloning will now be completed.

## Credits

### Content
The content on the website was mostly written by me, only the summary of the books is based on [goodreads.com](https://www.goodreads.com/).

### Media
The images from the book-covers are taken from [bookdepository.com](https://www.bookdepository.com/).  
The logo is made by [Freepik](https://www.flaticon.com/authors/freepik), on [Flaticon](www.flaticon.com).

### Code
I wrote all the code myself, with help and inspiration from the users of StackOverflow.com. Questions and answers on that site pointed me in the right direction more than once. 
The Code Institute tutor-team also helped me understand why sometimes some code wasn't working. https://wsvincent.com/django-contact-form/

## Disclaimer
The content of this website is for educational purposes only.

[![Build Status](https://travis-ci.org/PeterLenting/MyBookYourBook.svg?branch=master)](https://travis-ci.org/PeterLenting/MyBookYourBook)

# MyBookYourBook

## Introduction
Reading is fun and reading books creates understanding. 
So it’s important to give everyone the opportunity to read as many books as they want. 
MyBookYourBook will help people achieve that.

- [View the page here](https://mbyb-app.herokuapp.com/)
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
   - [How to add this project to your local workspace](https://github.com/PeterLenting/MSP3#How-to-add-this-project-to-your-local-workspace)
6. [Credits](https://github.com/PeterLenting/MyBookYourBook#credits)
   - [Content](https://github.com/PeterLenting/MyBookYourBook#content)
   - [Media](https://github.com/PeterLenting/MyBookYourBook#media)
   - [Code](https://github.com/PeterLenting/MyBookYourBook#code)
   - [Acknowledgements](https://github.com/PeterLenting/MSP3#acknowledgements)
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

### Design

Based on comparable webshops like Bookdepository.com, Amazon.com and the Dutch Bol.com. Using a similar design gives the users a familiar feeling. 
An important part of all these sites is the Search-bar. Users come here and know what they want, which book they want to read. The search-bar makes it very easy to find the right book.

## Features

### Existing features

**Navigation bar**

**Footer**

Contains links to (not yet existing) social media pages: Twitter, Facebook, Instagram and Youtube.

**Homepage(products)**

Shows all the books on offer, except for the books of the user that is logged in. Not all the information of each book is shown for clarity-reasons. 
To read more about a book, simply click on the title, the image or ‘more…’ at the end of the summary.
To buy a book, simply click on the ‘For Sale-button’. The user will be taken to the usercontactpage(LINK). If the user is not logged-in, he will be taken to the login-page.

**Rentpage**

**UserContactPage**

Allows the logged in user to send a message to the user that is selling the book the request user wants to buy. The book is shown together with a form with a default format. 
All the user has to do is hit send. The selling user will get an email and it’s up to them to get it all done.

**Registrationpage**

User gets a form to fill in some basic data. 
At the end the checkbox states “I want to be able to rent books”. If checked after sending in the form the user is led to the Checkout-page (LINK). 
If not checked, the registration is completed after sending in the form. The user is led his profile page (LINK) and encouraged to upload his first book.

**Checkoutpage**

User gets a form to make a deposit of 30 euro. The message at the top of the page states…. 
After sending in the form, the user gets a message that his payment was successful (or that it wasn’t). And he is encouraged to start renting.

**Aboutpage**

Shows the user why the MyBookYourBook is set up and who the buying and renting works.

**Profilepage**

Shows the users profile and the books he has on offer. 
On this page the user can edit his profile and edit and delete his books.

**Contactpage**

User can use this form to send a message (email) to MyBookYourBook.

**Loginpage**

**Reset-passwordpage**


### Features left to implement
There are loads of extra feature that could be build to make this platform even more appealing:

**Implement Google maps** - So users can search on proximity of books on offer. This makes it easier for the users to take care of the logistics.

**Automate rent-process** - So user can see his saldo.

**Update-profile for want_to_rent** -

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

•	Paint to edit the images used.

•	Google Chrome developer tools.

•	[Github](https://github.com/) for version control and for users to view the deployed version of the website.

•   [Heroku](https://www.heroku.com/) to deploy the project.


### Browsers
The page was tested in Chrome, Internet Explorer and Firefox.


## Testing

### Responsive testing
The responsiveness of the page was tested at all times during the development of the site. Locally as well as in preview using Google Inspect.

### Manual testing

I created, read, updated and deleted posts myself and had other people testing it as well during the development. This is a reliable way of discovering whether everything works as it should:

### Automated Testing
The following **validation services** were used to check the validity of the code:

•	W3C Markup Validation Service was used to validate HTML.

•	W3C CSS validation was used to validate CSS.

•	JSHint was used to validate JavaScript.

## Deployment


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

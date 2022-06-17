# The House of Books

## About

House of Books is an eCommerce site aimed at book lovers looking for their next “new adventures”. The site is designed to be responsive and easy to navigate on a range of devices to make it easily accessible for all users.
This site was built for educational reasons and no deliveries will be fulfilled.

Link to the [site](http://houseofbooks22.herokuapp.com/)

## Contents

- UX (User Experience)
  - User Stories 
- Design Choices
  - Fonts
  - Colours
  - Imagery
  - Wireframes
- Features
  - Site Navigation
  - Features Implemented
  - Future Features
  - Responsive Design
  - Defensive Design
- Database
- Technologies
  - Languages
  - Frameworks and Libraries
  - Tools
- Testing
- Deployment
  - Running locally
- Credits
  - Code
  - Cotent
  - Media
  - Acknowledgements
  
  
## UX (User Experience)
 
### User Stories
 
## Design Choices
 
### Font
  A unique font was used on the site - [Sora](https://fonts.google.com/specimen/Sora).
  
### Colours
  The site uses tons of blue and black. 
  
### Imagery and content
  The images used were taken from these sources as well as the books descriptions, for education purpose:
    - [Goodreads] (https://www.goodreads.com/)
    - [Easons] (https://www.easons.com/)
    
### Wireframes
  The wireframes were created using Balsamiq and can be found bellow:
  
  Desktop:
  
  Tablet:
  
  Mobile:
  
## Features

### Site Navigation
The navigation bar displays different links depending on whether the user is logged in, logged out or a super user.

|      Link     |  Not logged in |    Logged in  |  Logged in as super user |
|---------------|----------------|---------------|--------------------------|
| Logo          |           ✓    |           ✓   |                   ✓      |
| Search bar    |           ✓    |           ✓   |                   ✓      |
| Login in      |           ✓    |          ✗    |                  ✗       |
| Sign up       |           ✓    |          ✗    |                  ✗       |
| Profile Page  |          ✗     |           ✓   |                   ✓      |
| Log out       |          ✗     |           ✓   |                   ✓      |
| Add Products  |          ✗     |          ✗    |                   ✓      |


 ## Features Implemented
 
 ### Navigation
 Header
- All users, logged in or not, can:
  - Navigate to home, view the different categories, special offers, new arrivals. 
  - Create or login in to their profile page.
  - Check their bag.
  - Search for a book.
- Users logged in can access:
  - Navigate to home, view the different categories, special offers, new arrivals. 
  - Check their profile page.
  - Logout from their account. 
  - Make a search for a book.
- Super user logged in can access:
  - Navigate to home, view the different categories, special offers, new arrivals. 
  - Product management, where they can add products to the site. 
  - Check their profile page. 
  - Make a search for a book.
- Users who are not logged in can:
  - Navigate to home, view the different categories, special offers, new arrivals. 
  - Access register and login page.
  - Make a search for a book.
 
 ### Create Profile
 - The users are able to:
    - Create a profile to store their personal information and check their orders history.
    - Confirm their details are correct via email verification.

### Log in to the profile page 
 - The users are able to:
    - Log in to profile page to see their orders history and personal information.
    - If needed, users can update their personal information.

### Products Page
- The users are able to:
    - See all the books for sale on the site
    - Sort it by A-Z, Name, Category, and Price.
    - Check the price of a book
    - Check the different categories
    - Check the rating of a book 
    - Check who is the author of the book
    - Check the image of the cover of the book

### Product Details Page
 - The users are able to:
    - Click the book cover to find out more about the book.
    - There, they can check the title of the book, author, rating, category, price and description. 
    - Add books to the cart.
    - Go back to the products page, if desired.
    - Super users are able to:
    -   Add, edit and delete books. 

### Products Management
- If a super user, the user can:
    - Add a book, including adding an image. In case, one is not provided, a default will be put in place. 
    - Edit the information related to the books
    - Delete a book not available for sale anymore. 

### Bag
 - The users are able to:
    - Adjust number of books on the cart
    - Find out delivery costs
    - Find out how much more they need to spend to get free delivery
    - Clearly see the total of their items by quantity and how much it will cost.
    - Remove and add the number of the existing books on the cart. 

### Checkout
- The users are able to:
    - Save time as personal details are pulled from the profile page if the user is logged in.
    - Save their delivery information to their profile.
    - Clearly see how much they will be charged for their items and delivery.
    - Can see a summary of their order before completing it.
    - Once the order is completed, the user can once again check the order, see the order number and be notified that a confirmation email was sent to the email provided.

### Footer 
- All users can access:
  - The social media links, terms and conditions and privacy policy pages.
- If the user is not logged in, they can see:
  - The different books categories.
  - Links to register and login. 
- If the user is logged in, they can see:
  - The different books categories.
  - Access their profile.
- If a superuser is logged in, he/she can see:
  - The different books categories.
  - Access their profile.
  - A link to product management. 

### Error pages
#### 404.html
  404 page created to redirect users back to the main site in case of an error.
  
#### 403.html
  403 page created to redirect users back to the main site in case they try to access a page they are not authorised to.
  
#### 500.html
  500 error page created to redirect users to the main site after a server error.

## Future Features
- A chat bot where users can ask questions on the site.
- The ability to add many filters to their search criteria at the same time or combine filters. 
- Give the user the ability to track their orders.
- A star rating or upvote functionality for the books.
- Add users reviews to the site. 

## Responsive Design
The site was designed to be mobile first as more users are using their mobile to shop online but this has been adapted to allow the same good experience for desktop and tablet.

## Defensive Design

**Form Validation**
- Form validation has been added to every form to ensure all required information is included before submitting.
- If incorrect data is input, a warning text appears to notify the user that something is missing or gone wrong.

**Default Image if none added**
- In the event that a product is added without an image, a default image will be added. It is unlikely to happen due to the form validation, but just in case, a backup image was set.

**Unauthorised Attempts**
- An error is launched if a user attempts to visit a part of the site which they should not have access to. 

**@login_required**
- @login_required decorator added to restrict access to certain pages.
  - If a logged-out user tries to access a restricted page, they will be redirected to the login page.
  - Only authorised users may perform certain actions, such as add, edit, delete books.

**Bag**
- Validation was put into place to ensure a minimum of 0 product and maximum of 99 products is added to the bag. 
- In the case that 0 is selected the item is removed from the bag.
- Users can not add a negative number on the quantity of books to the bag.

## Database
- Postgres

### Database Design
  The database uses SQL through PostgreSQL and was originally formed from fixtures categories.json and products.json.The Database schema is below :
  
  ![data scheme](https://user-images.githubusercontent.com/65717229/174303224-7288256e-8418-4d82-b845-d86eaac86ef5.png)

  


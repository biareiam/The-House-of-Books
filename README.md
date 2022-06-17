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
- SQLite
    - Cloud based database to hold the product, user, and order fields.

### Database Design
  The database uses SQL through PostgreSQL and was originally formed from fixtures categories.json and products.json.The Database schema is below :
  
  ![data scheme](https://user-images.githubusercontent.com/65717229/174303224-7288256e-8418-4d82-b845-d86eaac86ef5.png)

 ## Technologies
 
 ### Languages
 
**HTML5**
- Used as the main markup language for the website content.
**CSS3**
- Used to style the individual webpages.
**JavaScript**
- Used to show the questions through pagination and for the game play.
**Python 3**
- Used to run the site and database

 ### Frameworks and Libraries
- Django
    - High level framework used for rapid development of the site.
- Panda Library
    - It is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language. It was used to create the most sold books section on the home page. 
 
## Tools
**Git** 
- Git was used for version control (commit to Git and push to GitHub).
**GitHub**
- Used to store, host and deploy the project files and source code after being pushed from Git. I also used it for the Project Kanban board to keep track and split tasks into smaller tasks to make them easier to fulfil.
**Gitpod**
- An online IDE linked to the GitHub repository used to write my code.
**Heroku**
- A Cloud Application Platform used to deploy the site
**AWS** 
- A cloud application to hold media files.
**Google fonts**
- Used to compare and choose fonts.
**Favicons**
- Used to generate a favicon for the website title.
**Lighthouse**
- Used to audit the site for quality and ensure responsiveness.
**JSHint**
- Used to detect errors in the JavaScript files
**PEP8 Online**
- Used to check PEP8 compliance in the code
**W3C Markup Validator**
- Markup validation service for HTML5
**Jigsaw Validator**
- CSS3 Validation Service

## Testing

### Automated Testing

**Bag**
  Automated testing of views was completed to:
    - Test the calc_subtotal function works as expected.
    - Test the bag views work correctly.
    - Test the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the products page is accessible by name.
    - Test that the view_bag view works correctly.
    - Test that the add to bag view works as expected.
    - Test that the add_to_bag function adds the item to the bag.
    - Test that the add_to_bag view adds the product to the bag.
    - Test that the add_to_bag view increases the quantity of an item if the item is already present in the shopping bag.
    - Test that the adjust bag view works as expected to calculate total.
    - Test that the add_to_bag view updates the quantity of an item if the item is already in the bag.
    - Test remove from bag view removes the product from the bag.
    - Test that the remove_from_bag view removes an item from the bag.
    - Test that the remove from bag view returns an error if something goes wrong.
    
**Checkout**
  Automated testing of views was completed to:
    - Test the checkout page loads correctly.
    - Test that the cache_checkout_data view works as expected.
    - Test the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the products page is accessible by name.
    - Test get checkout view when items in the bag.
    - Test error msg appears when bag empty.
    - Test error msg appears when no stripe key.

**Check if user is authenticated then autofill the form with details**
  Automated testing of models was completed to:
    - Test the order model.
    - Test order line model string method.
  
  Automated testing of forms was completed to:
    - Test to see if full name field is required.
    - Test to see if email field is required.
    - Test to see if phone number field is required.
    - Test to see if country field is required.
    - Test to see if town_or_city field is required.
    - Test to see if street_address1 field is required.
    - Check the field only displays certain fields.

**Profiles**
  Automated testing of views was completed to:
    - Test the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the profile page is accessible by name.
    - Test the profile form works if form is valid.
    - Test orders displayed on login to profile page.

  Automated testing of models was completed to:
    - Test retrieving the user profile.
    - Test the user profile string method returns the username.
    
  Automated testing of forms was completed to:
    - Test that none of the form fields are required.
    
**Products**
  Automated testing of views was completed to:
    - Test the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the products page is accessible by name.
    - Test products display.
    - Test categories sort functionality.
    - Test that the sort functionality works.
    - Test that the search functionality works as expected.
    - Test that the search error message display correctly.
    - Test product detail page loads via url.
    - Test product detail page loads via name.
    - Test product detail page loads via template.

  Automated testing of models was completed to:
    - Test category model string method.
    - Testing category models friendly name string method returns friendly name.
    - Test product model string method.
    - Test that the product name is returned.
    - Test that the product description is returned.
    - Test whether a product has sizes or not.
    - Test whether a product has weights or not.

  Automated testing of forms was completed to:
    - Test to see if review title field is required.
    - Test to see if review field is required.
    - Check the field only displays certain fields.
    - Test to see if review title field is required.

**Blog**
  Automated testing of views was completed to:
    - Test the blog page loads correctly.
    - Test the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the blog page is accessible by name.
    - Test blog posts display as expected.
    - Test to see if the post string method returns the title as expected.

**Home Page**
  Automated testing of views was completed to:
    - Test the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the home page is accessible by name.
    - Test the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the privacy page is accessible by name.
    - Test the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the terms and conditions page is accessible by name.

### Manual Testing
**Browsers**
The site was tested on:
- Safari
- Google Chrome
- Firefox
- Devices Used
The site was tested in many different devices. 

#### Navigation
-  All users
| Feature      | Expected                                                            | Testing                      | Result                                                                                                                | Pass/Fail |
|--------------|---------------------------------------------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------|
| Home button  | To redirect to home page                                            | Click the home button        | Button navigates to home                                                                                              | Pass      |
| Navbar links | Clicking All books takes user to All books page                     | Click All books              | Redirected to All books page                                                                                          | Pass      |
|              | Clicking category takes user to the specific category page          | Click each category in turn  | Redirected to specific category page                                                                                  | Pass      |
|              | Click on bag icon and direct user to cart page                      | Click Bag                    | Redirected to cart page                                                                                               | Pass      |
|              | Clicking Blog takes user to the Blog homepage                       | Click Blog                   | Redirected to Blog Page                                                                                               | Pass      |
|              | Searching using Search Bar displays the books in the books page     | Type "fantasy" in search bar | Redirected to a page in which the relevant results are displayed, "fantasy" in the title or on the book description.  | Pass      |
| Footer       | Redirect to Facebook in new tab                                     | Click Facebook icon          | Facebook page opened in new tab                                                                                       | Pass      |
|              | Redirect to Instagram in new tab                                    | Click Instagram icon         | Instagram page opened in new tab                                                                                      | Pass      |
|              | Redirect to Twitter in new tab                                      | Click Twkitter icon          | Twitter page opened in new tab                                                                                        | Pass      |
|              | Redirect to Pinterest in new tab                                    | Click Pinterest icon         | Pinterest page opened in new tab                                                                                      | Pass      |
|              | Clicking T&Cs takes user to the Terms and Conditions page           | Click T&Cs                   | Terms and conditions page opened                                                                                      | Pass      |
|              | Clicking Privacy Policy takes user to the Terms and Conditions page | Click Privacy Policy         | Privacy Policy page opened                                                                                            | Pass      |

- Users who are logged in 
| Feature      | Expected                                              | Testing                             | Result                                       | Pass/Fail  |
|--------------|-------------------------------------------------------|-------------------------------------|----------------------------------------------|------------|
| Navbar links | Clicking Profile takes user to their profile page     | Click Profile                       | Redirected to Profile Page                   | Pass       |
|              | Click Log Out logs out the user                       | Click Log Out, it logs out the user | User logged out and redirected to books page | Pass       |
|              | Click on the bag icon and is directed to the bag page | Click bag icon                      | Redirected to the bag page                   | Pass       |


- Users who are not logged in
 | Feature      | Expected                                              | Testing         | Result                           | Pass/Fail  |
|--------------|-------------------------------------------------------|-----------------|----------------------------------|------------|
| Navbar links | Click Log In redirects to log in page                 | Click Log In    | User redirected to Log In Page   | Pass       |
|              | Click Register redirects to log in page               | Click Register  | User redirected to Register Page | Pass       |
|              | Click on the bag icon and is directed to the bag page | Click bag icon  | Redirected to the bag page       | Pass       |


#### Home Page
| Feature       | Expected                                                                   | Testing             | Result                          | Pass/Fail  |
|---------------|----------------------------------------------------------------------------|---------------------|---------------------------------|------------|
| See more      | Clicking on the "see more" button and be redicted to the books page        | Click see more      | Redirected to the products page | Pass       |
| See all books | Clicking on the " see all books" button and be redicted to the books page  | Click see all books | Redirected to the products page | Pass       |

#### Register Page
| Register functionality | Form validation for email requires @ symbol                                        | Attempt to register without @ in input field                        | Form validation requests valid email address               | Pass |
|------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------|------|
|                        | E-mail Again value must be same as Email value                                     | Attempt to register with incorrect email in email again input field | Form validation requests email address must match          | Pass |
|                        | Username must be between 4 and 15 characters                                       | Attempt to enter username with less than 4 characters               | Feedback error displayed                                   | Pass |
|                        | Username must be between 4 and 15 characters                                       | Attempt to enter username with more than 15 characters              | Form restricts the user from using more than 15 characters | Pass |
|                        | Password must be longer than 8 characters                                          | Attempt to enter password with less than 8 characters               | Form restricts the user from using less than 8 characters  | Pass |
|                        | Register with new user and password to be logged in and redirected to Profile page | Enter email address, name, username, password and click register    | New account registered and profile page shown              | Pass |

#### Log in Page
| Feature              | Expected                                                                                    | Testing                                           | Result                                                                              | Pass/Fail  |
|----------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------|------------|
| Log in functionality | Correct user/pass combination directs user to their profile page with name displayed in tab | Log in with correct username/password combination | Redirected to user profile page with name displayed in tab                          | Pass       |
|                      | Incorrect username/password combination shows error message                                 | Attempt to log in with incorrect credentials      | "The username and/or password you specified are not correct." error message appears | Pass       |
| Link to Register     | Redirect to Register page                                                                   | Click link to register                            | Redirected to Register page                                                         | Pass       |

#### Profile Page
| Feature              | Expected                                                           | Testing                                                                          | Result                                                              | Pass/Fail |
|----------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------|-----------|
| Personal Information | Personal information is visible if previously saved                | Navigate to Profile page, view personal information                              | The personal information is visible in Personal Information section | Pass      |
|                      | Personal information can be updated                                | Navigate to Profile page, change personal information, click update information. | The personal information is updated with the new details.           | Pass      |
| Order History        | Order History is visible if order placed while logged in           | Navigate to Profile page, view Order History Section                             | The Order History is visible                                        | Pass      |
|                      | Order information can be accessed by clicking on the "view" button | Navigate to Profile page, view Order History Section, click on "View" button     | Order Information is visible                                        | Pass      |

#### Book Products Pages
| Feature           | Expected                                             | Testing                                     | Result                                         | Pass/Fail  |
|-------------------|------------------------------------------------------|---------------------------------------------|------------------------------------------------|------------|
| All books visible | The books page shows all the available books         | Open the books page and view all the books  | All books visible                              | Pass       |
|                   | Searching by category shows books from that category | Select to search by each category           | Book from each category successfully displayed | Pass       |

#### Book Details Page
| Feature      | Expected                                                                      | Testing                                               | Result                    | Pass/Fail |
|--------------|-------------------------------------------------------------------------------|-------------------------------------------------------|---------------------------|-----------|
| Book Details | Book description, among other informations are displayed for individual books | Open Book Detail page and view the book's information | Books details visible     | Pass      |
| Add to bag   | Clicking Add to bag adds the book to the bag                                  | Open Book Detail page click add to bag                | Book displayed in the bag | Pass      |

#### Add products
| Feature         | Expected                                             | Testing                                                      | Result                                                                                 | Pass/Fail |
|-----------------|------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------|
| Add new books   | Only admin is allowed to visit add a new book        | Log in as non-superuser and attempt to access /products/add/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass      |
| Form Validation | Required fields must be completed to add the product | Attempt to add product without filling in a required field   | Error message "Please fill in this field"                                              | Pass      |

#### Edit products
| Feature         | Expected                                                 | Testing                                                                 | Result                                                                                 | Pass/Fail |
|-----------------|----------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------|
| Edit books      | Only admin is allowed to visit edit a book's information | Log in as non-superuser and attempt to access /products/<item_id>/edit/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass      |
| Form Validation | Required fields must be completed to edit the product    | Attempt to edit product without filling in a required field             | Error message "Please fill in this field"                                              | Pass      |

#### Bag
| Feature      | Expected                                                                     | Testing                                                                | Result                        | Pass/Fail |
|--------------|------------------------------------------------------------------------------|------------------------------------------------------------------------|-------------------------------|-----------|
| View Items   | Correct books are in the bag                                                 | Add book to bag, check quantity and total on the bag                   | Expected books are in the bag | Pass      |
| Update Items | Update the number of a books in the bag and it will reflect in bag and price | Change number of books in bag and check quantity and total has updated | Total and quantity updated    | Pass      |
| Remove Items | Click on the remove icon for item to be removed from the bag                 | Click remove beside relevant book                                      | Item removed from bag         | Pass      |

#### Checkout
| Feature         | Expected                                      | Testing                                                  | Result                                    | Pass/Fail |
|-----------------|-----------------------------------------------|----------------------------------------------------------|-------------------------------------------|-----------|
| View Items      | Correct books are in the checkout             | Add book to bag, click Checkout                          | Expected books are in the checkout list   | Pass      |
| Form Validation | Required fields must be completed to complete | Attempt to check out without filling in a required field | Error message "Please fill in this field" | Pass      |

### User Stories Testing
| User Story ID                 | As a/an           | I want to be able to...                                     | So that I can...                                                                          | Testing                                                                                        | Result |
|-------------------------------|-------------------|-------------------------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------|
| Viewing Products & Navigation |                   |                                                             |                                                                                           |                                                                                                |        |
| 1                             | User/Shopper      | view individual products                                    | See what the books are about.                                                             | View Products Page                                                                             | Pass   |
| 2                             | User/Shopper      | be able to add, edit quantity and remove items from my cart | buy it after browsing.                                                                    | Add product to bag, view toast, update item quantity, remove from bag                          | Pass   |
| 3                             | User/Shopper      | see any special offers and new arrivals                     | take advantage of saving money on products I'd like to buy and be aware of new books.     | Navigation bar displays free shipping if shopper spends €20 or more                            | Pass   |
| Registration and Accounts     |                   |                                                             |                                                                                           |                                                                                                |        |
| 4                             | User/Shopper      | register for an account                                     | keep track of my orders and check my personal details, being able to update it if needed. | Users can register for an account and view their orders in the profile page                    | Pass   |
| 5                             |                   | receive email confirmation upon signing up                  | verify my set up was successful.                                                          | User receives email when they register for an account                                          | Pass   |
| 6                             |                   | be able to reset my password in case I forget it            | regain access to my account.                                                              | User can request email to reset their password                                                 | Pass   |
| 7                             |                   | have the ability to log in to the site with my details      | view my orders and personal details.                                                      | Users can log in using their registered details and view their orders and personal details     | Pass   |
| 8                             |                   | update my personal details.                                 | keep my personal information updated.                                                     | Users can update their personal details in the profile section                                 | Pass   |
| 9                             |                   | purchase from the site without having to create an account  | check out quickly and easily.                                                             | Users can use the checkout without registering for an account                                  | Pass   |
| Searching products            |                   |                                                             |                                                                                           |                                                                                                |        |
| 10                            | User/Shopper      | search for specific products                                | find books related to the keyword researched for.                                         | Users can search, on the site for products and if no product available message to confirm this | Pass   |
| 13                            |                   | easily understand the search results                        | quickly decide which book interests me.                                                   | Users can search for products and quickly see how many match their criteria                    | Pass   |
| 14                            |                   | sort by price, name, category and rating                    | view a wide range and choose which book(s) I would like to purchase.                      | Users can sort by price, name and category on the books page                                   | Pass   |
| Checkout                      |                   |                                                             |                                                                                           |                                                                                                |        |
| 15                            | Shopper           | have a running total of my bag                              | stay within my budget and be aware of my delivery cost.                                   | Users can see the total in the bag icon on the navbar.                                         | Pass   |
| 16                            |                   | view my bag contents                                        | keep track of which books I have selected and how many of them.                           | Users can view their bag to see which products and quantities have been added                  | Pass   |
| 17                            |                   | adjust the quantity of books to buy                         | update the order without going back to the product page.                                  | Users can update quantities in the shopping bag successfully. see before, after                | Pass   |
| 18                            |                   | easily enter my payment details                             | checkout as quickly and easily as possible.                                               | Users can navigate the checkout form payment input easily                                      | Pass   |
| 19                            |                   | Save the information I just entered on the checkout         | Easily create an account and have my information already saved.                           | Users can save thier information, if not saved yet, on the checkout page                       | Pass   |
| 20                            |                   | view the full order before entering card details.           | check it before confirmation and make sure I have all I want to purchase.                 | The Order can be viewed on the checkout page before entering card details                      | Pass   |
| 21                            |                   | receive email notifications when I make an order            | confirm my order has been placed and refer back to.                                       | Users receive an email when they make an order                                                 | Pass   |
| Admin/Management              |                   |                                                             |                                                                                           |                                                                                                |        |
| 22                            | Store owner/Admin | add a product                                               | Sell new books in the site                                                                | Super users can add a new book                                                                 | Pass   |
| 23                            |                   | update a product                                            | change descriptions, proce, categories, and images of the books                           | Super users can edit the book's information                                                    | Pass   |
| 24                            |                   | delete a product                                            | remove books which are no longer available to be purchased. .                             | Super users can delete a book                                                                  | Pass   |


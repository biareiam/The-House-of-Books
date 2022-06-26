# House of Books - Testing documentation

*This file contains the Testing section of the [full README.md file for house of books](README.md).*

It is important to keep in mind that any email addresses used in the testing images in this document are temporary and do not belong to real users, similarly with any delivery details. [Temp-mail](https://temp-mail.org/en/) was used to generate the fake emails. 

### Automated Testing

#### Bag

 Automated testing of views was completed to:
 
    - Test the calc_subtotal function works as expected.
    - Test the bag views work correctly.
    - Test if the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the products page is accessible by name.
    - Test that the view_bag view works correctly.
    - Test that the add to bag view works as expected.
    - Test that the add_to_bag function adds the item to the bag.
    - Test that the add_to_bag view adds the product to the bag.
    - Test that the add_to_bag view increases the quantity of an item if the item is already present in the shopping bag.
    - Test that the adjusted bag view works as expected to calculate total.
    - Test that the add_to_bag view updates the quantity of an item if the item is already in the bag.
    - Test remove from bag view removes the product from the bag.
    - Test that the remove_from_bag view removes an item from the bag.
    - Test that the remove from bag view returns an error if something goes wrong.
    
**Checkout**

  Automated testing of views was completed to:
  
    - Test the checkout page loads correctly.
    - Test that the cache_checkout_data view works as expected.
    - Test if the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the products page is accessible by name.
    - Test get checkout view when items are in the bag.
    - Test error msg appears when the bag empty.
    - Test error msg appears when no stripe key.

**Check if user is authenticated then autofill the form with details**

  Automated testing of models was completed to:
  
    - Test the order model.
    - Test order line model string method.
  
  Automated testing of forms was completed to:
  
    - Test to see if a full name field is required.
    - Test to see if an email field is required.
    - Test to see if a phone number field is required.
    - Test to see if a country field is required.
    - Test to see if town_or_city field is required.
    - Test to see if street_address1 field is required.
    - Check if the field only displays certain fields.

**Profiles**

  Automated testing of views was completed to:
  
    - Test if the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the profile page is accessible by name.
    - Test if the profile form works if form is valid.
    - Test orders displayed on login to profile page.

  Automated testing of models was completed to:
  
    - Test retrieving the user profile.
    - Test the user profile string method returns the username.
    
  Automated testing of forms was completed to:
  
    - Test that none of the form fields are required.
    
**Products**

  Automated testing of views was completed to:
  
    - Test if the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the products page is accessible by name.
    - Test products display.
    - Test categories sort functionality.
    - Test that the sort functionality works.
    - Test that the search functionality works as expected.
    - Test that the search error message displays correctly.
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
  
    - Test to see if the review title field is required.
    - Test to see if a review field is required.
    - Check if the field only displays certain fields.
    - Test to see if the review title field is required.

**Home Page**

  Automated testing of views was completed to:
  
    - Test if the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the home page is accessible by name.
    - Test if the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the privacy page is accessible by name.
    - Test if the url works when loading the page.
    - Test the correct template loads on page load.
    - Test the terms and conditions page is accessible by name.

### Manual Testing

**Browsers**

The site was tested on:
- Safari
- Google Chrome
- Firefox
- Devices Used
The site was tested on many different devices. 


| **Feature**      | **Expected**                                                             | **Testing**                  | **Result**                                                                                                            | **Pass/Fail** |
|:----------------:|:------------------------------------------------------------------------:|:----------------------------:|:---------------------------------------------------------------------------------------------------------------------:|:-------------:|
| **Home button**  | To redirect to home page                                                 | Click the home button        | Button navigates to home                                                                                              | Pass          |
| **Navbar links** | Clicking All books takes user to All books page                          | Click All books              | Redirected to All books page                                                                                          | Pass          |
|          | Clicking category takes user to the specific category page               | Click each category in turn  | Redirected to specific category page                                                                                  | Pass          |
|          | Click on bag icon and direct user to cart page                           | Click Bag                    | Redirected to cart page                                                                                               | Pass          |
|          | Click on the events link and takes user to the events page               | Click Events                 | Redirected to Events Page                                                                                             | Pass          |
|          | Searching using Search Bar displays the books in the books page          | Type "fantasy" in search bar | Redirected to a page in which the relevant results are displayed, "fantasy" in the title or on the book description.  | Pass          |
| **Footer**       | Redirect to Facebook in new tab                                          | Click Facebook icon          | Facebook page opened in new tab                                                                                       | Pass          |
|          | Redirect to Instagram in new tab                                         | Click Instagram icon         | Instagram page opened in new tab                                                                                      | Pass          |
|          | Redirect to Twitter in new tab                                           | Click Twkitter icon          | Twitter page opened in new tab                                                                                        | Pass          |
|          | Redirect to Pinterest in new tab                                         | Click Pinterest icon         | Pinterest page opened in new tab                                                                                      | Pass          |
|          | Click on T&Cs and a pop up opens with the relevant information           | Click T&Cs                   | Terms and conditions page pop up                                                                                      | Pass          |
|          | Click on Privacy Policy and a pop up opens with the relevant information | Click Privacy Policy         | Privacy Policy page pop up                                                                                            | Pass          |


### Navigation
| - When users are logged in    |                                                        |                                     |                                              |           |
|-------------------------------|--------------------------------------------------------|-------------------------------------|----------------------------------------------|-----------|
| Feature                       | Expected                                               | Testing                             | Result                                       | Pass/Fail |
| Navbar links                  | Click on Profile takes user to their profile page      | Click Profile                       | Redirected to Profile Page                   | Pass      |
|                               | Click Log Out and logs out the user                    | Click Log Out, it logs out the user | User logged out and redirected to books page | Pass      |
|                               | Click on the bag icon and is directed to the bag page  | Click bag icon                      | Redirected to the bag page                   | Pass      |
|                               | Click on My Events takes user to the events saved page | Click My Event                      | Redirected to the My Events page             | Pass      |
| - When user are not logged in |                                                        |                                     |                                              |           |
| Feature                       | Expected                                               | Testing                             | Result                                       | Pass/Fail |
| Navbar links                  | Click Log In redirects to log in page                  | Click Log In                        | User redirected to Log In Page               | Pass      |
|                               | Click Register redirects to log in page                | Click Register                      | User redirected to Register Page             | Pass      |
|                               | Click on the bag icon and is directed to the bag page  | Click bag icon                      | Redirected to the bag page                   | Pass      |

### Home Page
| Feature               | Expected                                                                                                    | Testing              | Result                                                    | Pass/Fail |
|-----------------------|-------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------|-----------|
| See more              | Clicking on the see more button and be redicted to the books page                                           | Click see more       | Redirected to the products page                           | Pass      |
| See more (categories) | Click on see more on the category banner and be direct to the book page from that category.                 | Click see more       | Redirected to the products page from an specific category | Pass      |
| All categories        | Click on the "all categories" button and be directed to the books page where all the categories are present | Click all categories | Redirected to the products page with all the categories   | Pass      |
| All books             | Click on the "all books" button and be directed to the all books page.                                      | Click all books      | Redirected to the products page                           | Pass      |

### Register Page
| Feature                | Expected                                                                           | Testing                                                             | Result                                                     | Pass/Fail |
|------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------|-----------|
| Register functionality | Form validation for email requires @ symbol                                        | Attempt to register without @ in input field                        | Form validation requests valid email address               | Pass      |
|                        | E-mail Again value must be same as Email value                                     | Attempt to register with incorrect email in email again input field | Form validation requests email address must match          | Pass      |
|                        | Username must be between 4 and 15 characters                                       | Attempt to enter username with less than 4 characters               | Feedback error displayed                                   | Pass      |
|                        | Username must be between 4 and 15 characters                                       | Attempt to enter username with more than 15 characters              | Form restricts the user from using more than 15 characters | Pass      |
|                        | Password must be longer than 8 characters                                          | Attempt to enter password with less than 8 characters               | Form restricts the user from using less than 8 characters  | Pass      |
|                        | Register with new user and password to be logged in and redirected to Profile page | Enter email address, name, username, password and click register    | New account registered and profile page shown              | Pass      |

### Log In Page
| Feature              | Expected                                                                                    | Testing                                           | Result                                                                              | Pass/Fail |
|----------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------|-----------|
| Log in functionality | Correct user/pass combination directs user to their profile page with name displayed in tab | Log in with correct username/password combination | Redirected to user profile page with name displayed in tab                          | Pass      |
|                      | Incorrect username/password combination shows error message                                 | Attempt to log in with incorrect credentials      | "The username and/or password you specified are not correct." error message appears | Pass      |
| Link to Register     | Redirect to Register page                                                                   | Click link to register                            | Redirected to Register page                                                         | Pass      |

### Profile Page
| Feature              | Expected                                                           | Testing                                                                          | Result                                                              | Pass/Fail |
|----------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------|-----------|
| Personal Information | Personal information is visible if previously saved                | Navigate to Profile page, view personal information                              | The personal information is visible in Personal Information section | Pass      |
|                      | Personal information can be updated                                | Navigate to Profile page, change personal information, click update information. | The personal information is updated with the new details.           | Pass      |
| Order History        | Order History is visible if order placed while logged in           | Navigate to Profile page, view Order History Section                             | The Order History is visible                                        | Pass      |
|                      | Order information can be accessed by clicking on the "view" button | Navigate to Profile page, view Order History Section, click on "View" button     | Order Information is visible                                        | Pass      |   |

### Books Pages

| Feature           | Expected                                             | Testing                                     | Result                                         | Pass/Fail |
|-------------------|------------------------------------------------------|---------------------------------------------|------------------------------------------------|-----------|
| All books visible | The books page shows all the available books         | Open the books page and view all the books  | All books visible                              | Pass      |
|                   | Searching by category shows books from that category | Select to search by each category           | Book from each category successfully displayed | Pass      |

### Book Details
| Feature         | Expected                                                                      | Testing                                                                 | Result                                                                                 | Pass/Fail |
|-----------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------|
| Book Details    | Book description, among other informations are displayed for individual books | Open Book Detail page and view the book's information                   | Books details visible                                                                  | Pass      |
| Add to bag      | Clicking Add to bag adds the book to the bag                                  | Open Book Detail page click add to bag                                  | Book displayed in the bag                                                              | Pass      |
| Add Product     |                                                                               |                                                                         |                                                                                        |           |
| Feature         | Expected                                                                      | Testing                                                                 | Result                                                                                 | Pass/Fail |
| Add new books   | Only admin is allowed to visit add a new book                                 | Log in as non-superuser and attempt to access /products/add/            | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass      |
| Form Validation | Required fields must be completed to add the product                          | Attempt to add product without filling in a required field              | Error message "Please fill in this field"                                              | Pass      |
| Edit Product    |                                                                               |                                                                         |                                                                                        |           |
| Feature         | Expected                                                                      | Testing                                                                 | Result                                                                                 | Pass/Fail |
| Edit books      | Only admin is allowed to visit edit a book's information                      | Log in as non-superuser and attempt to access /products/<item_id>/edit/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass      |
| Form Validation | Required fields must be completed to edit the product                         | Attempt to edit product without filling in a required field             | Error message "Please fill in this field"                                              | Pass      |

### Events Pages
| Feature        | Expected                                                 | Testing                                      | Result             | Pass/Fail |
|----------------|----------------------------------------------------------|----------------------------------------------|--------------------|-----------|
| Events         | The events page shows all the upcoming and past events.  | Open the events page and view all the events | All events visible | Pass      |
|                |                                                          |                                              |                    |           |
| Events Details |                                                          |                                              |                    |           |
| Feature        | Expected                                                 | Testing                                      | Result             | Pass/Fail |

### Event Details
| Feature       | Expected                                                                         | Testing                                                    | Result                | Pass/Fail |
|---------------|----------------------------------------------------------------------------------|------------------------------------------------------------|-----------------------|-----------|
| Event Details | Event description, among other informations are displayed for individual events. | Open an Event Detail page and view the event's information | Event details visible | Pass      |

### Add Event
| Feature         | Expected                                           | Testing                                                   | Result                                                                                 | Pass/Fail |
|-----------------|----------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------|-----------|
| Add new events  | Only admin is allowed to visit add a new event     | Log in as non-superuser and attempt to access /event/add/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass      |
| Form Validation | Required fields must be completed to add the event | Attempt to add event without filling in a required field  | Error message "Please fill in this field"                                              | Pass      |                                                                   

### Edit Events
| Feature         | Expected                                                       | Testing                                                                | Result                                                                                 | Pass/Fail |
|-----------------|----------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------|
| Edit events     | Only admin is allowed to visit and edit an event's information | Log in as non-superuser and attempt to access /events/<event_id>/edit/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass      |
| Form Validation | Required fields must be completed to edit the event            | Attempt to edit event without filling in a required field              | Error message "Please fill in this field"                                              | Pass      |

### Bag
| Feature      | Expected                                                                     | Testing                                                                | Result                        | Pass/Fail |
|--------------|------------------------------------------------------------------------------|------------------------------------------------------------------------|-------------------------------|-----------|
| View Items   | Correct books are in the bag                                                 | Add book to bag, check quantity and total on the bag                   | Expected books are in the bag | Pass      |
| Update Items | Update the number of a books in the bag and it will reflect in bag and price | Change number of books in bag and check quantity and total has updated | Total and quantity updated    | Pass      |
| Remove Items | Click on the remove icon for item to be removed from the bag                 | Click remove beside relevant book                                      | Item removed from bag         | Pass      |

### Checkout
| Feature         | Expected                                      | Testing                                                  | Result                                    | Pass/Fail |
|-----------------|-----------------------------------------------|----------------------------------------------------------|-------------------------------------------|-----------|
| View Items      | Correct books are in the checkout             | Add book to bag, click Checkout                          | Expected books are in the checkout list   | Pass      |
| Form Validation | Required fields must be completed to complete | Attempt to check out without filling in a required field | Error message "Please fill in this field" | Pass      |



## User Stories 
- Website experience
    - As a user, I would like to see what the website is selling.
        - The website has numerous reference to being a book store.
        - The home page has a link in its main hero section directing users to the products page.

<img width="945" alt="home-page-see-more" src="https://user-images.githubusercontent.com/65717229/175826020-6e13f1c3-7b39-4939-97c7-ed6968ee15d7.PNG">

        - The homepage also display some of the books' categories. By clicking on the "see more" on the categories banner, users are direct to the product page from that specific categories.

<img width="782" alt="categories-banner" src="https://user-images.githubusercontent.com/65717229/175826160-241d3b77-c2e4-4e19-9f32-9ffa2b7b2b69.PNG">

        - The homepage also has a best selling books section, which display the top 3 most sold books. 

<img width="765" alt="most-sold" src="https://user-images.githubusercontent.com/65717229/175826230-f53dbbd6-e475-4eb7-8c5c-bb85b9d698b8.PNG">

        - The user can also select different categories from the navigation.

<img width="947" alt="categories-navmenu" src="https://user-images.githubusercontent.com/65717229/175826277-0bb3746c-9e58-4948-ba4f-8268748585c0.PNG">

    - As a user, I would like to be able to navigate the site easily.
        - The logo brings the users back to the home page from any page. 
        - The main navigation has the logo, search bar, diffrent categories, events, the account, and the cart.
        - The main navigation is then accessed by clicking the burger menu, for smaller devices.

<img width="944" alt="navmenu" src="https://user-images.githubusercontent.com/65717229/175826381-36f23c3f-6b27-4f74-9898-d3b015913bd8.PNG">

    - As a user, I would like to see some information about the terms of user and privacy policy, connect with the store through social media and subscribe to the newsletter.

<img width="754" alt="useful-links" src="https://user-images.githubusercontent.com/65717229/175826525-d61b99de-8e9a-4ef3-ade9-09ab9d7e2802.PNG">
<img width="929" alt="terms" src="https://user-images.githubusercontent.com/65717229/175826529-e4c27bed-1dff-4bac-8777-d4f4a0415359.PNG">
<img width="927" alt="privacy" src="https://user-images.githubusercontent.com/65717229/175826534-8771fd7c-6bae-4fe7-88d6-5524a61c1c35.PNG">

- Searching for items

    - As a user, I would like to see all the products the book store is selling.
        - Through the navigation bar and other buttons through the home page, users can be easily direct to the product page.

 <img width="943" alt="all-books" src="https://user-images.githubusercontent.com/65717229/175826696-66953c1a-f1d1-4604-8ae8-4c20fd2799b9.PNG">   

    - As a user, I would like to be able to search by category and see the available books.
        - The navigation menu contains a link for each category.
        - The user can also click on the categories from an specific category and filter it to a particular category.

<img width="943" alt="categories" src="https://user-images.githubusercontent.com/65717229/175826778-d405a00b-ca91-45a5-94ec-2d97bc45f906.PNG">
<img width="930" alt="cat" src="https://user-images.githubusercontent.com/65717229/175826781-0d89f3af-305d-4170-8fd7-5325104d1eeb.PNG">

    - As a user, I would like to be able to search through the items.
        - The navigation menu has a search form that the user can use to search through the site's products.

 <img width="926" alt="love" src="https://user-images.githubusercontent.com/65717229/175826870-e7410b2a-ed61-47b8-94eb-bcf14941e4fb.PNG">

    -   As a user, I would like to have different sort options. 
        - The all items page has a select input to allow the items to be sorted by price.

<img width="896" alt="sort" src="https://user-images.githubusercontent.com/65717229/175826987-c55110a8-150a-472a-ab79-87a013fe64c3.PNG">

- Shopping

    - As a user, I would like to see the product price and description, among other informations.
      - Upon clicking on an book image, the user is brought to the book page where the book's price and description are shown.

<img width="642" alt="product-detail" src="https://user-images.githubusercontent.com/65717229/175827093-09f2c786-fca9-48bf-9032-627b55c853fe.PNG">

    -  As a user, I would like to be able to add products to my shopping bag.
      - From the item page the user can click the add to bag button which will then add the item to the user's bag.

<img width="836" alt="bag" src="https://user-images.githubusercontent.com/65717229/175827141-bb91b992-4a17-4a78-b903-57a01a32b389.PNG">

    - As a user, I would like to be notified when I complete interactions with the site.
      - The user is notified with a popup message whenever they act on the site.
      - The messages confirm actions as well as warnings and alerts. eg Add to bag message.

<img width="932" alt="add-bag" src="https://user-images.githubusercontent.com/65717229/175827138-f6c2d459-c2e5-4d5c-9f77-4fcd9c74cf28.PNG">

    - As a user, I would like to be able to edit my shopping bag.
      - From the bag page the user can alter the quantity or a particular item in their bag.
      - They can also delete an item if they wish to.

<img width="836" alt="bag" src="https://user-images.githubusercontent.com/65717229/175827260-c98d541e-2e0e-45f8-8dbe-ad3062cddc0f.PNG">
<img width="940" alt="over-price" src="https://user-images.githubusercontent.com/65717229/175827261-df4ffff8-3804-4ee6-804b-e796a7928bc9.PNG">

    - As a user, I would like to be able to checkout easily.
      - Once the user has an item in their bag, they can then click on the checkout button to be taken to the checkout screen.
      - Once in the checkout the user then fills out a simple form and enters their card details.
      - Once this form is valid the checkout process will then be complete.
  
<img width="486" alt="checkout" src="https://user-images.githubusercontent.com/65717229/175827338-ebb13d8e-721d-4c70-8a14-b399060c7ea0.PNG">

    - As a user, I would like to receive confirmation of my order.
      - Once the user submits an order and it has been confirmed they will then be sent a confirmation email containing the order details.

<img width="467" alt="checkout-done" src="https://user-images.githubusercontent.com/65717229/175827472-38742795-e421-479f-b4ca-57bd1811ce59.PNG">
<img width="517" alt="order-done" src="https://user-images.githubusercontent.com/65717229/175827474-f3882ce3-94c7-47d4-a2f7-6ec7e475d124.PNG">
<img width="579" alt="confirmation" src="https://user-images.githubusercontent.com/65717229/175827477-c2765952-0cca-43b6-9ee1-28cb77b2e57d.PNG">

- Account

    - As a user, I would like to save my details to an account.
      - The user can click the save details button when checking out to save their details.
      - When the user signs up they can also save their details on the user profile page for future shopping.

        - Unlogged in user
<img width="243" alt="login-checkout" src="https://user-images.githubusercontent.com/65717229/175827579-362ab335-31a5-439f-aaab-644452755ecc.PNG">

        - Logged in user
<img width="255" alt="saved" src="https://user-images.githubusercontent.com/65717229/175827620-8eec4278-f749-4dd5-9fac-fa035ccbf68b.PNG">


    - As a user, I would like to see my previous order details.
      - On the user's profile page there is a list of the user's previous orders.
      - When the user clicks on an order number they will be brought to the previous order page with its details.

<img width="532" alt="history-order" src="https://user-images.githubusercontent.com/65717229/175827669-ccf21b49-8129-4195-bc15-ec5484de7398.PNG">
<img width="525" alt="profile" src="https://user-images.githubusercontent.com/65717229/175827699-9c12beb8-d904-4e67-89dd-80250925af0d.PNG">


    - As a user, I would like to see the store's events.
      - The user can navigate to the events page and check upcoming and past events.

<img width="526" alt="upcoming" src="https://user-images.githubusercontent.com/65717229/175827805-cc6e9074-752f-4a93-9c01-9f8da5c0c0b7.PNG">
<img width="525" alt="past" src="https://user-images.githubusercontent.com/65717229/175827925-b0d7bdf6-495f-4af3-9966-c20ee139a4b4.PNG">

    - As a user, when loged in, I would like to save the events which I am interested in.

<img width="570" alt="save" src="https://user-images.githubusercontent.com/65717229/175828046-c64875cc-bc4e-44a7-8c88-2bb3b238b2e0.PNG">
<img width="577" alt="saved-event" src="https://user-images.githubusercontent.com/65717229/175828048-a0d80b5e-992a-4214-9db0-a1981e77a14d.PNG">

    - As a user, I would like to see the details of the events.

<img width="363" alt="detail-event" src="https://user-images.githubusercontent.com/65717229/175828090-436c550a-a91c-4e24-8582-36139cec7387.PNG">

    - As a user, I would like to see all the comments on the events.
      - user can edit and delete their own comments. 

<img width="531" alt="comment" src="https://user-images.githubusercontent.com/65717229/175828228-23c9931f-6cc0-4cf2-a655-b16b68794c0d.PNG">
<img width="494" alt="comment-2" src="https://user-images.githubusercontent.com/65717229/175828229-14c8ed0a-601a-49ed-915c-67ef93171296.PNG">


- Site owner

    - As the business owner, I would like to be able to edit and add products easily.
      - The superuser can add products from the admin section of the site.
      - They also have access to the product management page on the front end of the site.

<img width="354" alt="product managemed" src="https://user-images.githubusercontent.com/65717229/175828375-7861ea1c-c981-4ae2-85cb-867838aa1e03.PNG">
<img width="533" alt="add-product" src="https://user-images.githubusercontent.com/65717229/175828426-04d25b51-615d-4f98-99a6-b9371698276b.PNG">
<img width="530" alt="edit-detail" src="https://user-images.githubusercontent.com/65717229/175828427-4e048a51-9e29-4164-9f3c-d921da00f432.PNG">
<img width="535" alt="edit" src="https://user-images.githubusercontent.com/65717229/175828428-e35d264c-b62a-4719-961b-51340b69e2d1.PNG">

    - As the business owner, I would like to be able to delete products.
      - The items section will show buttons for the superuser to delete products.
      - A modal will ask them to confirm the deletion to prevent accidental deletion.

<img width="512" alt="delete-1" src="https://user-images.githubusercontent.com/65717229/175828632-20bc1c38-8a24-4f33-847e-cf00a4396ca0.PNG">
<img width="462" alt="delete-2" src="https://user-images.githubusercontent.com/65717229/175828633-4a232152-d56c-476a-a31c-57244bdc9731.PNG">

    - As the business owner, I would like to be able to edit and add events easily.
      - The superuser can add events from the admin section of the site.
      - They also have access to the event management page on the front end of the site.

<img width="524" alt="event-management" src="https://user-images.githubusercontent.com/65717229/175828545-68001671-9676-4d6f-a0db-b70a9f12dbc2.PNG">
<img width="513" alt="edit-event" src="https://user-images.githubusercontent.com/65717229/175828546-cb775db0-ccee-4970-afdc-361c3ade686b.PNG">
<img width="534" alt="detail-event-management" src="https://user-images.githubusercontent.com/65717229/175828547-759885cc-fb45-452e-bc0c-09f1b15e239f.PNG">

    - As the business owner, I would like to be able to delete events.
      - The items section will show buttons for the superuser to delete events.
      - A modal will ask them to confirm the deletion to prevent accidental deletion.

<img width="489" alt="delete-3" src="https://user-images.githubusercontent.com/65717229/175828703-248f4947-4553-49b7-a14b-d7fa4d51647d.PNG">
<img width="502" alt="12" src="https://user-images.githubusercontent.com/65717229/175829157-3a415229-649a-45d7-a230-3944abb310cb.PNG">

    - As the business owner, I would like to see who subscribed to the newsletter.

<img width="926" alt="newsletter" src="https://user-images.githubusercontent.com/65717229/175829065-3b4dedea-42e9-4c80-ba3b-6bd281ec3414.PNG">
<img width="899" alt="newsletter-success" src="https://user-images.githubusercontent.com/65717229/175829066-887a6a76-9878-49e2-bd0e-cfd6c498b19f.PNG">
<img width="950" alt="newsletter-success-1" src="https://user-images.githubusercontent.com/65717229/175829064-300d49c8-bfa5-46d8-9c66-5ee784147a13.PNG">

### Validation

- W3C HTML Validator Passed tests without issues
- W3C CSS Validator Passed tests without issues
- PEP8 and AUTOPEP8. Online PEP8 warned about some long lines on the settings.py. 

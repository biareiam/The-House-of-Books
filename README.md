# The House of Books
## Table of Contents

- [About](https://github.com/biareiam/The-House-of-Books#about) 
- [UX (User Experience)](https://github.com/biareiam/The-House-of-Books#ux-user-experience)
  - [User Stories](https://github.com/biareiam/The-House-of-Books#user-stories)
- [Design Choices](https://github.com/biareiam/The-House-of-Books#design-choices)
  - [Fonts](https://github.com/biareiam/The-House-of-Books#font)
  - [Colors](https://github.com/biareiam/The-House-of-Books#colours)
  - [Imagery](https://github.com/biareiam/The-House-of-Books#imagery-and-content)
  - [Wireframes](https://github.com/biareiam/The-House-of-Books#wireframes)
- [Features](https://github.com/biareiam/The-House-of-Books#features)
  - [Site Navigation](https://github.com/biareiam/The-House-of-Books#site-navigation)
  - [Features Implemented](https://github.com/biareiam/The-House-of-Books#features-implemented)
  - [Future Features](https://github.com/biareiam/The-House-of-Books#future-features)
- [Web Marketing & Business]()
  - [Responsive Design](https://github.com/biareiam/The-House-of-Books#responsive-design)
  - [Defensive Design](https://github.com/biareiam/The-House-of-Books#defensive-design)
- [Database Schema](https://github.com/biareiam/The-House-of-Books#database-schema)
- [Technologies](https://github.com/biareiam/The-House-of-Books#technologies)
  - [Languages](https://github.com/biareiam/The-House-of-Books#languages)
  - [Frameworks and Libraries](https://github.com/biareiam/The-House-of-Books#frameworks-and-libraries)
  - [Tools](https://github.com/biareiam/The-House-of-Books#tools)
- [Testing](https://github.com/biareiam/The-House-of-Books#testing)
- [Deployment](https://github.com/biareiam/The-House-of-Books#deployment)
- [Credits](https://github.com/biareiam/The-House-of-Books#credits)
  - [Code](https://github.com/biareiam/The-House-of-Books#code)
  - [Content](https://github.com/biareiam/The-House-of-Books#content)
  - [Media](https://github.com/biareiam/The-House-of-Books#media)
  - [Acknowledgements](https://github.com/biareiam/The-House-of-Books#acknowledgements)

## About

House of Books is an eCommerce site aimed at book lovers looking for their next “new adventures”. The books are divided in different genres, making it easier for users to find what they are looking for. The site is designed to be responsive and easy to navigate on a range of devices to make it easily accessible for all users.
This site was built for educational reasons and no deliveries will be fulfilled.

Link to the [site](http://houseofbooks22.herokuapp.com/)

  
## UX (User Experience)
 
### User Stories

| **User Story ID**                 | **As a/an**       | **I want to be able to...**                                 | **So that I can...**                                                                      |
|:---------------------------------:|:-----------------:|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------------:|
| **Viewing Products & Navigation** |                   |                                                             |                                                                                            |
| **1**                             | User/Shopper      | view individual products                                    | see what the books are about.                                                              |
| **2**                             |                   | be able to add, edit quantity and remove items from my cart | buy it after browsing.                                                                     |
| **3**                             |                   | see any special offers and new arrivals                     | take advantage of saving money on products I'd like to buy and be aware of new books.      |
| **4**                             |                   | view current and past events                                | see what the events are about, when and where it will happens.                             |
| **5**                             |                   | save the events into a list                                 | get back to the events in a later stage if I desire to join it,                            |
| **Registration and Accounts**     |                   |                                                             |                                                                                            |
| **6**                             | User/Shopper      | register for an account                                     | keep track of my orders and check my personal details, being able to update it if needed.  |
| **7**                             |                   | receive email confirmation upon signing up                  | verify my set up was successful.                                                           |
| **8**                             |                   | be able to reset my password in case I forget it            | regain access to my account.                                                               |
| **9**                             |                   | have the ability to log in to the site with my details      | view my orders and personal details.                                                       |
| **10**                            |                   | update my personal details.                                 | keep my personal information updated.                                                      |
| **11**                            |                   | purchase from the site without having to create an account  | check out quickly and easily.                                                              |
| **Searching products**            |                   |                                                             |                                                                                            |
| **12**                            | User/Shopper      | search for specific products                                | find books related to the keyword researched for.                                          |
| **13**                            |                   | easily understand the search results                        | quickly decide which book interests me.                                                    |
| **14**                            |                   | sort by price, name, category and rating                    | view a wide range and choose which book(s) I would like to purchase.                       |
| **Checkout**                      |                   |                                                             |                                                                                            |
| **15**                            | Shopper           | have a running total of my bag                              | stay within my budget and be aware of my delivery cost.                                    |
| **16**                            |                   | view my bag contents                                        | keep track of which books I have selected and how many of them.                            |
| **17**                            |                   | adjust the quantity of books to buy                         | update the order without going back to the product page.                                   |
| **18**                            |                   | easily enter my payment details                             | checkout as quickly and easily as possible.                                                |
| **19**                            |                   | Save the information I just entered on the checkout         | Easily create an account and have my information already saved.                            |
| **20**                            |                   | view the full order before entering card details.           | check it before confirmation and make sure I have all I want to purchase.                  |
| **21**                            |                   | receive email notifications when I make an order            | confirm my order has been placed and refer back to.                                        |
| **Admin/Management**              |                   |                                                             |                                                                                            |
| **22**                            | Store owner/Admin | add a product                                               | add new books to the site.                                                                 |
| **23**                            |                   | update a product                                            | change descriptions, price, categories, and images of the books.                           |
| **24**                            |                   | delete a product                                            | remove books which are no longer available to be purchased.                                |
| **25**                            |                   | add events                                                  | let users know about upcoming events.                                                      |
| **26**                            |                   | edit events                                                 | change the informations regarding the events.                                              |
| **27**                            |                   | delete events                                               | remove the events, if needed.                                                              |
|

## Design Choices
 
### Font
  A unique font was used on the site - [Sora](https://fonts.google.com/specimen/Sora).
  
### Colors
  The site uses tons of blue and black. 
  
### Imagery and content
  The images used were taken from these sources as well as the books descriptions, for education purpose:
 <br>
    - [Goodreads](https://www.goodreads.com/)
     <br>
    - [Easons](https://www.easons.com/)
    
### Wireframes
  The wireframes, for desktop and mobile, were created using Balsamiq and can be found bellow:
  
![wireframe](https://user-images.githubusercontent.com/65717229/175821262-12ee826f-e121-428d-9f1f-e9fdd7199aaf.png)

  
## Features

### Site Navigation
The navigation bar displays different links depending on whether the user is logged in, logged out or a super user.

|      Link     |  Not logged in |    Logged in   |  Logged in as super user |
|---------------|----------------|----------------|--------------------------|
| Logo          |           ✓    |           ✓   |                   ✓      |
| Search bar    |           ✓    |           ✓   |                   ✓      |
| Login in      |           ✓    |          ✗    |                  ✗       |
| Register      |           ✓    |          ✗    |                  ✗       |
| Profile Page  |          ✗     |           ✓   |                   ✓      |
| Log out       |          ✗     |           ✓   |                   ✓      |
| Add Products  |          ✗     |          ✗    |                   ✓      |
| Add Events    |          ✗     |          ✗    |                   ✓      |
| My Events     |          ✗     |          ✓    |                   ✓      |


 ## Features Implemented
 
 ### Navigation - Header
- All users, logged in or not, can:
  - Navigate to home, view the different categories, special offers, and new arrivals. 
  - Create or login into their profile page.
  - Check their bag.
  - Search for a book.
- Users logged in can access:
  - Navigate to home, view the different categories, special offers, and new arrivals. 
  - Check their profile page.
  - Logout from their account. 
  - Make a search for a book.
- Super user logged in can access:
  - Navigate to home, view the different categories, special offers, and new arrivals. 
  - Product management, where they can add products to the site. 
  - Check their profile page. 
  - Make a search for a book.
- Users who are not logged in can:
  - Navigate to home, view the different categories, special offers, and new arrivals. 
  - Access register and login page.
  - Make a search for a book.
 
 ### Create Profile
- The users are able to:
  - Create a profile to store their personal information and check their order history.
  - Confirm their details are correct via email verification.

### Log in to the profile page 
- The users are able to:
  - Log in to the profile page to see their orders history and personal information.
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
  - Add, edit and delete books. 

### Products Management
- If a super user, the user can:
  - Add a book, including adding an image. In case, one is not provided, a default will be put in place. 
  - Edit the information related to the books
  - Delete a book not available for sale anymore. 

### Event Page
- All users, logged in or not, can:
  - Navigate to events, view the different events.
  - Check the events details. 
- Users logged in can access:
  - Navigate to events, view the different events. 
  - Check the events details.
  - Save/remove the events to "my events". 
  - Add comments to the events.
  - Edit or delete thier own comments.
- Super user logged in can access:
  - Navigate to events, view the different events. 
  - Product management, where they can add products to the site. 
  - Check their profile page. 
  - Make a search for a book.
- Users who are not logged in can:
  - Navigate to events, view the different events.
  - Check the events details.
  - Access register and login page.
  - See all the comments.

### Event Details Page
- The users are able to:
  - Click the events and find out more about it.
  - Read the comments.
- Users logged in can access:
  - Add/Remove events to the "My Events" session.
  - Leave a comment
- Super users are able to:
  - Add, edit and delete events. 

### Event Management
- If a super user, the user can:
  - Add an event, including adding an image. In case, one is not provided, a default will be put in place. 
  - Edit the information related to the events.
  - Delete event. 

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
  - sign up to the newsletter.

### Error pages
#### 404.html
- 404 pages created to redirect users back to the main site in case of an error.
  
#### 403.html
- 403 page created to redirect users back to the main site in case they try to access a page they are not authorized to.
  
#### 500.html
- 500 error page created to redirect users to the main site after a server error.

## Future Features
- A chat bot where users can ask questions on the site.
- The ability to add many filters to their search criteria at the same time or combine filters. 
- Give the user the ability to track their orders.
- A star rating or upvote functionality for the books.
- Add users' reviews to the site. 

## Web Marketing & Business

As part of web marketing a Facebook page was created for The House of Books.

![house](https://user-images.githubusercontent.com/65717229/175274998-7b2b56e4-6338-4ad6-8acc-c7005b647e4d.PNG)

## Responsive Design
The site was designed to be mobile first as more users are using their mobile to shop online but this has been adapted to allow the same good experience for desktop and tablet.

## Defensive Design

**Form Validation**
- Form validation has been added to every form to ensure all required information is included before submitting.
- If incorrect data is input, a warning text appears to notify the user that something is missing or gone wrong.

**Default Image if none added**
- In the event that a product is added without an image, a default image will be added. It is unlikely to happen due to the form validation, but just in case, a backup image was set.

**Unauthorized Attempts**
- An error is launched if a user attempts to visit a part of the site which they should not have access to. 

**@login_required**
- @login_required decorator added to restrict access to certain pages.
  - If a logged-out user tries to access a restricted page, they will be redirected to the login page.
  - Only authorized users may perform certain actions, such as add, edit, delete books.

**Bag**
- Validation was put into place to ensure a minimum of 0 product and maximum of 99 products is added to the bag. 
- In the case that 0 is selected the item is removed from the bag.
- Users can not add a negative number on the quantity of books to the bag.


## Database Schema
  The database uses SQL through PostgreSQL and was originally formed from fixtures categories.json and products.json.The Datamodel schema is below :
  
  ![data scheme](https://user-images.githubusercontent.com/65717229/175821121-a1c6f9c6-58cc-4c2c-9287-68eb0f1507b5.png)

### Database
- Postgres
- SQLite
    - Cloud based database to hold the product, user, and order fields.

 ## Technologies
 
 ### Languages
 
- HTML
- CSS
- JavaScript
- Python (with Django framework) and Django templating language

 ### Frameworks, Libraries, Programmes and Tools
- Balsamiq was used to design the wireframes of the site. 
- Panda Library is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language. It was used to create the most sold books section on the home page. 
- tiny png was used to compress the images of the books, among others.
- AWS to host media and static files.
- To handle payments, Stripe was used. It is currently only set up to handle test payments.
- Bootstrap v4.4.1 was used for responsiveness, layout, modals, and general styles on the frontend.
- django-allauth was used for user registration and authentication.
- Django countries was used to create a countries dropdown list in checkout form.
- Bootstrap Icons were used for the icons used throughout the site.
- W3C HTML validator to validate the HTML code
- W3C CSS Validator to validate the CSS code
- PEP8 checker to validate the Python code
- "Privacy Policy" and "Terms and Conditions" Generators were used to create this useful links.
-  Generator to make the Terms of Use document
- Mailchimp was used for the newsletter sign up form in the site footer.
- Facebook was used to create the Facebook business page.
- XML-Sitemaps.com was used to generate the sitemap.
- Lucidchart was the tool used to create the ER diagram.
 
**Git** 
  - Git was used for version control (commit to Git and push to GitHub).
  
**GitHub**
  - Used to store, host and deploy the project files and source code after being pushed from Git. I also used it for the Project Kanban board to keep track and split tasks into smaller tasks to make them easier to fulfill.
  
## Testing

The testing can be seen [here](testing.md).

### Deployment

#### Gitpod Workspaces

1. Starting from GitHub clone the Code Institute template by clicking Use This Template and copying to my repository under the name biareiam. The workspace is then launched by clicking GitPod - this action only needs to be performed once and then workspace reopened from GitPod.
2. Start the Gitpod Workspace which opens an online IDE editor window.

#### Gitpod branching and committing to GitHub

**Deploying to Heroku**

The project has been deployed to Heroku and AWS. The steps for deployment were:
 
- Create an account in Heroku;
- Create a new app in Heroku: choose a unique name and region;
- On the resources tab provide a new Postgres database (used free plan for this project);
- Go back to gitpod and install dj_database_url and psycopg2 and freeze the requirements in requirements.txt file to ensure Heroku installs our apps requirements when we deploy;
- In settings.py import dj_database, comment out the default database configuration, replace it with a call to dj_database_url.parse and give it the database URL from Heroku (which can be found in the settings tab);
- Migrate all the changes;
- Import all the books, categories and subcategories using the command 'python3 manage.py load “data name”';
- Create a super user using command 'python3 manage.py createsuperuser' and follow terminal instructions;
- Create an if statement in settings.py to allow the system to take the database from os.environ if it exists otherwise it will use the default configuration.
- Create a Procfile to tell Heroku to create a web dyno;
- Temporarily disable collect_static using command 'heroku config:set DISABLE_COLLECT_STATIC=1';
- In settings.py add the hostname of the heroku app and a localhost so that gitpod will keep working;
- Deploy to Heroku;
- In Heroku, inside the app, go to the Deploy tab and set it to deploy to github, search for the project repository and click connect. Once connected set up automatic deploys (due to recent issues shared by the Heroku team automatic deploys have been temporarily disabled);
- Generate a secret key for the Heroku app and add it to the env.py file (which is included in .gitignore file to keep all the keys secret and safe);
- In settings.py set up debug to true only if there is a variable called development in the environment;

**Deployment to AWS S3**:
- Navigate to https://aws.amazon.com/ and create an account;
- Once logged in, from the AWS Management Console page, find the S3 service in the 'Find Services' search bar to create a new bucket where our files will be stored;

Create a bucket:

- With a matching name with your app to keep things organized;
- Select your closest region;
- Uncheck 'block all public access' and acknowledge that the bucket will be public;
- Under Bucket Ownership section select 'ACLs enabled';
- Select Create Bucket;

Inside our new bucket:
- In the properties tab turn on static website hosting to create a new endpoint accessible from the internet;
- In the permissions tab we will make 3 changes:
  - Paste in new CORS Configuration: [ { "AllowedHeaders": [ "Authorization" ], "AllowedMethods": [ "GET" ], "AllowedOrigins": [ "*" ], "ExposeHeaders": [] } ]
- In the policy tab click on policy generator and create a new policy and copy it in the policy editor and before saving add /* at the end of the resource key to allow access to all resources in the bucket;
- In the Access Control List tab click edit and enable List for Everyone (public access) and accept the warning box;
- Now that the bucket is ready, we need to create a user to access it, we will create through the service called IAM (Identity Access Management):
  - Access IAM through the Services menu;
- Click User Groups on the side menu and click Create New Group and call it manage-houseofbooks-v3 (to match our website again and have consistency) and click on Create Group;
- On the side menu click on Policies and then click on Create Policies;
- In the JSON tab select 'import managed policy' which will let us import the 'S3 Full Access Policy' that AWS has pre-built for full access to S3. But because we only want to allow full access to our bucket we need to get the bucket ARN from the bucket policy page in S3 and paste it under Resource as a list. We will paste twice, the first item is the ARN as it is and the second item with /* at the end to add another rule for all files and folders in the bucket;
- Click review policy, give it a name and description and click Create Policy;
- To attach the policy to the group we created click on User Groups, select manage-houseofbooks-v3, click Attach Policy, search policy created, select it and click Attach Policy;
- Now we need to create a user to put in the group: click Users in the sidebar menu;
- Create the user houseofbooks-v3-staticfiles-user, select Programmatic Access and select Next;
- From the list provided select manage-houseofbooks-v3 and click Create User;
- Click on 'Download .csv' which will contain the users access key and secret access key that we will use to authenticate them from our Jango app. It is very important you download and save this CSV file as it won't be downloadable again after this process.
- Configure Django to connect to S3 using the keys we just created:
- In settings.py file, under the Static Files section create an IF statement to check if there is an environment variable called USE_AWS in the environment;
- In the IF statement define the AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, access key and secret access key we will get from the environment to keep them secure;
- In Heroku, in the Config Vars section of the Settings tab:
- Add the AWS keys;
- Set USE_AWS to True;
- Remove the DISABLE_COLLECTSTATIC variable;
- In settings.py in gitpod set up the bucket name;
- Create a new file called custom_storages.py:
- Import settings from django and s3boto3 storage class from django storages;
- Create a new class called static_storages that inherits from django s3boto3;
- Tell the class that we want to store static files in a location from the settings that we'll define in a moment;
- Create an exact same class but for media;
- In settings.py and set a variable that points to the new storage classes we just created and that the location it should save static files is a folder called 'static'. Do the same for media files;
- Now we need to override and explicitly set the URLs for static and media files using our custom domain and the new locations.
- Deploy to Heroku. Once the deployment to Heroku is successful, if we go to S3, we can see that we have a static folder in our bucket with all our static files in it. Basically, what is happening now, when our project is deployed to Heroku, it will run python3 manage.py collectstatic during the build process and will search through all the apps and project folders looking for static files. It will use the S3 custom domain setting with our custom storage classes that will tell the location where we want to save things. This means that when USE_AWS is set to TRUE, whenever collectstatic is run, static files will be collected into a static folder in our s3 bucket;
- Go to S3 and create a new folder called 'media', inside this folder click 'upload', 'add files' and then select all the book cover images.

Stripe:
- Add all the Stripe keys to the Heroku Config Variables;
- Create a new Stripe wehbhook endpoint using the new address: http://houseofbooks22.herokuapp.com/;
- Test the webhook is working correctly by creating and test order through our new deployed site in Heroku;

if you can not deploy through Heroku, it is possible to do it through Gitpod.

#### How to run the project locally
To clone this project from GitHub follow the instructions taken from GitHub Docs explained here:
  
1. Navigate to the GitHub Repository
2. To clone using HTTPS click the clipboard symbol under "Clone with HTTPS". To clone using SSH key click Use SSH then click the clipboard symbol. To clone using GitHub CLI select Use GitHub CLI and click the clipboard symbol.
3. Open Git Bash
4. Change the working directory to the location you want the cloned directory to be.
5. Type 'git clone' and paste the url copied from step 3.
6. Press 'enter' to create your clone.

### Credits
#### Code
- A good portion of the Django, Python and JavaScript code was developed following the Code Institute's Boutique Ado walkthrough.
- CodeInstitute Full Stack Developer Course.
- Code from - https://mdbootstrap.com/docs/standard/components/carousel/ - was used as inspiration for the creation of the carousel of the home page. 
- Code from - https://mdbootstrap.com/docs/standard/components/carousel/ - was used as inspiration to create the footer.
- Code from https://stackoverflow.com/questions/55023534/how-to-get-10-of-the-best-seller-selling-products-in-django was used as an inpsiration to create the most sold books on the home page. 
- Code from https://www.geeksforgeeks.org/e-commerce-website-using-django/ was used as an inpsiration to create the ecommerce site. 
- Code from https://www.educative.io/answers/what-are-built-in-error-views-in-django was used as an inpsiration to create the error pages. 

    
#### Content
  - Terms and conditions, privacy page sources from https://www.termsfeed.com/
  
#### Media
  - All the book images and descriptions were sourced from Goodreads and Easons. 
  - All the events images werefrom Pexel.com

#### Acknowledgements

Thanks to my friend Authur Pereira Neto for all the support and help throughout this project, and the Slack groups.

Disclaimer
If there are any issues with the copyright of the content, please contact me. I will fix that as soon as possible. This project is for educational purposes only.

Beatriz Amorim



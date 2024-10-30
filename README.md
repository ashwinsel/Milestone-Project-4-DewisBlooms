### Dewi's Blooms - Florist E-commerce Project
###### Code Institute / Full-Stack Development / Milestone Project
------------

[View Live Project Here](#)

As part of this project for **Full-Stack Development**, we are building **Dewi's Blooms**, a florist website that allows users to browse a variety of floral products, manage accounts, save special occasions for family and friends, and make purchases using a secure payment system powered by **Stripe**.

This project is designed to offer users an easy, enjoyable experience while buying flowers, setting reminders for special dates like birthdays and anniversaries, and getting personalized recommendations based on preferences. The aim is to create a responsive, user-friendly platform that integrates **Bootstrap** for styling, **Django** for backend functionality, and **django-allauth** for user authentication.

![Screenshot](#)

## **Index - Table of Contents**
------------

+ [User Experience (UX)](#-user-experience-ux)
    * [User Stories](#user-stories)
        - [First Time Visitor Goals](#a-first-time-visitor-goals)
        - [Returning Visitor Goals](#b-returning-visitor-goals)
        - [Frequent User Goals](#c-frequent-user-goals)       
+ [UX Planes](#ux-planes)
    * [Strategy](#strategy)
        - [Project Goals](#project-goals) 
        - [Customer Goals](#customer-goals)
        - [Company Goals](#company-goals)
        - [Future Implementations](#future-implementations)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)     
    * [Surface](#surface)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
        - [Imagery](#imagery)
+ [Features](#features)
    * [Homepage](#homepage)
    * [Shop Page](#shop-page)
    * [Shopping Cart](#shopping-cart)
    * [Checkout](#checkout)
    * [User Account](#user-account)
    * [Special Dates & Reminders](#special-dates-reminders)      
+ [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
+ [Testing](#testing)
    * [Validator Testing Results](#validator-testing-results)
    * [Browser Compatibility](#browser-compatibility)
+ [Deployment](#deployment)
+ [Credits](#credits)
    * [Content](#content)
    * [Code](#code)
    * [Media](#media)
+ [Gratitude](#gratitude)

---

## **User Experience (UX)**
------------

### **User Stories**

1. **As a/an user/shopper** (the type of user)
2. **I want to be able to...** (the functionality the user desires)
3. **So that I can...** (the benefit or reason the user wants the feature)

| **App Function**                   | **As a/an user/shopper**       | **I want to be able to...**                                 | **So that I can...**                                        |
|-------------------------------------|--------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| **1. Viewing and Navigation**       | Shopper                        | Browse flowers and floral arrangements                       | See the available products for purchase                     |
|                                     | Shopper                        | View detailed product pages                                  | Learn more about each product, including price and details   |
|                                     | Shopper                        | Navigate between categories (e.g., bouquets, single flowers)  | Easily find the type of flowers I’m looking for              |
|                                     | Shopper                        | See featured products on the homepage                        | Quickly find popular or seasonal products                   |
|                                     | Shopper                        | Use a main navigation menu to move between sections (shop, cart, etc.) | Easily access different parts of the site                   |
|                                     | Shopper                        | View a responsive layout on mobile and desktop               | Have a seamless experience no matter which device I use      |
| **2. Registration and User Accounts** | Shopper                        | Register for an account                                      | Save my information for faster future purchases              |
|                                     | Shopper                        | Log in to my account                                         | Access my saved preferences, orders, and contact dates       |
|                                     | Shopper                        | Save friends' and family members’ special dates (e.g., birthdays, anniversaries) | Get reminders to send gifts for important occasions          |
|                                     | Shopper                        | Manage my profile (e.g., update address, email, password)    | Keep my information up to date                               |
|                                     | Shopper                        | View my past orders                                          | Easily reorder items for recurring gifts                    |
|                                     | Shopper                        | Log out of my account                                        | Ensure my account is secure                                 |
| **3. Sorting and Searching**        | Shopper                        | Filter products by category (e.g., bouquets, arrangements)   | Quickly find products that match my preferences              |
|                                     | Shopper                        | Search for products using keywords                           | Locate a specific flower or arrangement                      |
|                                     | Shopper                        | Sort products by price (low to high, high to low)            | Find items within my budget                                 |
|                                     | Shopper                        | Sort products by occasion (e.g., Valentine’s Day, birthday)  | Choose products relevant to the event I'm shopping for       |
|                                     | Shopper                        | Sort by availability (in stock, out of stock)                | See only the products I can order immediately                |
|                                     | Shopper                        | Sort by color or flower type                                 | Find items in specific colors or types for a personalized gift|
| **4. Purchasing and Checkout**      | Shopper                        | Add products to a shopping cart                              | Save items I’m interested in purchasing                      |
|                                     | Shopper                        | View my shopping cart before checkout                        | Review my order before completing the purchase               |
|                                     | Shopper                        | Select a delivery date during checkout                       | Schedule deliveries for special occasions in advance         |
|                                     | Shopper                        | Apply discount codes at checkout                             | Save money with promotions or coupons                       |
|                                     | Shopper                        | Enter shipping and billing information during checkout       | Provide the necessary details for my order to be processed   |
|                                     | Shopper                        | Pay for my order securely using Stripe                       | Complete my purchase with confidence that my payment is safe |
|                                     | Shopper                        | Receive a confirmation email after ordering                  | Know that my order has been successfully placed              |
|                                     | Shopper                        | Save my payment information for future purchases             | Speed up the checkout process on future orders               |
| **5. Notifications and Reminders**  | Shopper                        | Receive reminder emails for special dates                    | Get notified before important dates like birthdays or holidays|
|                                     | Shopper                        | Get promotional emails for holidays (e.g., Valentine’s, Christmas) | Take advantage of special offers on flowers for major events |
|                                     | Shopper                        | Get a reminder when I have abandoned my shopping cart        | Complete my purchase if I forgot to check out                |

---

### Summary of User Stories

- **Viewing and Navigation** focuses on user interaction with the product catalog, ensuring ease of access to various sections of the site and product details.
- **Registration and User Accounts** enables users to register, log in, and manage their profiles, orders, and important dates for personalized experiences.
- **Sorting and Searching** helps users quickly find products based on specific criteria like price, category, or availability.
- **Purchasing and Checkout** ensures that the user can add products to their cart, select a delivery date, and pay securely using Stripe.
- **Notifications and Reminders** enhances user experience by sending emails for upcoming occasions and special promotions.
 

- #### A. First Time Visitor Goals
    1. As a first-time visitor, I want to easily browse through different floral products.
    2. As a first-time visitor, I want to understand how to add items to my cart and complete a purchase.
    3. As a first-time visitor, I want to be able to register for an account and receive special offers or reminders for occasions.
    4. As a first-time visitor, I want to navigate a clean, visually appealing layout, ensuring that all features are accessible.
    5. As a first-time visitor, I want the site to load quickly and work smoothly on my device.

- #### B. Returning Visitor Goals
    1. As a returning visitor, I want to log into my account and view my saved special dates (e.g., birthdays, anniversaries).
    2. As a returning visitor, I want to quickly reorder my favorite flowers from past purchases.
    3. As a returning visitor, I want to see any promotions or new products.
    4. As a returning visitor, I want to manage my personal details (e.g., update my address or preferences).

- #### C. Frequent User Goals
    1. As a frequent user, I want reminders for upcoming birthdays or anniversaries so that I don’t miss any special occasions.
    2. As a frequent user, I want to store preferences for specific friends and family members so I can quickly choose the right flowers for them.
    3. As a frequent user, I want to track my order history and see delivery status.

---

## **UX Planes**
------------

- ### **Strategy**
    + #### Project Goals
        The primary goal of **Dewi's Blooms** is to provide a user-friendly platform for browsing, purchasing, and sending flowers for various occasions. The project focuses on seamless navigation, ease of use, and personalized experiences for users. 
    + #### Customer Goals
        - Allow users to browse and purchase flowers easily.
        - Provide an account system where users can save personal information and special dates.
        - Offer reminders and product recommendations based on user preferences.
    + #### Company Goals
        - Establish a robust online presence for the florist.
        - Increase sales by offering targeted promotions around special events (e.g., Valentine's Day, Mother’s Day).
        - Maintain customer engagement with email reminders and user accounts.
    + #### Future Implementations
        - Introduce a flower subscription service.
        - Offer gift cards.
        - Add social sharing features for users to recommend products to friends.

- ### **Scope**
    - The website will provide the following functionalities:
        * User-friendly product browsing with filter and search options.
        * Secure payment system using **Stripe**.
        * User accounts with personalized settings for managing special dates.
        * Reminders and promotions for specific occasions.

- ### **Structure**
    - The structure of **Dewi's Blooms** follows a logical flow:
        * **Homepage**: Highlights featured products and provides access to all major site sections.
        * **Shop Page**: Lists all products with filters for easy navigation.
        * **Account Page**: Allows users to manage their information and special dates.
        * **Checkout Page**: Secure checkout with Stripe integration.

- ### **Surface**
    + #### Colour Scheme
        - Soft pastel tones, complemented by green and floral accents, will evoke a sense of freshness and calmness.
    + #### Typography
        - Font choices include **Lora** and **Montserrat**, chosen for their readability and elegance. Standard web-safe fonts like **Arial** will serve as fallbacks.
    + #### Imagery
        - High-quality images of flowers and floral arrangements will play a key role in creating an inviting atmosphere.

---

## **Features**
------------

- ### Homepage
    - Displays featured products, quick navigation links, and a clean, welcoming layout.
    
- ### Shop Page
    - Allows users to browse through all available flowers and products, filter by category (e.g., roses, bouquets), and sort by price.
    
- ### Shopping Cart
    - Users can review their selected products, update quantities, and proceed to checkout.

- ### Checkout
    - Secure checkout page with Stripe integration for handling payments. Users can enter shipping information and select delivery dates.

- ### User Account
    - Allows users to register and log in using **django-allauth**. Users can view their order history, manage personal information, and save preferences.

- ### Special Dates & Reminders
    - Users can save special dates (e.g., birthdays, anniversaries) and get email reminders ahead of those dates, suggesting products based on their saved preferences.

---

## **Technologies Used**
------------
- ### **Languages Used**
    * **HTML5**
    * **CSS3**
    * **JavaScript**
    * **Python3** (Backend using Django)
  
- ### **Frameworks, Libraries, and Programs Used**
    * **Django**: Backend framework to manage user authentication, database interactions, and page routing.
    * **django-allauth**: Used for user registration, login, and account management.
    * **Stripe**: For secure payments.
    * **Bootstrap5**: For responsive design and easy-to-use UI components.

---

## **Testing**
------------
+ ### Validator Testing Results
    - All HTML and CSS files were validated using the W3C Validator to ensure code quality.
  
+ ### Browser Compatibility
    - The website has been tested on various browsers (Chrome, Firefox, Safari) and devices (desktop, tablet, mobile) for responsiveness and usability.

---

## **Deployment**
------------
+ The project is deployed using **Heroku**.
+ Instructions for deploying and cloning the project:
    - Clone the repository from GitHub.
    - Set up a virtual environment.
    - Install required dependencies from `requirements.txt`.
    - Set up environment variables for **Stripe** and **django-allauth**.
    - Deploy to **Heroku** or similar platforms.

---

## **Credits**
------------
+ ### **Content**
    - All written content is original and tailored for the **Dewi's Blooms** project.

+ ### **Code**
    - Custom code for the backend was written using **Django**. Tutorials and documentation were referenced from **Django** and **Stripe** official sites.

+ ### **Media**
    - All images used for product listings are either sourced from the business or licensed for use.

---

## **Gratitude**
------------
I would like to thank **Code Institute** for their guidance in developing this project. Special thanks to mentors and peers for their invaluable feedback and support throughout the project.

--- 

This README has been tailored to reflect the unique goals and structure of **Dewi's Blooms**, a full-stack project combining **Django**, **Stripe**, **Bootstrap**, and **django-allauth**.
Database Schema Structure
Category Table

Fields:
id (Primary Key)
name (Unique Identifier for the category, e.g., "occasions", "seasonal", "type")
friendly_name (User-friendly name, e.g., "Occasions Flowers")
Product Table

Fields:
product_id (Primary Key)
sku (Stock Keeping Unit for tracking)
category_id (Foreign Key referring to Category.id)
name (Product name, e.g., "Anniversary Bouquet 0")
description (Description of the product, e.g., "Beautiful anniversary bouquet.")
price (Price of the product, e.g., "45.00")
rating (User rating, e.g., 4.6)
image_url (URL to the product image)
Relationships

One-to-Many: A Category can have multiple Product entries associated with it through the category_id foreign key.
This schema allows each product to be associated with a specific category, enabling filtering by category, as well as displaying product details such as name, price, rating, and image. 
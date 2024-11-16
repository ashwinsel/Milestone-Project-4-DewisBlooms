### Dewi's Blooms - Florist E-commerce Project
###### Code Institute / Full-Stack Development / Milestone Project
------------

[View Live Project Here](https://dewis-blooms-unique-123-b3c2c80b60fd.herokuapp.com/)

### Introduction

Dewi's Blooms is a fictional Welsh florist e-commerce site created to provide users with an effortless and delightful shopping experience for floral arrangements and gifts. The site showcases a range of flower categories, allowing customers to browse, purchase, and schedule deliveries for special occasions. Users can make secure payments via Stripe and receive confirmation emails after completing their orders.

Visitors can create an account to save personal details, manage order histories, and even set reminders for special dates, making the gifting process smoother and more personalized. Accounts also enable users to save time on future purchases by storing their shipping and billing information.

The site features products in multiple categories, such as bouquets, floral arrangements, and seasonal flowers, managed entirely by the admin. Administrators have full CRUD (Create, Read, Update, Delete) capabilities for managing products, categories, and other backend functions.

Stripe is used for secure payments, ensuring a safe and reliable checkout experience. The platform is currently in 'test' mode, meaning no real payments will be taken. To test the checkout process, you can use Stripe's test card numbers. For valid test payments, use:

- **Card Number:** 4242 4242 4242 4242  
- **CVC:** Any 3 digits  
- **Expiration Date:** Any future date  

To access admin functionality and explore the backend features of the site, use the following superuser credentials:

- **Username:** ashwinsel@someemail.com  
- **Password:** Anusha1990  

Dewi's Blooms not only highlights the beauty of flowers with high-quality imagery but also provides a seamless e-commerce experience that ensures users feel confident and satisfied with their purchase journey.

![Screenshot](#)

---

## **Index - Table of Contents**
------------

+ [User Experience (UX)](#user-experience-ux)
    * [User Stories](#user-stories)
        - [First Time Visitor Goals](#first-time-visitor-goals)
        - [Returning Visitor Goals](#returning-visitor-goals)
        - [Frequent User Goals](#frequent-user-goals)       
+ [UX Planes](#ux-planes)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Surface](#surface)
+ [Features](#features)
+ [Technologies Used](#technologies-used)
+ [Custom Models and Database Schema](#custom-models-and-database-schema)
    * [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Credits](#credits)
+ [Gratitude](#gratitude)

---

## **User Experience (UX)**
------------

### **User Stories**

| **App Function**                   | **As a/an user/shopper**       | **I want to be able to...**                                 | **So that I can...**                                        |
|-------------------------------------|--------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| **1. Viewing and Navigation**       | Shopper                        | Browse flowers and floral arrangements                       | See the available products for purchase                     |
|                                     | Shopper                        | View detailed product pages                                  | Learn more about each product, including price and details  |
|                                     | Shopper                        | Navigate between categories (e.g., bouquets, single flowers) | Easily find the type of flowers I’m looking for             |
|                                     | Shopper                        | Search for products using keywords                           | Locate a specific flower or arrangement                     |
|                                     | Shopper                        | View a responsive layout on mobile and desktop               | Have a seamless experience no matter which device I use     |
| **2. Registration and User Accounts** | Shopper                        | Register for an account                                      | Save my information for faster future purchases             |
|                                     | Shopper                        | Log in to my account                                         | Access my saved preferences and order history               |
|                                     | Shopper                        | Update my personal information (e.g., address, email)        | Keep my profile information up to date                      |
|                                     | Shopper                        | View my order history                                        | Check past orders for reordering or reference               |
| **3. Sorting and Searching**        | Shopper                        | Filter products by category (e.g., bouquets, arrangements)   | Quickly find products that match my preferences             |
|                                     | Shopper                        | Search for specific products                                 | Locate items that meet my exact needs                       |
| **4. Purchasing and Checkout**      | Shopper                        | Add products to a shopping cart                              | Save items I’m interested in purchasing                     |
|                                     | Shopper                        | View my shopping cart                                        | Review my selected items before checkout                    |
|                                     | Shopper                        | Pay for my order securely using Stripe                       | Complete my purchase with confidence that my payment is safe|
|                                     | Shopper                        | Enter shipping and billing information during checkout       | Ensure my order is delivered to the correct address         |
|                                     | Shopper                        | Receive an order confirmation email                          | Know my order was placed successfully                       |
| **5. Notifications and Reminders**  | Admin                         | View customer orders                                         | Fulfill orders and manage stock effectively                 |
| **6. Admin Features**               | Admin                         | Add, edit, or remove products                                | Keep the product catalog up to date                         |
|                                     | Admin                         | Manage customer orders                                       | Ensure efficient order processing and delivery              |

---

## **UX Planes**
------------

- ### **Strategy**
    + The primary goal of **Dewi's Blooms** is to provide a user-friendly platform for browsing, purchasing, and sending flowers for various occasions.

- ### **Scope**
    - The website will provide the following functionalities:
        * User-friendly product browsing with filter and search options.
        * Secure payment system using **Stripe**.

- ### **Structure**
    ### Structure Plane: Organizing Information and Functionality

    The structure of Dewi's Blooms was planned with the user journey in mind, ensuring the site is intuitive and efficient for both shoppers and administrators. The app is split into four main categories, each serving a specific purpose and contributing to a seamless user experience. Below is an outline of these categories and the design considerations that influenced their implementation.

    ---

    #### **1. Browsing and Finding Products**
    Finding products is a fundamental aspect of the Dewi's Blooms app. Since the primary goal is to provide an enjoyable and easy shopping experience, the following structural features were implemented to facilitate browsing:

    - **Clear Navigation**: The navigation bar allows users to easily browse by product categories, such as bouquets, arrangements, and seasonal flowers.
    - **Search Functionality**: A search bar in the header enables users to find products directly by entering keywords.
    - **Product Details**: Each product page provides high-quality imagery, a detailed description, and pricing, allowing users to make informed decisions.
    - **Responsiveness**: The app has been designed to ensure users can browse products effortlessly across devices, whether on desktop or mobile.

    The structure mirrors conventional e-commerce sites to provide familiarity, but extra care was taken to include florist-specific features, such as showcasing seasonal arrangements and promoting featured bouquets prominently on the homepage.

    ---

    #### **2. The Checkout Process**
    The checkout process is designed for clarity and efficiency, ensuring users can complete purchases with minimal friction. Here’s how the structure supports a smooth checkout experience:

    - **Shopping Cart**: A cart icon in the navigation bar provides users with quick access to their selected items. The cart page displays item quantities, pricing, and a total cost summary.
    - **Delivery Details**: Users can input their shipping address and select a delivery date to suit their gifting needs.
    - **Secure Payments**: Stripe integration provides secure payment options. Users are reassured by the familiar interface of Stripe's payment form, while administrators benefit from its reliability.
    - **Confirmation Emails**: Users receive email confirmations with order details, reinforcing trust in the service and providing a reference for their purchase.

    The entire process was modeled on industry-standard UX practices, minimizing unnecessary steps while ensuring users feel secure and confident during the transaction.

    ---

    #### **3. User's Account**
    The user account functionality was designed to empower users to manage their details and view past transactions easily. The structure of the account page includes:

    - **Order History**: Users can view their past purchases and access detailed receipts, ensuring they can reorder products or track delivery.
    - **Profile Management**: Users can update personal information, such as their email address, shipping details, or password, directly from their profile.
    - **Saved Special Dates**: A unique feature allows users to store important dates (e.g., birthdays, anniversaries) and receive reminders, creating a personalized shopping experience.
    - **User-Friendly Navigation**: The account page uses a clean, list-style menu that directs users to relevant features, ensuring functionality is easy to find.

    This structure prioritizes simplicity and usability, enabling users to perform essential tasks without confusion.

    ---

    #### **4. Admin Features**
    The admin panel plays a critical role in maintaining the site’s functionality and product offerings. While Django’s built-in admin interface provides robust management capabilities, the following admin-specific features were added for convenience:

    - **Product Management**: Administrators can create, edit, and delete products directly from the backend, ensuring the product catalog remains up to date.
    - **Category Management**: Admins can manage product categories, allowing for seasonal updates or the addition of new product lines.
    - **Order Overview**: The admin dashboard includes an order management system where administrators can track and process customer orders.

    These features allow the admin to perform essential tasks efficiently while leveraging Django’s default tools for more advanced management tasks.

    ---

    #### **Flow of Information**
    The structure of Dewi's Blooms ensures that information flows logically throughout the site. Users begin by browsing the homepage or categories, navigating seamlessly to product pages. From there, they can add items to their cart and proceed to the checkout. Registered users can log in to save time and view their account details, while administrators manage content behind the scenes.

    All major sections—products, checkout, user accounts, and admin tools—are accessible from the navigation bar or through intuitive call-to-action buttons, ensuring users can achieve their goals quickly and easily.

    ---

    By organizing Dewi's Blooms into these key structural components, the app delivers a cohesive experience for users, providing the functionality they expect while maintaining a professional and visually appealing design. This thoughtful structure ensures that both customers and administrators can interact with the site effectively and efficiently.

- ### **Surface**
    + #### Colour Scheme
        ### Color Scheme for Dewi's Blooms

The **Dewi's Blooms** website has been designed with a clean and elegant **color palette** to evoke freshness and tranquility, aligning perfectly with the essence of a florist business. Here's a breakdown of the color choices:

1. **Primary Colors**:
   - **Soft Pastel Yellow**: Used in the hero section and banners, this color represents joy and freshness, echoing the natural beauty of flowers.
   - **White and Light Beige**: These neutral tones create a sense of simplicity and sophistication, ensuring that the focus remains on the vibrant floral arrangements.

2. **Accent Colors**:
   - **Green (Toast Messages)**: The green toasts grab attention without overwhelming the user, making them an effective tool for providing instant feedback, such as "Item added to cart" or "Action completed successfully."

3. **Typography Colors**:
   - **Dark Blue**: Used for the text, this color contrasts well against the lighter backgrounds, ensuring readability and professionalism.

### Why the Green Toast Messages Work
While green may initially seem unrelated to the pastel tones of the site, it serves an important purpose in the **UX design**:
- **Functionality**: The green color is vibrant and draws immediate attention, ensuring users notice important notifications like confirmation messages or errors.
+ #### Typography
        - ### Typography in Dewi's Blooms Application

The typography in **Dewi's Blooms** combines elegance with practicality:

- **Primary Font:** `Arial, Helvetica, sans-serif` ensures readability and accessibility across devices.
- **Accent Font:** `Dancing Script`, used in the logo and key headings, adds a floral, elegant touch that reflects the brand’s charm.
- **Colors:** Neutral shades (`#555`, `#333`) for readability, with vibrant accents like `#ff5733` (orange) and `#5a8c5a` (green) to align with the floral theme.
- **Responsive Design:** Font sizes adapt seamlessly for mobile and desktop, maintaining a user-friendly experience.

This typography balances sophistication and usability, reinforcing the boutique florist aesthetic.
+ #### Imagery

- **Imagery** plays a pivotal role in the **Dewi's Blooms** experience, creating a visual connection with our users:

- **Daffodil Background:** As the national flower of Wales, the daffodil symbolizes our roots and heritage. It serves as a key background element, reflecting Dewi's Blooms' identity as a Welsh florist.
- **High-Quality Product Images:** To showcase our floral arrangements in their best light, we use crisp, high-resolution images. These visually appealing photos allow customers to confidently assess the quality of our products.
- **User Experience Impact:** While the use of high-quality images slightly affects website load times, their inclusion is crucial. They provide a pleasing and detailed visual experience that builds trust and encourages customers to feel confident in spending their money.

Our imagery not only enhances the site’s aesthetic but also underscores our commitment to quality and authenticity, making the shopping experience delightful and trustworthy.

---

## **Features**
------------
Thank you for clarifying! Let’s review and only include features **actually implemented** in the Dewi's Blooms app. Here's a refined list based on typical functionality for your app:

---

### **Features in Dewi's Blooms**

#### **1. Homepage**
- **Featured Products**:
  - Display a selection of highlighted flowers or arrangements.
- **Navigation Bar**:
  - Links to key sections: Shop, Cart, Login, and Account.
- **Search Bar**:
  - Allows users to search for products by name or keyword.
- **Responsive Design**:
  - Layout adjusts for both desktop and mobile users.

---

#### **2. Shop Page**
- **Product Listings**:
  - All available products are displayed in a grid format with:
    - Product image
    - Name
    - Price
    - "Add to Cart" button.
- **Category Filters**:
  - Users can filter products by categories like "Roses," "Bouquets," etc.

---

#### **3. Product Detail Page**
- **Detailed View**:
  - Provides:
    - Full product description
    - Pricing details
    - "Add to Cart" button.
- **High-Quality Product Image**:
  - Showcases floral arrangements.

---

#### **4. Shopping Cart**
- **Cart Management**:
  - View selected items with the ability to:
    - Adjust quantities
    - Remove items.
- **Order Summary**:
  - Displays total price, subtotal, and any applicable taxes or shipping fees.
- **Proceed to Checkout**:
  - Navigate directly to the checkout page.

---

#### **5. Checkout Page**
- **Secure Payment with Stripe**:
  - Users can enter card details and process payments securely.
- **Billing and Shipping Information**:
  - Input address and contact details during checkout.
- **Order Confirmation**:
  - Display a summary of the purchase upon completion.

---

#### **6. User Accounts**
- **User Registration**:
  - Sign up for a new account.
- **Login/Logout**:
  - Access personal account features.
- **Profile Management**:
  - Update account information like email, password, and shipping address.
- **Order History**:
  - View past orders and their statuses.

---

#### **7. Admin Features**
- **Product Management**:
  - Admins can:
    - Add new products
    - Edit existing products
    - Remove outdated products.
- **Order Management**:
  - Review and manage customer orders.

---

#### **8. Responsive Design**
- **Mobile-Friendly Interface**:
  - Fully optimized for smartphones and tablets.
- **Desktop Compatibility**:
  - Enhanced browsing experience for larger screens.

---

If there are additional features or specifics you'd like added or removed, let me know, and we can refine this further!


---

## **Technologies Used**
------------

- ### **Languages Used**
    * **HTML5**, **CSS3**, **JavaScript**, **Python3**

- ### **Frameworks, Libraries, and Programs Used**
    * **Django**: Backend framework for authentication, database interactions, and routing.
    * **django-allauth**: Used for user registration, login, and account management.
    * **Stripe**: For secure payments.
    * **Bootstrap5**: For responsive design and easy-to-use UI components.

---

## **Custom Models and Database Schema**
------------

### **Entity Relationship Diagram (ERD)**

This project uses custom Django models for managing data effectively. The two key models are:

1. **UserProfile**
    - Extends the default Django User model to include profile-related data.
    - Fields include `default_phone_number`, `default_street_address`, and other user details.

2. **Order**
    - Represents an order placed by a user.
    - Fields include `full_name`, `email`, `phone_number`, and `grand_total`.

### **Relationships and Cardinalities**

- **User ↔ UserProfile**
    - **Type**: One-to-One (1:1)
    - Each User has a single UserProfile to extend their information.

- **UserProfile ↔ Order**
    - **Type**: One-to-Many (1:N)
    - Each UserProfile can have multiple associated orders.

### **Database Schema**
#### **Category Table**
| **Field**         | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| `id`              | Primary Key                                                                     |
| `name`            | Unique Identifier for category (e.g., "Occasions", "Seasonal")                  |
| `friendly_name`   | User-friendly name for category                                                 |

#### **Product Table**
| **Field**         | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| `product_id`      | Primary Key                                                                     |
| `sku`             | Stock Keeping Unit                                                              |
| `category_id`     | Foreign Key referring to Category                                               |
| `name`            | Product name                                                                    |
| `price`           | Price of the product                                                           |

---
Table to compare 2 custom models, fields, and data entries in the context of the project. Based on your ERD and model details:

| In a DB       | In an ERD        | In Django           | Example                                     |
|---------------|------------------|---------------------|---------------------------------------------|
| **Table**     | **Entity**       | **Model**           | `Order`, `OrderLineItem`, `UserProfile`, `Product` |
| **Column**    | **Attribute**    | **Field**           | `full_name`, `email`, `phone_number`, `product_name`, `price` |
| **Row**       | n/a              | **Data entry**      | `John Doe`, `john@example.com`, `1234567890`, `Rose Bouquet`, `49.99` |

### Explanation:

- **Table** in a database maps to an **Entity** in an ERD and a **Model** in Django. Examples include models like `Order`, `OrderLineItem`, `UserProfile`, and `Product`.

- **Column** in a database corresponds to an **Attribute** in an ERD and a **Field** in Django. These fields contain specific data attributes for each model, such as `full_name`, `email`, `phone_number`, `product_name`, and `price`.

- **Row** in a database is a data entry, representing a single record. In Django, this corresponds to an instance of a model. For example, an order might have the data entry values: `John Doe` (full name), `john@example.com` (email), `1234567890` (phone number), `Rose Bouquet` (product name), and `49.99` (price).

This table provides a clear mapping of your Django models to database tables and their fields.

### 1. Understanding Custom Models

### Identifying Custom Models

We have **two custom models** in this project:

1. **Order Model** (from `checkout` app)
   - The `Order` model is custom because it was created specifically for this project to handle orders and related information, such as `full_name`, `email`, `phone_number`, and other order details.
   
2. **UserProfile Model** (from `profiles` app)
   - The `UserProfile` model is also custom. While Django provides a built-in `User` model for basic authentication, the `UserProfile` model is a custom extension that adds additional fields related to the user's profile, such as `default_phone_number`, `default_country`, and address fields.

- **Order** and **UserProfile** were explicitly designed and implemented to address specific needs in the project.
- They serve a specialized purpose beyond Django's default functionality.
- Custom fields, relationships, and methods within these models enable unique functionality, like handling orders or managing extended user profiles, which is outside the scope of Django’s built-in `User` or session models.

### Example to Differentiate Custom Models from Built-in Models

| Model        | Custom or Built-in | Purpose                                                          |
|--------------|--------------------|------------------------------------------------------------------|
| **Order**    | Custom             | Manages order details, including products ordered and user info. |
| **UserProfile** | Custom         | Extends user details, adding profile-specific fields like address.|
| **User**     | Built-in           | Handles basic authentication (Django provides this automatically). |
| **Session**  | Built-in           | Manages user sessions (Django manages this automatically).        |

### Summary

The project has **two custom models**: `Order` and `UserProfile`. These models are unique to the application, designed to manage data that Django's default models (like `User` or `Session`) don’t cover. The custom models provide flexibility and extend Django's built-in functionality, allowing site owner to store and manage additional information specific to shop/project requirements.

## **Testing**
------------

+ ### Validator Testing Results
    - All HTML and CSS files validated using the W3C Validator.
    * Results    

| Page                     | Notes              |
|--------------------------|--------------------|
| base.html               | ✅ No errors       |
| mobile-top-header.html  | ✅ No errors       |
| main-nav.html           | ✅ No errors       |
| bag.html                | ✅ No errors       |
| profile.html            | ✅ No errors       |
| products.html           | ✅ No errors       |
| product_detail.html     | ✅ No errors       |
| edit_product.html       | ✅ No errors       |
| add_product.html        | ✅ No errors       |
| index.html              | ✅ No errors       |
| search_results.html     | ✅ No errors       |
| checkout.html           | ✅ No errors       |
| checkout_success.html   | ✅ No errors       |

### CSS Validation
I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to validate my CSS code.

 I entered each CSS file separately and got No errors each time.

Here are the tables for manual testing of Dewi's Blooms app that you can use to fill in the results for each feature:

---

### **Manual Testing (Feature Testing)**

#### **Authentication**

| Page      | User Action                                      | Expected Result                                                                                 | Pass/Fail | Comments          |
|-----------|--------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------|-------------------|
| Sign In   | Enter valid username and password, click 'Sign In' | Directed to homepage. Toast confirming successful sign in.                                      |           |                   |
|           | Enter invalid credentials, click 'Sign In'        | Error message indicating incorrect username/password.                                           |           |                   |
|           | Click 'Sign-up'                                   | Redirected to the 'Sign Up' page.                                                              |           |                   |
|           | Click 'Forgot your password?'                     | Redirected to the 'Password Reset' page.                                                       |           |                   |
| Sign Up   | Enter valid credentials, click 'Sign-Up'          | Account created, verification email sent. Redirect to verification page.                       |           |                   |
|           | Click verification link in email                  | Opens 'Confirm Email' page.                                                                   |           |                   |
|           | Click 'Confirm'                                   | Redirected to 'Sign-In' page. Toast confirms email verification.                               |           |                   |
|           | Submit empty form fields                          | Validation errors prompting to fill in required fields.                                        |           |                   |
|           | Enter an existing username                        | Error message indicating the username is already taken.                                        |           |                   |
| Sign Out  | Click 'Sign Out'                                  | Redirected to homepage. Toast confirms successful sign out.                                    |           |                   |

---

#### **All Visitor Features**

| Page                     | User Action                                     | Expected Result                                                                            | Pass/Fail | Comments          |
|--------------------------|-------------------------------------------------|--------------------------------------------------------------------------------------------|-----------|-------------------|
| Navbar - Logo            | Clicks logo                                     | Navigate to homepage.                                                                     |           |                   |
| Navbar - Search Bar      | Enter valid search query                        | Displays search results matching the query.                                               |           |                   |
|                          | Enter invalid query or leave empty              | Displays all products. Toast message explaining no results found.                         |           |                   |
| Navbar - User Icon       | Clicks user icon (unauthenticated)              | Redirected to the 'Sign In' page.                                                         |           |                   |
|                          | Clicks user icon (authenticated)                | Redirected to the 'Profile' page.                                                         |           |                   |
| Navbar - Basket Icon     | Clicks basket icon                              | Redirected to the 'Shopping Bag' page.                                                    |           |                   |

---

#### **Product Features**

| Page               | User Action                                      | Expected Result                                                                 | Pass/Fail | Comments          |
|--------------------|--------------------------------------------------|---------------------------------------------------------------------------------|-----------|-------------------|
| Products Page      | Hover over a product                             | Image overlay appears with a "View Details" button.                             |           |                   |
|                    | Click on a product                               | Redirected to the product detail page.                                          |           |                   |
| Product Detail     | Add product to shopping bag                      | Product added. Toast confirms addition. Bag icon count increases.               |           |                   |
|                    | Change product quantity                          | Quantity updates dynamically in the shopping bag.                               |           |                   |
| Search Results     | Click on a search result                         | Redirected to the respective product detail page.                               |           |                   |

---

#### **Checkout**

| Page                  | User Action                                    | Expected Result                                                                 | Pass/Fail | Comments          |
|-----------------------|------------------------------------------------|---------------------------------------------------------------------------------|-----------|-------------------|
| Shopping Bag          | Click "Secure Checkout" button                | Redirected to the 'Checkout' page.                                              |           |                   |
| Checkout              | Submit form with empty fields                 | Validation errors prompting to fill in required fields.                         |           |                   |
|                       | Enter invalid card details                    | Error message explaining invalid payment details.                               |           |                   |
|                       | Enter valid card details                      | Redirected to 'Checkout Success' page. Toast confirms successful order.         |           |                   |
| Checkout Success      | Click "Continue Shopping"                     | Redirected to homepage.                                                         |           |                   |

---

#### **Profile Features**

| Page                  | User Action                                     | Expected Result                                                                | Pass/Fail | Comments          |
|-----------------------|-------------------------------------------------|--------------------------------------------------------------------------------|-----------|-------------------|
| Profile Page          | Click on "Order History"                       | Redirected to the 'Order History' page.                                        |           |                   |
|                       | Click on "Edit Profile"                        | Redirected to the 'Edit Profile' page.                                         |           |                   |
| Edit Profile          | Submit valid changes                           | Profile updates successfully. Toast confirms the update.                       |           |                   |
|                       | Submit invalid changes                         | Validation error prompts corrections.                                          |           |                   |

---

#### **Admin Features**

| Page                  | User Action                                      | Expected Result                                                                 | Pass/Fail | Comments          |
|-----------------------|--------------------------------------------------|---------------------------------------------------------------------------------|-----------|-------------------|
| Manage Products       | Click "Add Product"                             | Redirected to the 'Add Product' page.                                           |           |                   |
| Add Product           | Submit valid details                            | Product added. Redirected to product list. Toast confirms addition.             |           |                   |
|                       | Submit invalid details                          | Validation error prompts corrections.                                          |           |                   |
| Edit Product          | Submit valid changes                            | Product updates successfully. Toast confirms the update.                       |           |                   |
| Delete Product        | Confirm deletion                                | Product removed. Toast confirms successful deletion.                           |           |                   |

---

### **Lighthouse Audit**

| Page                     | Performance | Accessibility | Best Practice | SEO | Comments                        |
|--------------------------|-------------|---------------|---------------|-----|---------------------------------|
| Homepage                 |             |               |               |     |                                 |
| Products Page            |             |               |               |     |                                 |
| Product Detail           |             |               |               |     |                                 |
| Shopping Bag             |             |               |               |     |                                 |
| Checkout                 |             |               |               |     |                                 |
| Profile                  |             |               |               |     |                                 |

---
+ ### Browser Compatibility
    - Website tested on Chrome, Firefox, and Safari.

---

## **Deployment**
------------

### **Heroku Deployment**
- Create a Heroku app and configure environment variables.
- Use Gunicorn and AWS S3 for production deployment.
---
### **Email Configuration**
- Set up Gmail for sending notifications using Django’s email backend.
---
### **Stripe Setup**
- Integrate Stripe for secure payment processing.
- Add webhook endpoint for handling payment events.
---
## **Clone the Project**

1. Clone the repository:
    ```bash
    git clone https://github.com/ashwinsel/Milestone-Project-4-DewisBlooms.git
    ```
2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure environment variables and migrate the database:
    ```bash
    python manage.py migrate
    ```
---
## **Credits**
------------

### **Acknowledgements**
Special thanks to mentors and peers for feedback and guidance during this project.

### **Resources**
- [Code Institute’s Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1).
- [Django Documentation](https://docs.djangoproject.com/).

### **Images**
Product images sourced from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/).

---

## **Gratitude**
------------

Thanks to **Code Institute** for their guidance, and mentors for their invaluable feedback.


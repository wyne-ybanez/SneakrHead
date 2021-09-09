## Testing

### User stories: Shopper View & Navigation
-

**User Story:**
> As a shopper, I would like to view a list of Products

**Criteria:**
- Products are should be displayed clearly for the customers and named appropriately.
- Products should be easily categorised and sorted.

**Implementation:**

The site will display the products through products.html. An initial view of the product is displayed in index.html. The site also incoporates numerous ways for the customer to find popular and new brands through the sorting menu, through products.html or through the horizontal scroll at the bottom of the page.

<hr>

**User Story:**
> As a shopper, I would like to view a specific category of products

**Criteria:**
- The site should categorise its products so as the filter the products shown on the page.
- Categorising products should be simple and it should be easy to categorise products.

**Implementation:**

The site allows shoppers to categorise products through the main navigational menu on all pages. This is accessible on both short, medium and large screens and there are 4 choices: men's, women's, kids' and discounted items. 

<hr>

**User Story:**
> As a shopper, I would view individual product details

**Criteria:**
- The shopper should be able to access the description and details of their desired product.

**Implementation:**

The site allows the shopper to view product description by clicking on the product's image/card. This will then lead them to the product details page, product_details.html, which will display the item's price, rating, category, brand, description and availability.

<hr>

**User Story:**
> As a shopper, I would like to quickly identify deals and special offers

**Criteria:**
- The shopper should be able to search for discounted items easily.

**Implementation:**

The website utilises a category called 'Discounted' to navigate to discounted products on the online, store shown on the sort_display.html component page.

<hr>

**User Story:**
> As a shopper, I would like to easily view the total of my purchases at any time

**Criteria:**
- There should be a button or a link that allows the shopper to view the products they would like to purchase 
- This page should display a list of the products, their details and the total price for the order

**Implementation:**

There is a basket app and a basket icon in the navigation bar which leads to basket.html. This allows the shopper to view the items in their basket, the title of the products, the details such as size, quantity and price.

### User stories: Sorting and Searching
-

**User Story:**
> As a shopper, I would like to sort the list of available products 

**Criteria:**
- The shopper must have the ability to filter/sort the products according to a certain rule. For example, sort the products in alphabetical order.

**Implementation:**

The website utilises a sorting display feature through a sort display menu. It will have numerous options such as filtering the products alphabetically, reverse alphabetically, by price (lowest to highest) and by rating. This sorting menu is available in products.html.

<hr>

**User Story:**
> As a shopper, I would like to sort a specific category of products

**Criteria:**
- Once a category is chosen by the shopper, they should be able to sort the list of products with the active category filter

**Implementation:**

In products.html, the user can choose a specific category on the navigation menu, then, should the shopper prefer to sort the products a cetain way, the category filter remains and the products sort accordingly. 

<hr>

**User Story:**
> As a shopper, I would like to search for a product by name or description 

**Criteria:**
- The shopper should be able to query the website for a product, searching its name or a text which resides in its description

**Implementation:**

The website utilises a search bar feature which allows the shopper to search for a specific product either searching the product name or description. This feature is availbable on all screens, at the top of the page for medium to large screens in the navbar. Within products.html underneath the titles on small screens.

<hr>

**User Story:**
> As a shopper, I would like to easily see what I’ve searched for and the number of results

**Criteria:**
- The shopper needs to see what their search criteria was and the total products that can be displayed through their search

**Implementation:**

Once a search query is presented by the user, the site will display the total number of products found that matches the shopper's query and text entered for their query. The result is showin in products.html and is searched using the function from the Products app view.

### User stories: Shopper Purchasing & Checkout
-

**User Story:**
> As a shopper, I would like to easily select the size and quantity of a product when purchasing it

**Criteria:**
- The shopper should be able to choose the size and quantity of the product prior to purchasing and order creation

**Implementation:**

The site incorporates a product detail page, product_detail.html, as well as a basket page, basket.html, where the shopper can outline the size and quantity for their desired product, factors of which are customizeable at any time prior to the checkout process.

<hr>

**User Story:**
> As a shopper, I would like to view items in my bag to be purchased

**Criteria:**
- The shopper should have complete freedom to check the items they have placed in their shopping basket at any point in time

**Implementation:**

Through the shopping basket functionality, user's can always view the items within their basket, this is situated at the top right of the screen. It leads to the basket page and displays the totals, quantity and prices of the products they wish to purchase prior to checkout.

<hr>

**User Story:**
> As a shopper, I would like to adjust the quantity of individual items in my bag

**Criteria:**
- The shopper must have complete freedom to edit the quantities for all items in their basket

**Implementation:**

The basket page allows the shopper to edit the quantities of all their items. It will have up and down arrows within the input box, it allows the shopper to type the quantity and it also allows the shopper to increase or decrease the value using the append and prepend buttons.

<hr>

**User Story:**
> As a shopper, I would like to easily enter my payment information

**Criteria:**
- The user should be able to go to checkout easily and continue with their purchase, the should be able to add their payment information once they are certain they would like to buy an item.

**Implementation:**

The site utilises a checkout functionality which allows the shopper to add their card details and make a purchase. This will appear in the form of a toast with a secure checkout option, or by clicking the basket icon and continuing to the checkout page.

<hr>

**User Story:**
> As a shopper, I would like to feel my personal and payment information is safe and secure

**Criteria:**
- The shopper's payment information must be secure and confidential at all times. Appropriate payment validation logic must be present to detect safe and secure purchases.

**Implementation:**

The site takes advantage of Stripes API and uses payment intent to determine if a card's purchase is successful or if it was not successful. If a purchase is unsuccessful due to glitches, the card is not charged. The site always responds with a status message for successful or failed payments. Stripe will also ensure that the shopper's card physically exists and will require the card owner's details prior to a payment.

<hr>

**User Story:**
> As a shopper, I would like to view an order confirmation after checkout

**Criteria:**
- An order confirmation should be sent to the shopper once they have successful made a payment and have went through the checkout process completely

**Implementation:**

An order confirmation page is implemented within the site's functionalities and will appear displaying the shopper's purchase details such as order number, product type and details, quantities, date of purchase, personal details of the shopper used for payment.

<hr>

**User Story:**
> As a shopper, I would like to receive an email confirmation after checking out

**Criteria:**
- Shoppers should receive an email confirming the order they just made so as to keep them as records for the purchase.

**Implementation:**

An order confirmation email is sent to the user outlining the order number, date and total costs. This order confirmation email is sent directly to the customer's chosen email after a successful creation of an order.

### User stories: Site User

**User Story:**
> As a User, I would like to easily register for an account

**Criteria:**
- New shoppers should be able to sign up for an profile on the site

**Implementation:**

The site allows users to register for an account at any time either prior to, during, or after a purchase. This is facilitated through django allauth and is handled through the signup.html. At the top right there is a person icon which can be clicked and will display options to register.

<hr>

**User Story:**
> As a User, I would like to easily login or logout 

**Criteria:**
- Users should have the ability to sign in and log out of their account at any point in time whilst exploring 

**Implementation:**

The site allows its shoppers to sign in to their respective accounts from the navigation bar. At the top right there is a person icon which can be clicked and will display options to register or login. This same icon will also show options to log out or check the user's profile. It will display their user profiles in profile.html

<hr>

**User Story:**
> As a User, I would like to easily recover my password in case I forget it

**Criteria:**
- There should be a way for the site user to retrieve or create a new password should they ever forget their current password.

**Implementation:**

The site utilises django allauth to assist shoppers/users with pasword resets on password_reset.html. This will help shoppers who forgot their password to create a new password all together and access their profiles.

<hr>

**User Story:**
> As a User, I would like to receive an email confirmation after registering

**Criteria:**
- A confirmation email must be sent to the user after a successful sign up for a profile

**Implementation:**

The site utilises django and an allauth template to also send the user an email confirming that they have just registered for an account. This email confirmation message is displayed through the email_confirmation_message.txt.

<hr>

**User Story:**
> As a User, I would like to have a personalised user profile

**Criteria:**
- The shopper must have a profile that shows their personal details and the orders they have created on their respective accounts.

**Implementation:**

Once the shopper creates a profile account. The site records the shoppers orders once they make an order. The site also saves the shoppers personal details after the checkout process should the shopper choose to save their information for future orders. Records of their recent orders and their billing information are stored in profile.html.


#### Admin User Stories

User Story:
> 

Criteria:
- 

Implementation:


User Story:
> 

Criteria:
- 

Implementation:


User Story:
> 

Criteria:
- 

Implementation:
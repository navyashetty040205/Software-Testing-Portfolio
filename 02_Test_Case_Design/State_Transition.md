
# STATE TRANSITION TESTING

## 1. Introduction
State Transition Testing is a black-box testing technique used to verify the behaviour of an application when it moves from one state to another due to user actions or events.

It helps ensure that the application transitions correctly between different states.

## 2. Application Module
Login and Shopping Cart Module of SauceDemo Online Shopping Application.

Website: https://www.saucedemo.com/

## 3. Test Objective
To verify that the application moves correctly between different states during login, product selection and checkout.

## 4. Application States

| State ID | State Description |
|---|---|
| S1 | Login Page |
| S2 | Products Page |
| S3 | Shopping Cart Page |
| S4 | Checkout Information Page |
| S5 | Checkout Overview Page |
| S6 | Order Confirmation Page |

## 5. State Transitions

| Current State | User Action | Next State |
|---|---|---|
| Login Page | Enter valid credentials | Products Page |
| Login Page | Enter invalid credentials | Login Page with error |
| Products Page | Click cart icon | Shopping Cart Page |
| Shopping Cart Page | Click Checkout | Checkout Information Page |
| Checkout Information Page | Enter valid details and click Continue | Checkout Overview Page |
| Checkout Overview Page | Click Finish | Order Confirmation Page |

## 6. Test Cases

| Test Case ID | Initial State | Action | Expected State |
|---|---|---|---|
| ST01 | Login Page | Enter valid credentials | Products Page |
| ST02 | Login Page | Enter invalid credentials | Login Page with error |
| ST03 | Products Page | Click cart icon | Shopping Cart Page |
| ST04 | Shopping Cart Page | Click Checkout | Checkout Information Page |
| ST05 | Checkout Information Page | Enter valid details and Continue | Checkout Overview Page |
| ST06 | Checkout Overview Page | Click Finish | Order Confirmation Page |

## 7. Test Procedure
1. Open SauceDemo.
2. Enter valid login credentials.
3. Verify that the products page appears.
4. Add a product to the cart.
5. Navigate to the shopping cart.
6. Click Checkout.
7. Enter the required checkout information.
8. Click Continue.
9. Verify the checkout overview.
10. Click Finish and verify the order confirmation page.

## 8. Conclusion
State Transition Testing helps verify the movement of the application between different states. It ensures that user actions lead to the expected pages and that the shopping workflow functions correctly.

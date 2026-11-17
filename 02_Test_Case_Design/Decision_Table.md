
# DECISION TABLE TESTING

## 1. Introduction
Decision Table Testing is a black-box testing technique used to test system behaviour based on different combinations of input conditions.

It helps verify that the application responds correctly to different combinations of conditions.

## 2. Application Module
Checkout Information Module of SauceDemo Online Shopping Application.

Website: https://www.saucedemo.com/

## 3. Test Objective
To verify the checkout functionality by testing different combinations of first name, last name and postal code inputs.

## 4. Conditions
- C1: First name entered
- C2: Last name entered
- C3: Postal code entered

## 5. Decision Table

| Conditions / Rules | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| First name entered | Yes | No | Yes | Yes |
| Last name entered | Yes | Yes | No | Yes |
| Postal code entered | Yes | Yes | Yes | No |
| **Actions** | | | | |
| Proceed to next step | Yes | No | No | No |
| Display validation error | No | Yes | Yes | Yes |

## 6. Test Cases

| Test Case ID | First Name | Last Name | Postal Code | Expected Result |
|---|---|---|---|---|
| DT01 | Entered | Entered | Entered | Proceed to next step |
| DT02 | Empty | Entered | Entered | Display error |
| DT03 | Entered | Empty | Entered | Display error |
| DT04 | Entered | Entered | Empty | Display error |

## 7. Test Procedure
1. Open SauceDemo.
2. Log in with valid credentials.
3. Add a product to the shopping cart.
4. Open the cart and click Checkout.
5. Enter the values according to each test case.
6. Click Continue.
7. Observe the application response.
8. Record the actual result.

## 8. Conclusion
Decision Table Testing helps verify the checkout process by testing different combinations of input conditions. It ensures that the application displays appropriate validation messages when required information is missing.

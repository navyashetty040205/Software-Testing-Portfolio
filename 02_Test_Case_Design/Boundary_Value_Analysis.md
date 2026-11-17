
# BOUNDARY VALUE ANALYSIS

## 1. Introduction
Boundary Value Analysis (BVA) is a black-box testing technique used to test values at the minimum and maximum boundaries of an input range.

It helps identify errors that may occur at the edges of input limits.

## 2. Application Module
Checkout Information Module of SauceDemo Online Shopping Application.

Website: https://www.saucedemo.com/

## 3. Test Objective
To verify that the checkout information fields accept appropriate input values and handle empty or boundary inputs correctly.

## 4. Test Data and Boundaries

For this exercise, the first name, last name and postal code fields will be tested using empty and non-empty values.

The application does not publish a numeric minimum or maximum length for these fields. Therefore, the following are practical boundary-oriented tests rather than verified length limits.

| Field | Boundary Condition | Test Input |
|---|---|---|
| First Name | Minimum | Empty |
| First Name | Just above minimum | A |
| Last Name | Minimum | Empty |
| Last Name | Just above minimum | B |
| Postal Code | Minimum | Empty |
| Postal Code | Just above minimum | 1 |

## 5. Test Cases

| Test Case ID | Test Input | Expected Result |
|---|---|---|
| BVA01 | First name empty | Checkout should show required-field error |
| BVA02 | First name A | Field should accept non-empty input |
| BVA03 | Last name empty | Checkout should show required-field error |
| BVA04 | Last name B | Field should accept non-empty input |
| BVA05 | Postal code empty | Checkout should show required-field error |
| BVA06 | Postal code 1 | Field should accept non-empty input |

## 6. Test Procedure
1. Open SauceDemo.
2. Log in using valid credentials.
3. Add a product to the cart.
4. Open the cart and click Checkout.
5. Enter the selected test values.
6. Click Continue.
7. Observe the application response.
8. Compare actual and expected results.

## 7. Conclusion
Boundary-oriented testing helps identify errors associated with empty and minimum input values. It improves the reliability of the checkout information module.

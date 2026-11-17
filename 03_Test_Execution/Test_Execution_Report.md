
# TEST EXECUTION REPORT

## 1. Introduction
This document records the manual testing activities performed on the SauceDemo online shopping application.

## 2. Testing Environment
- Application: SauceDemo
- Website: https://www.saucedemo.com/
- Browser: Google Chrome
- Testing Type: Manual Functional Testing

## 3. Test Execution Results

### A. Shopping Workflow Testing

| Test ID | Test Scenario | Actual Result | Status |
|---|---|---|---|
| EX01 | Login with valid credentials | Products page opened | PASS |
| EX02 | Select a product | Product selected | PASS |
| EX03 | Add product to cart | Product added successfully | PASS |
| EX04 | Proceed to checkout | Checkout page opened | PASS |
| EX05 | Enter checkout information | Overview page opened | PASS |
| EX06 | Complete order | Order confirmation displayed | PASS |

### B. Negative Login Testing

| Test ID | Test Scenario | Actual Result | Status |
|---|---|---|---|
| EP02 | Wrong username | Invalid credentials error displayed | PASS |
| EP03 | Wrong password | Invalid credentials error displayed | PASS |
| EP04 | Empty username | Username is required | PASS |
| EP05 | Empty password | Password is required | PASS |
| EP06 | Both fields empty | Username is required | PASS |

### C. Checkout Validation Testing

| Test ID | Test Scenario | Actual Result | Status |
|---|---|---|---|
| BVA01 | Empty first name | First Name is required | PASS |
| BVA03 | Empty last name | Last Name is required | PASS |
| BVA05 | Empty postal code | Postal Code is required | PASS |

## 4. Test Execution Summary

- Total test cases executed: 14
- Passed: 14
- Failed: 0
- Pass Percentage: 100%

## 5. Observations
1. Valid login credentials successfully opened the products page.
2. Invalid login credentials displayed an appropriate error message.
3. Empty login fields displayed validation messages.
4. Products were successfully added to the shopping cart.
5. Checkout validation correctly identified missing information.
6. The order confirmation page appeared after completing checkout.

## 6. Conclusion
The manual testing of the SauceDemo online shopping application was performed successfully.

All 14 executed test cases passed during the testing session. The application behaved as expected for the tested scenarios.

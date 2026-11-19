
# Test Execution Report

## 1. Introduction

This report distinguishes the recorded manual test run from the later Selenium
automation run. Their results are separate and should not be combined into one
pass percentage.

## 2. Testing Environment

- Application: SauceDemo
- Website: https://www.saucedemo.com/
- Browser: Google Chrome
- Automation: Python, Selenium WebDriver, and pytest

## 3. Manual Test Execution

The following results are retained from the manual execution record. The date
of that run was not recorded.

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

**Manual run summary:** 14 recorded test cases; 14 passed; 0 failed.

## 4. Automated Test Execution

The pytest suite was run on 2026-11-18.

| Metric | Result |
|---|---:|
| Tests collected | 57 |
| Passed | 56 |
| Failed | 1 |

The failed test was `test_PROD010_problem_user_images`. For the SauceDemo `problem_user`
account, all six product images showed the same missing-image placeholder. The
test failure is documented in [the defect report](../04_Defect_Reports/Defect_Report.md),
and evidence is saved as [08_problem_user_images.png](../07_Screenshots/08_problem_user_images.png).

## 5. Summary

The recorded manual scenarios passed. The automated suite found an image issue
for the `problem_user` account, so the overall testing outcome is **not a clean
pass**. The manual and automated results are from separate runs and have
different scopes.

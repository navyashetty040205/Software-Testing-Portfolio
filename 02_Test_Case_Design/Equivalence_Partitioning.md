
# EQUIVALENCE PARTITIONING

## 1. Introduction
Equivalence Partitioning is a black-box software testing technique in which input data is divided into valid and invalid groups called equivalence classes.

Instead of testing every possible input, one representative value from each class is selected for testing.

## 2. Application Module
Login Module of SauceDemo Online Shopping Application.

Website: https://www.saucedemo.com/

## 3. Test Objective
To verify whether the login functionality accepts valid credentials and rejects invalid or incomplete credentials.

## 4. Equivalence Classes

| Class ID | Input Condition | Type |
|---|---|---|
| EC01 | Valid username and valid password | Valid |
| EC02 | Invalid username and valid password | Invalid |
| EC03 | Valid username and invalid password | Invalid |
| EC04 | Empty username | Invalid |
| EC05 | Empty password | Invalid |
| EC06 | Both username and password empty | Invalid |

## 5. Test Cases

| Test Case ID | Test Input | Expected Result |
|---|---|---|
| EP01 | standard_user / secret_sauce | Login successful |
| EP02 | wrong_user / secret_sauce | Error message displayed |
| EP03 | standard_user / wrong_pass | Error message displayed |
| EP04 | Empty username / secret_sauce | Username required error |
| EP05 | standard_user / Empty password | Password required error |
| EP06 | Empty username / Empty password | Username required error |

## 6. Test Procedure
1. Open the SauceDemo website.
2. Enter the selected username and password.
3. Click the Login button.
4. Observe the application response.
5. Compare the actual result with the expected result.
6. Record the test result.

## 7. Conclusion
Equivalence Partitioning helps reduce the number of test cases while maintaining effective test coverage. It helps verify that valid inputs are accepted and invalid inputs are rejected by the login module.

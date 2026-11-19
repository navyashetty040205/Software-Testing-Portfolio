# Test Summary Report

## Project

- **Application:** SauceDemo online shopping application
- **Website:** https://www.saucedemo.com/
- **Testing approach:** Manual functional testing and Selenium automation

## Results

| Execution | Run date | Executed | Passed | Failed |
|---|---|---:|---:|---:|
| Manual scenarios (recorded run; date not recorded) | Not recorded | 14 | 14 | 0 |
| Selenium / pytest | 2026-11-18 | 57 | 56 | 1 |

These are separate runs with different scopes. Their counts are not added
together as unique test cases.

## Finding

The automated run failed `test_PROD010_problem_user_images`: all six product
images appeared as the same missing-image placeholder when logged in as
`problem_user`. The finding is documented as DEF-001 in the
[defect report](../04_Defect_Reports/Defect_Report.md), with screenshot evidence
in [08_problem_user_images.png](../07_Screenshots/08_problem_user_images.png).

## Overall assessment

The manual scenarios passed in their recorded run, but the automation run
found an issue. Therefore, the overall result is **56/57 automated tests
passed, with one observed issue documented**; it is not a 100% pass result.

For detailed test cases and execution records, see the
[test execution report](../03_Test_Execution/Test_Execution_Report.md).

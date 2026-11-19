# Defect Report

## Project Details

- **Project:** Software Testing of an Online Shopping Application
- **Application:** SauceDemo
- **Testing type:** Selenium automation

## Defect Summary

### DEF-001: Product images are missing for the `problem_user` account

| Field | Details |
|---|---|
| Affected module | Products / product images |
| Test case | `test_PROD010_problem_user_images` |
| Status | Observed during automation; recorded for evaluation |
| Evidence | [08_problem_user_images.png](../07_Screenshots/08_problem_user_images.png) |

**Precondition:** The SauceDemo site is available and the `problem_user`
credentials can be used to log in.

**Steps to reproduce:**
1. Open https://www.saucedemo.com/.
2. Log in using the `problem_user` credentials configured for the tests.
3. Open the products page and inspect the product images.

**Expected result:** Each product displays its corresponding image.

**Actual result:** All six product images show the same missing-image
placeholder. This was detected by the automated test on 2026-11-18.

**Impact:** Product imagery is unavailable for this account, making products
harder to identify visually. This observation is specific to the tested
`problem_user` account and does not establish that other accounts are affected.

## Other Tested Scenarios

The previous manual execution record reports these scenarios as passing:

| Test Scenario | Recorded Result |
|---|---|
| Valid and invalid login inputs | PASS |
| Empty login fields | PASS |
| Checkout required-field validation | PASS |
| Complete shopping flow | PASS |

The manual results are historical and separate from the automated run. See the
[test execution report](../03_Test_Execution/Test_Execution_Report.md) for
their counts and the automated suite result.

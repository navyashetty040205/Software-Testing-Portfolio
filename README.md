
# Software Testing Portfolio

## Student Details
- **Name:** Navya P Shetty
- **USN:** [1MS23IS075]
- **College:** [MS RAMAIAH INSTITUTE OF TECHNOLOGY]
- **Subject:** Software Testing

## Project Title
Software Testing of an Online Shopping Application

## Application Selected
SauceDemo - Online Shopping Application

Website: https://www.saucedemo.com/

## Project Description
This project focuses on testing an online shopping application to verify its functionality, reliability and usability.

The application allows users to log in, browse products, add products to the shopping cart and complete the checkout process.

## Objectives
1. To understand the software testing process.
2. To prepare a test plan for an online shopping application.
3. To design test cases using different testing techniques.
4. To execute test cases and identify defects.
5. To perform automation testing using Selenium.
6. To document and maintain testing reports.

## Testing Techniques
- Equivalence Partitioning
- Boundary Value Analysis
- Decision Table Testing
- State Transition Testing

## Tools Used
- GitHub
- Selenium
- Python
- Google Chrome

## Project Modules
- Login Module
- Product Module
- Shopping Cart Module
- Checkout Module
- Order Confirmation Module

## Expected Outcome
To evaluate the functionality of the online shopping application, identify defects and understand practical software testing activities.

## Run the automated tests

From the repository root in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r 05_Test_Automation\requirements.txt
py -m pytest
```

Chrome must be installed. Tests run headlessly by default; add `--headed` to
show the browser window:

```powershell
py -m pytest --headed
```

The last recorded run (2026-11-18) collected 57 tests: 56 passed and 1 failed.
The known failure checks missing product images for SauceDemo's `problem_user`
account. See the [test execution report](03_Test_Execution/Test_Execution_Report.md)
and [defect report](04_Defect_Reports/Defect_Report.md).

## Portfolio folders

- `01_Test_Plan` — test plan
- `02_Test_Case_Design` — testing-technique documents
- `03_Test_Execution` — execution details
- `04_Defect_Reports` — documented findings
- `05_Test_Automation` — Selenium tests and supporting code
- `06_Test_Reports` — summary report
- `07_Screenshots` — test evidence

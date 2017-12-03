# Covenant-Monitoring-Capstone
This repo contains my capstone project from my 2017 coding bootcamp.

*Covenant Monitoring is a loan portfolio management system, that automates compliance management by comparing user-defined Loan Covenants (i.e. agreed-upon financial performance metrics) with financial data that is pulled from the user once connected with their Quickbooks account.  Previously, borrowers would be required to submit financial statements periodically, and checked manually.  Covenant Monitoring automates the process, increasing the effectiveness of monitoring by reducing the likelihood of errors and minimizing personnel resources.*

The project was deployed using Django web framework, leveraging Javascript, HTML/CSS, and Python.  I learned a lot about Django's templating system and Jinja syntax.  I owe a big thanks to my instructor, Chris Jones, who helped me with the Oauth2 connections to and using exisitng code we found on github.

The project leverages https://github.com/grue/django-quickbooks-online and https://github.com/sidecars/python-quickbooks.  Using these repos, I connected to a sandbox Intuit Quickbooks account, and pulled a financial statement (in this instance, a Balance Sheet). 

This project is just an MVP of the final product.  Next steps for the project include:
* Creating batch-pull functionality
* Creating effective UI system for connecting with clients' financial statements
* Expand financial statments beyond just Balance Sheet
* Add additional covenants to choose from
* Create covenants that are more complex rather than a single datapoint
* Add users to allow multiple portfolios
* Strengthen site design

# test.io
An automated system test suite for Intelligent Office

Python + pytest + selenium + page objects

## BrowserTypes

The current supported browsertypes are:
* Chrome [Default], firefox, ie, edge

## Prerequisites

Download and unpack ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads
Ensure the path you unpack the driver to is in your PATH

# Setting up a virtual environment
Being of the project repo in the gitbash console, execute the following commands:
* pip install -r requirements.txt
* pip install virtualenv
* virtualenv venv
* source venv/Scripts/activate
(potentially you might come across the ModuleNotFoundError: No module named 'requests'. It can be fixed by executing the command "pip install requests")

## Running Locally

Required parameters are:
* -E The environment eg: `prd-10`, `uat-10`, `tst-01`, `tst-02` etc. Domain names are derived from this. 

Override parameters are (the defaults are in `vars/env.json`):
* -U The username to login with. Default value differs per environment.
* -P The password to login with. Default value differs per environment.
* -D The domain i.e. https://abc.com, current default is 'https://www.intelligent-office.net'

Other parameters are: 
* -C The OAuth client id
* -S The OAuth client secret
* -K The api key
* -B Browser types. Supported values `chrome` [Default], `firefox`, `ie`, `edge` and `SauceLabs`
* -T New value in data.json to run teh test with, if not provided the data.json is used

## Markers

To see markers, check AVAILABLE_MARKERS.md 

## Running Selected Tests Sequentially

You can specify which tests to run.

To run all tests in a specific folder
```
pytest userjourneys/* -E tst-02 
```
To run all tests in a specific class
```
pytest userjourneys/test_user_journey_1.py -E tst-02
```
To run tests with one a marker (assuming you are currently in the test directory i.e. `cd userjourneys`)
```
pytest -m "login" -E tst-02
```
or more than one marker
```
pytest -m "clientsearch or login" -E tst-02
```
or excluding certain marker(s)
```
pytest -m "not login and not clientsearch" -E tst-02
```
***
To run tests based on any part of their name
```
pytest -k "user_journey" -E tst-02
```
or excluding a name
```
pytest -k "not user_journey" -E tst-02
```

## Running Selected Tests Parallel

At the moment we are able to run our tests parallel using pytests xdist library in the following environments :
prd-10, uat-10, tst-02 

Other environments preparation is in progress.

```
Running in 3 threads example below:
pytest userjourneys -E "env_name" -m "marker" --dist=loadscope  --tx popen//env:IO_FIELD="username1/password" --tx popen//env:IO_FIELD="username2/password"  --tx popen//env:IO_FIELD="username3/password"
```

The username and password can be found here for each environment: https://confluence.intelliflo.com/display/QA/06+Test+credentials

## Test Results

You can specify either an xml file or html or json report.
We are currently using json report to send the data from jenkins to splunk.
Also jenkins builds are passing/failing based on the json report.
All the report related settings can be found in pytest.ini
```
json_report = ui_tests/ui_test_results.json
--junitxml=ui_test_results.xml
--html=ui_test_results.html --self-contained-html
```

## SauceLabs

If you have a SauceLabs account you need to provide a **username** and **api key** to pytest

The saucelabs.json file should look like:
```
{
    "saucelabs": {
        "username": "XXXXX",
        "password": "XXXXX"
	}
}
```
and be located in the test.io /vars folder

To run using saucelabs supply the following:
```
--variables vars/saucelabs.json -B saucelabs
```

## API Tests

You must provide the `-E` option on the commandline so that all the required domain names can be derived.

You can provide options `-C`, `-S`, `-K`, `-U`, `-T`, `-P` and `-E`.


## Configuring tests with common and environmental data

Variable files can be passed to pytest using the `--variables vars/file.json` syntax. By default `vars/env.json`, `vars/common_data.json` and `vars/env_data.json` are 
passed to pytest automatically as a convenience.

* `env.json` is used to store information about the environment such as domain names and port numbers etc. 

* `commo_data.json` is used to hold test specific static data such as test data, client names etc. 

* `env_data.json` is used to contain the env related data f.e. username, password, etc The default username and password are provided in `environments.*.data.users.default.username` and `environments.*.data.users.default.password` respectively.

All the information above can be overridden by cmd line parameters, see above.

To use these variables in test fixtures they can be accessed from the `config.variables` property. If you just want the test data you can access this as follows: `config.get_data()["myvariable"]`. 

# CODING CONVENTIONS

# Coding Style Guide

Please read and follow [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) and use this as the basis for coding in the repository.
Further specialised conventions, for the specific use case of journey testing, are described below.

# Organisation

**Applications**

Journey tests in this repository can span multiple applications and multiple application journey tests can be created here too. To organise the objects related to these applications, such as `PageObjects` and `Locators` you must place these in an applications named folder i.e. `ioffice` is the folder for IntelligentOffice related objects and `pfp` is the folder related to PFP. 

**Page objects**

Pages, elements, locators etc should be placed in a module named according to the page in lowercase. eg: `home.py` should contain the `HomePage` class and it's related element and locator classes.

**Areas**

Applications tend to be organised into a hierarchical structures based on the information architecture. Use this as the basis for organising objects within an application folder. eg: `ioffice/clients` for the client related pages and `ioffice/clients/plans` for the plan related pages etc.

# Object Conventions

**PageObjects**

These are classes that encapsulate and model web pages.

* PageObjects must inherit from `BasePage`
* Applications must have their own base page eg: `IOfficeBasePage(BasePage)`
* PageObjects must be classes and named in Pascal case, suffixed with `Page`
* methods must be lowercase and use underscores for word boundaries

**Locators**

These are classes that encapsulate the element locators on a page. 

* Locators are classes that inherit from `object`
* Locator objects must be classes and named in Pascal case `Locators`  
* Locator descriptors should be upper cased and be tuples eg: `GO_BUTTON = (By.ID, 'submit')`
* Locators must be named based on PO Naming Convention of WebElements. Ref: https://confluence.intelliflo.com/pages/viewpage.action?pageId=51022852 
* Locators that relate to a specific page should be found in the same module as the page object.

**Input Elements**

These are classes that encapsulate an input element on a page. 

* Input Elements are classes that are or inherit from either `NamedInputElement` or `IdInputElement`
* Input Elements objects must be classes and named in Pascal case, suffixed with `Element`  

# Testing Conventions

* Use pytest
* Tests methods should be lowercase and underscores for word boundaries
* Assertions must have descriptions
* `config` argument contains the driver and other configuration variables that may be necessary in your tests.
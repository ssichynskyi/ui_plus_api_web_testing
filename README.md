# "Hey, look-at-me" project :-)
For long time I've developed only proprietary SW with no opportunity to share it. So, this project demonstrates some of my skills in automated Web testing.

## AUT
Testing is done vs locally installed WordPress website with WooCommerce plugin on it.
It runs using Apache and MySQL servers powered by MAMP PRO4.
Although there's a specific python lib available for WooCommerce, it's intentionally not used
in order to have a more general implementation.

## Tech stack
- POSeleniumbase (custom page-object wrapper for Seleniumbase framework)
- Seleniumbase (UI test framework)
- pytest
- PyMySQL
- requests
- PyYaml
- etc

## Content
- UI tests (coming soon)
- API tests
- Page Objects (coming soon) / DAO / Data Models / helpers

By any means the available test coverage cannot pretend to be complete or even sufficient.
It's just an example of what could be done.
The focus was on the framework and the eco-system rather than on a test coverage.
Also, the decision to use feature-rich Seleniumbase framework brought up some
inevitable (although not critical) tradeoffs in the quality and readability of code.

## Prerequisites
- python 3.9+ is installed
- pipenv is installed
- Website with DB is up and running
- test user creds are available in DB and in .env file
- .env file is configured based on .env.example
- config/hosts.yaml is configured
- config/hosts_local.yaml is configured from hosts_local.yaml.example

## Usage:
1. Open project folder
2. Run pipenv commands
```console
pipenv shell
pipenv install
```
3. Run tests with pytest
```console
pytest ...
```
4. ToDo:
- add verification vs DB in UI test cases
- add api-ui integration / data integrity test cases  
- add docker file to execute all tests in container

# "Hey, look-at-me" project :-)
This project demonstrates some of my skills in automated Web testing.

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
- add environment selection as a commandline arguments for pytest (?)
- ADD UI TESTS
- ADD docker file to execute all tests in container

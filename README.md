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

## Content
- UI tests
- API tests
- Page Objects / DAO / Data Models / helpers
- Test Cases

By any means the available test coverage cannot pretend to be complete or even sufficient.
It's just an example of what could be done.
The focus was on the framework and the eco-system rather than on a test coverage.

## Prerequisites
- python 3.9+ is installed
- pipenv is installed
- Website is up and running
- test user is available in DB and in .env file
- .env file is configured
- config/hosts.yaml is configured

## Usage:
1. Open project folder
2. Run env command
```console
pipenv shell
pipenv install
```
3. Run tests (pytest is recommended)
```console
pytest ...
```
4. ToDo:
- add byte check for uploaded PDF (stream comparison?)
- add environment selection as a commandline arguments for pytest (?)

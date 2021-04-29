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
- Page Objects and helpers
By any means the available test coverage cannot pretend to be complete or even sufficient.
It's just an example of what could be done

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
- add smoke test -> host availability
- add commandline arguments for pytest
- add data abstraction layer from DB
- add file upload tests (add sample files in test_api/data)
- https://pypi.org/project/pytest-testconfig/  ?? (if it makes sense to use it)

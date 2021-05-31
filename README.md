[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6ac94efb1fcb441daa03bfa27d2c712a)](https://www.codacy.com/gh/ssichynskyi/ui_plus_api_web_testing/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ssichynskyi/ui_plus_api_web_testing&amp;utm_campaign=Badge_Grade)
# "Hey, look-at-me" project :-)
For long time I've developed only proprietary SW with no opportunity to share it.
So, this project demonstrates some of my skills in automated Web testing.

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

## Tech stack for local environment
- MAMP PRO4 (with apache and mysql running on it)
- mkcert (to enable TLS/SSL)

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

## Usage
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
4. ToDo
- add docker file to execute all tests in container

- reduce boilerplate code in dynamic list elements with
  automatic search of property using dir() and filtering by "_locator"
  instead of indexing them in "member_locators" ppty

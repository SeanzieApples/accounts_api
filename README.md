# Project Title

**Description**:  AccountsAPI is an interface create and manage bank accounts
Other things to include:

## Dependencies

Requires: Python 3.10, pip3.10
Optional: Docker

## Installation

On Windows simply run the `./scripts/startup.bat`
On MacOS or Linux run `./scripts/startup.sh`
The project also includes a Dockerfile which can be run with `./scripts/docker_startup.sh`

## Usage

Once the API is running you have the following actions available

```
POST /accounts
REQUST BODY: {"name": "Account Name"}
```
Creates an account with the given name

```
GET /accounts/:account_name
```
Gets an account with the given name

```
POST /accounts/:account_name/deposit
REQUST BODY: {"amount": 10.00}
```
Desposits specified amount

```
POST /accounts/:account_name/deposit
REQUST BODY: {"amount": 10.00}
```
Withdraws specified amount

## Getting help

Once running you can reference the Swagger doc and try the API out here: http://localhost:8000/docs#/default

## Approach

Since this exercise was a simple API, I researched what Python framework was the fastest. Based on my research it seemed like FastAPI was the way to go so I chose that. I then spent some time reading over the documentation and referencing best practices for creating a clear project structure

It seemed like the best way to go about creating a simple API was to have the following:
1. Base folder that provided the application configuration and settings via a Settings class.
2. A crud folder for any operations that were performed against the database, broken up by models.
3. A db folder, which provided references to the database.
4. A models folder that used the SQLAlchemy ORM to map models to tables.
5. A routers folder that...
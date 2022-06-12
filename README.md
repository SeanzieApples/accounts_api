# Project Title

**Description**:  AccountsAPI is an interface create and manage bank accounts
Other things to include:

## Dependencies

Requires: Python 3.10
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
# Bins API - Flask

This is the code needed to create a REST API to be used as a tutorial for learning how to interact with REST APIs. The primary functionality of this API is to allow users to create virtual bins and store a string in each of those bins.

There is an interactive explorer for this API [here](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/dchosnek/bin-api-tutorial/main/openapi3.1.0.yml), but a simple overview of the API is:

🔐 **POST**   `/bins` to create a new empty bin

🔐 **GET**    `/bins/{binId}` to retrieve the contents of a specific bin

🔐 **PUT**    `/bins/{binId}` to update the contents of a specified bin

🔐 **DELETE** `/bins/{binId}` to permanently delete a bin


All of the above methods require a token (API key) that identifies the user. Normally a user would be issued a token from the system being accessed via some web page. To keep this tutorial simple, insecure methods have been added for generating and validating a token.

  **GET** `/token?email={email}` to generate an expiring token

  **GET** `/token/{token}` to verify if the specified token is still valid

  More details of the exact format of each request and response are available in the [spec](openapi3.1.0.yml) or the interactive [guide](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/dchosnek/bin-api-tutorial-flask/main/openapi3.1.0.yml).

- - -

## Implementation details

This can be run locally following the step below (setting up environment variables and running a local instance of a database). If it will be deployed at any scale, it is recommended to use Gunicorn.

### Environment variables

For local machine development, using these EVs:

```
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
```

### Docker

Run a mongo container that can be accessed by the local Flask server

```
docker run --name some-mongo -p 27017:27017 -d mongo:latest
```

### Running the app

With the database operational and the EVs set, simply type

```
flask run
```
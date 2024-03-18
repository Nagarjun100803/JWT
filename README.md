# JWT

FastAPI Authentication Example
This is a simple FastAPI application demonstrating user authentication, token generation, and accessing protected resources using JSON Web Tokens (JWT).

There are three endpoints, each serving a specific purpose. Here's a brief overview of each endpoint

# 1st end point is /register/ [POST]
  Description: Registers a new user in the system.
  Request Body:
    {
      "username": "string",
      "email": "string",
      "password": "string",
      "age": "integer",
      "level": "enum"
    }
  ##Response:
  Status Code: 200 OK
  ##Body:
    {
    "id": "integer",
    "username": "string",
    "email": "string",
    "age": "integer",
    "level": "enum"
  }
  ##Responsibilities:
    Checks if the username and email are unique.
    Hashes the password before storing it in the database.
    Returns the registered user data.


#2nd endpoint is  /token [POST]

  ##Description: Generates an access token for authentication.
  ##Request Body:
    {
      "username": "string",
      "password": "string"
    }
  ##Response:
  `Status Code: 200 OK
  ##Body:
    {
      "access_token": "string",
      "token_type": "string"
    }
  ##Responsibilities:
    Validates the username and password.
    Generates and returns an access token.
#3rd endpoint is /conversation [GET]

  ##Description: Retrieves conversation data.
  ##Response:
  Status Code: 200 OK
  Body:
    {
      "conversation": "string",
      "current_user": "string"
    }
  ##Responsibilities:
    Retrieves conversation data.
    Gets the current user's username for the response.

These endpoints collectively handle user registration, authentication token generation, and conversation data retrieval. The /register/ endpoint allows users to register by providing their username, email, password, age, and level. The /token endpoint generates an access token for authentication based on the provided username and password. The /conversation endpoint retrieves conversation data and includes the username of the current user in the response.




  

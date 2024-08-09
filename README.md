# Personal Portfolio Website (Python Flask Backend)

This is the backend server for the Personal Portfolio Website. The backend is built using Python and Flask, and it provides the necessary APIs to handle contact form submissions and other server-side operations.

## Features
- Flask: The lightweight web framework used to build the backend server.
  
- Flask-CORS: Handles Cross-Origin Resource Sharing (CORS), making it possible to interact with the front-end hosted on different origins.
  
- SMTP: Integrated with Gmail SMTP server to send email notifications when the contact form is submitted.
  
- Front-end library: React
  
- CSS framework: React-bootstrap
  
- CSS animations library: Animate.css

## Installation
1. Clone the repository:
   
### `git clone https://github.com/your-username/python-flask-backend.git`
### `cd python-flask-backend`

2. Create a virtual environment:

### `python3 -m venv venv`
### `source venv/bin/activate`

3. Set up environment variables:

### `FLASK_APP=app.py`
### `FLASK_ENV=development`
### `SENDER_EMAIL=your-email@gmail.com`
### `SENDER_PASSWORD=your-email-password`
### `RECEIVER_EMAIL=receiver-email@gmail.com`

## Running the Server

### `flask run`

## API Endpoints
## POST `/contact`

This endpoint handles contact form submissions and sends an email notification to the specified receiver email.

Request:

Method: `POST`

Content-Type: application/json

Body: JSON object containing:

firstName: User's first name

lastName: User's last name

email: User's email address

phone: User's phone number

message: The message from the user



## POST `/subscribe`

This endpoint handles subscription.

Request:

Method: `POST`

Content-Type: application/json

Email: User's email address

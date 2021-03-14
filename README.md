# Python URL Shortener

## Overview

This application provides the user with the ability to shortern urls.

This application uses a MySQL Database and a Flask RESTful API with three endpoints:

`GET /health` - Returns a "Hello World!" message and a 200 response code.

`POST /generate` - Generates a unique short url. Include body like below:

```json
{
  "url": "http://www.mysite.co.uk"
}
```

`GET /<hash>` - Redirects the user to the original url.

## Instructions

Coming Soon...

## Deployment

### Running Locally (Host)

1. Create Virtual Environment `python3 -m venv venv`
2. Activate Virtual Environment `source venv/bin/activate`
3. Install Packages `pip3 install -r requirements.txt`
4. Start Server `python3 src/server.py`

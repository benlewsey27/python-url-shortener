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

## Deployment

Before deployment, a `.env` file should be created in the root directory.

The contents of this file should be as below:

```bash
MYSQL_HOST=mysql
MYSQL_USER=XXXXX
MYSQL_PASSWORD=XXXXX
MYSQL_DATABASE=XXXXX
```

### Local Deployment (Docker)

Run the application with the instructions below:

```bash
docker-compose build
docker-compose up

# The application can be accessed on localhost:3000...

docker-compose down
```

### Cloud Deployment

Coming Soon!

## Instructions

1. Generate a new short URL by running:

```
curl -X POST -H "Content-type: application/json" -d '{"url":"https://www.google.co.uk"}' localhost:3000/generate
```

Example Response:

```json
{
  "status": 200,
  "message": "URL generated successfully",
  "url": "http://localhost:3000/7698461393916768163"
}
```

2. Go to the provided URL from Step 1. If successful, you will be redirected to the original URL.

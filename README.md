# Work in progress

This repo contains partially completed work.

At this point, the Flask server appears to be working and approximates the behavior of the serverless implementation of this API implemented [here](https://github.com/dchosnek/bin-api-tutorial-aws).

- - -

### Environment variables

Currently using these EVs:

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
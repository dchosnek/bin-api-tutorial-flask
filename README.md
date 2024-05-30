# Work in progress

This repo contains a working prototype of the API implemented [here](https://github.com/dchosnek/bin-api-tutorial-aws).

The next step is to combine this backend API with the frontend web UI into a single VM. That frontend UI (react.js) is implemented [here](https://github.com/dchosnek/bin-api-tutorial-react).

- - -

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
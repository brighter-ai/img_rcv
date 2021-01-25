# Sample multi-part image receiver
This project was setup to provide simple server which can receive an image as part of a multi-part form-data request.  
This is intended for easier debugging of the following issue:
https://github.com/readmeio/api-explorer/issues/1078

## Prerequisites
You will need `pipenv` and `python3.8` in order to run this project. 
I recommend using [pyenv](https://github.com/pyenv/pyenv) for managing your local python versions. 
To install pipenv simply run `pip install pipenv`.

## Running the server 
Simply call `make` in order to install all necessary dependencies and start the server. 
For subsequent runs a simple `make run` will skip the requirements step.

## Sending a request to the server

You can send the sample image provided in this repo with the following `curl` command:
```bash
curl --request POST \
  --url http://localhost:5000/upload \
  --form file=@pixel.png
```

The server will respond with a `file` string containing the received bytes and a `success` field which indicates whether `pillow` was able to read the image.


## Using with api-explorer
This repo also provides a `debug-multipart-file-upload.json` OAS3 specification to test `api-explorer`. 
Simply put it into the `examples/swagger-files` directory of `api-explorer` and disable proxying of requests. 
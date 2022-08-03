from flask import Flask, Response, send_file
from os.path import exists
import tempfile
from fastapi import FastAPI, status, HTTPException, Depends
import logging


app = Flask(__name__)

@app.route("/ping")
async def ping():
    file_exists = exists(tempfile.gettempdir() + '/ok.txt')
    return Response("File found",status.HTTP_200_OK) if file_exists else Response("",status.HTTP_503_SERVICE_UNAVAILABLE)

@app.route("/img")
async def img():
    logging.info("GET request,/img")
    return send_file("img.gif", mimetype='image/gif')

    
if __name__ == "__main__":
    app.run(debug=True)

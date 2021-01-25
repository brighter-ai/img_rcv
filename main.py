from flask import Flask, request
from flask_cors import CORS
from PIL import Image, UnidentifiedImageError

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def receive_image():
    file = request.files.get('file')

    success = True

    try:
        Image.open(file)
    except UnidentifiedImageError:
        success = False

    return {
        "success": success,
        "file": str(file.read()),
    }

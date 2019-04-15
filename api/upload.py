from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask import request, current_app as app


photos = UploadSet('photos', IMAGES)


def upload_file():
    if request.method == 'POST' and 'file' in request.files:
        filename = photos.save(request.files['file'])
        return "saved"

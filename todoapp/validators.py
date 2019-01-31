import os
import magic
import zipfile
from django.core.exceptions import ValidationError

def validate_is_zip_or_image(file):
    valid_mime_types = ['application/zip','image/jpeg','image/png']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type')
        
    valid_file_extensions = ['.jpeg','.jpg', '.png','.zip']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unsupported file extension')

def size_validator(file):

    if (zipfile.is_zipfile(file)):
        totalSize = 0
        with zipfile.ZipFile(file, 'r') as zip: 
            for info in zip.infolist():
                totalSize += info.file_size
        if (totalSize > 5242880):
            raise ValidationError('File is too big')
    else:
        if (file.size > 5242880):
            raise ValidationError('File is too big')

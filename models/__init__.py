#!/usr/bin/python3
'''Global variable initialized as class FileStorage'''
from models.engine.file_storage import FileStorage


'''instance of FileStorage'''
storage = FileStorage()

'''reload() method called on storage instance'''
storage.reload()

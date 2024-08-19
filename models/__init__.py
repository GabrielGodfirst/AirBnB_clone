#!/usr/bin/python3
"""
Initialize the models package and create a unique FileStorage instance.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

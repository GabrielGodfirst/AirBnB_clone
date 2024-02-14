#!/usr/bin/python3
"""
Module: __init__.py

Initializes the models package and creates a unique FileStorage instance
for the application.
"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()

# Call the reload() method on the storage variable
storage.reload()

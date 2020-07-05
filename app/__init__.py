from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config= True)

#set configurations
app.config.from_object(DevConfig) 
app.config.from_pyfile('cofig.py')

from app import views
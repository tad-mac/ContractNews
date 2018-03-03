from flask import Flask
from config import Config
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)


from app import views

login = LoginManager(app)

app.config.from_object('config')

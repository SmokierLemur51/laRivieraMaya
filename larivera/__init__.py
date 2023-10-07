from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="/static")
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    
    from canteen.main.routes import main
    app.register_blueprint(main, url_prefix="/")

    from canteen.score.routes import score
    app.register_blueprint(score, url_prefix="/score")

    from canteen.notes.routes import notes
    app.register_blueprint(notes, url_prefix="/notes")

    from canteen.larivera.routes import rivera
    app.register_blueprint(riviera, url_prefix="/riviera")
    
    return app

app = create_app()

# my tables, because screw flask-sqlalchemy!!!
from .models import create_table



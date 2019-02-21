from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()

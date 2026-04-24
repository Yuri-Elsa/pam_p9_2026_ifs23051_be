from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from routes.auth_routes import auth_bp
    from routes.recipe_routes import recipe_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(recipe_bp, url_prefix="/recipes")

    with app.app_context():
        db.create_all()

        # Seed admin di dalam app_context yang sama
        from models.user import User
        from werkzeug.security import generate_password_hash

        if not User.query.filter_by(username="admin").first():
            admin = User(
                username="admin",
                password=generate_password_hash("admin123"),
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print("[SEED] Admin account created: admin / admin123")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8080)
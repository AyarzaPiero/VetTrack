from flask import Flask
from .config import Config
from .db import db
from .routes.pet_routes import pet_bp
import os

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Generar una clave secreta para la sesión si no existe
    if not app.config.get('SECRET_KEY'):
        app.config['SECRET_KEY'] = os.urandom(24).hex()
        
    # Inicializar las extensiones
    db.init_app(app)

    # Crear todas las tablas en la base de datos
    with app.app_context():
        db.create_all()

    # Registrar blueprints
    app.register_blueprint(pet_bp)
    
    # Manejo de errores
    register_error_handlers(app)

    return app

def register_error_handlers(app):
    """Registrar manejadores de errores personalizados"""
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500
        
# Importación para evitar error de referencia circular
from flask import render_template
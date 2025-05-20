import os

class Config:
    """Configuración base de la aplicación"""
    
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://usuario_remoto:sgrmgebg@3.21.93.239:3306/vettrack"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de la aplicación Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_predeterminada'
    
    # Configuración de subida de archivos
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    
    # Configuración de sesiones
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 1800  # 30 minutos
    
    # Configuración de zona horaria
    TIMEZONE = 'America/Mexico_City'

class DevelopmentConfig(Config):
    """Configuración para el entorno de desarrollo"""
    DEBUG = True
    
class ProductionConfig(Config):
    """Configuración para el entorno de producción"""
    DEBUG = False
    
    # Es mejor establecer estas variables desde el entorno en producción
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or Config.SQLALCHEMY_DATABASE_URI
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Opciones de seguridad adicionales para producción
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = True
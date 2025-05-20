from app import create_app
from app.config import DevelopmentConfig, ProductionConfig
import os

# Determinar el entorno de ejecución
env = os.environ.get('FLASK_ENV', 'development')

# Crear la aplicación con la configuración correspondiente
if env == 'production':
    app = create_app(ProductionConfig)
else:
    app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    # Ejecutar la aplicación en modo debug en desarrollo
    app.run(host='0.0.0.0', port=5000, debug=(env == 'development'))
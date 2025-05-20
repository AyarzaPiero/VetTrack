# 🐾 VetTrack – Sistema de Registro de Mascotas

VetTrack es una aplicación web desarrollada en Python con Flask, diseñada para digitalizar el proceso de registro de mascotas de una veterinaria. Permite registrar mascotas junto con el nombre de su dueño, y visualizar una lista de mascotas registradas.

---

## 📌 Funcionalidades

- Registrar una mascota (nombre + nombre del dueño)
- Ver listado de mascotas registradas
- Persistencia de datos en base de datos MySQL
- Arquitectura en 3 capas (presentación, aplicación, datos)
- Despliegue en AWS EC2

---

## 🖼️ Arquitectura del sistema

**Modelo de despliegue:**

      +-------------------+         HTTPS/SSH        +---------------------+
      |  EC2 (Flask App)  |  <-------------------->  |  EC2 (MySQL Server) |
      |   Puerto 5000     |                         |     Puerto 3306     |
      +-------------------+                         +---------------------+
                |
                v
     Acceso vía IP pública (Navegador)


**Capas del sistema:**
- 🖥️ Presentación: HTML con Jinja2 (formularios y listas)
- 🧠 Aplicación: Flask con servicios separados por lógica
- 💾 Datos: MySQL como backend relacional

---

## 🚀 Despliegue

### 🔧 Requisitos

- Python 3.10+
- MySQL Server (instancia EC2 separada)
- Conexión a Internet (puerto 5000 abierto en EC2)
- Linux (Ubuntu 22.04 en EC2)

### 🛠️ Instrucciones para desplegar

1. **Crear y conectar a una EC2 (para Flask):**
   - AMI: Ubuntu 22.04
   - Grupo de seguridad con puertos 22 (SSH) y 5000 (HTTP)
   - Conéctate por EC2 Instance Connect

2. **Instalar dependencias:**

```bash
sudo apt update && sudo apt install python3-pip python3-venv git -y
```

3. **Clonar el proyecto:**
```bash
git clone https://github.com/tu_usuario/vettrack.git
cd vettrack
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. **Ejecutar la aplicacion:**
```bash
python run.py
```
5. **Acceder:**
```bash
http://IP_PUBLICA_EC2:5000
```

## 📋 Explicación de la arquitectura en 3 capas

- **Capa de presentación:** templates/ y routes/pet_routes.py, donde se definen las vistas HTML y navegación.
- Capa de aplicación: services/pet_service.py, que gestiona la lógica de negocio.
- Capa de datos: models/pet_model.py y db.py, que definen los modelos y conexión a MySQL.

## Seguridad

- Se uso 

## 🖼️ Evidencia del despliegue
### Capturas
![Paginaweb](https://github.com/AyarzaPiero/VetTrack/blob/main/assets/paginafuncionando.png)
![Instanciadbv1](https://github.com/AyarzaPiero/VetTrack/blob/main/assets/instanciapython.png)
![Instanciadbv1](https://github.com/AyarzaPiero/VetTrack/blob/main/assets/paginafuncionando.png)

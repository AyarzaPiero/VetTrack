# 🐾 VetTrack – Sistema de Registro de Mascotas

VetTrack es una aplicación web desarrollada en Python con Flask, diseñada para digitalizar el proceso de registro de mascotas de una veterinaria. Permite registrar mascotas junto con el nombre de su dueño, y visualizar una lista de mascotas registradas.

---

## 📌 Funcionalidades

- Registrar una mascota (nombre + nombre del dueño + espcecie + raza + fecha de registro y fecha de actualizacion etc)
- Ver listado de mascotas registradas
- Persistencia de datos en base de datos MySQL
- Arquitectura en 3 capas (presentación, aplicación, datos)
- Despliegue en AWS EC2

---

## 🖼️ Arquitectura del sistema

**Modelo de despliegue:**

![Instanciadbv1](https://github.com/AyarzaPiero/VetTrack/blob/main/assets/diagrama.png)

**Capas del sistema:**
- 🖥️ Presentación: HTML minimalista, elegantes con animaciones interactivas y varias vistas
- 🧠 Aplicación: Flask con servicios separados por lógica
- 💾 Datos: MySQL como backend relacional

---

## 🚀 Despliegue

### 🔧 Requisitos

- Python 3.10+
- MySQL Server (instancia EC2 separada)
- Conexión a Internet (puerto 5000 abierto en EC2)
- Linux (Ubuntu 22.04 en EC2)

### 🛠️ Instrucciones para desplegar Instancia 1

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

> [!WARNING]
> Debe editar el archivo ```app/config.py``` para que coincida con su instancia: ```SQLALCHEMY_DATABASE_URI = "mysql+pymysql://usuario:contraseña@IP_EC2_DB:3306/vettrack"```

4. **Ejecutar la aplicacion:**
```bash
python run.py
```
5. **Acceder:**
```bash
http://IP_PUBLICA_EC2:5000
```

### 🛠️ Instrucciones para desplegar Instancia 2

1. **Crear y conectar a una EC2 (para base de datos):**
   - AMI: Ubuntu 22.04
   - Grupo de seguridad de tipo MySQL/Aurora - TCP (3306)
   - Conéctate por EC2 Instance Connect

2. **Instalar dependencias:**
```bash
sudo apt update
sudo apt install -y mariadb-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo mysql_secure_installation
```

2. **Crear la base de datos y usuario:**
```bash
sudo mysql
```

```bash
CREATE DATABASE vettrack;
CREATE USER 'usuario_java'@'%' IDENTIFIED BY 'tu_clave_segura';
GRANT ALL PRIVILEGES ON vettrack.* TO 'usuario_java'@'%';
FLUSH PRIVILEGES;
EXIT;
```

2. **Crear tabla:**
```bash
USE vettrack
CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    owner VARCHAR(100) NOT NULL,
    species VARCHAR(50),
    breed VARCHAR(50),
    age INT,
    gender VARCHAR(20),
    color VARCHAR(50),
    notes TEXT,
    vaccinated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
);
```

> [!WARNING]
> Edite el archivo ```/etc/mysql/mariadb.conf.d/50-server.cnf``` para permitir conexiones externas asi: ```bind-address = 0.0.0.0```

## 📋 Explicación de la arquitectura en 3 capas

- **Capa de presentación:** templates/ y routes/pet_routes.py, donde se definen las vistas HTML y navegación.
- **Capa de aplicación:** services/pet_service.py, que gestiona la lógica de negocio.
- **Capa de datos:** models/pet_model.py y db.py, que definen los modelos y conexión a MySQL.

## Seguridad

- Se uso **Fail2Ban** para bloquear IPs que realizan comportamientos sospechosos (como intentos fallidos de login repetidos).

```bash
[sshd]
enabled = true
port    = ssh
logpath = %(sshd_log)s
maxretry = 5
bantime = 3600
```

## 🖼️ Evidencia del despliegue
### Aplicacion funcionando
![Paginaweb](https://github.com/AyarzaPiero/VetTrack/blob/main/assets/paginafuncionando.png)
![Paginaweb](https://raw.githubusercontent.com/AyarzaPiero/VetTrack/refs/heads/main/assets/e2.png)

### Despliegue
![Instanciadbv1](https://github.com/AyarzaPiero/VetTrack/blob/main/assets/e3.png)
![Instanciadbv1](https://github.com/AyarzaPiero/VetTrack/blob/main/assets/e4.png)
![Instanciadbv1](https://github.com/AyarzaPiero/VetTrack/blob/main/assets/instanciapython.png)
![Instanciadbv1](https://github.com/AyarzaPiero/VetTrack/blob/main/assets/instanciabasededatos.png)

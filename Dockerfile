# Usa una imagen base de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

# Exponer el puerto que usará la API de Flask
EXPOSE 5000

# Definir el comando para ejecutar la aplicación
CMD ["python", "app.py"]

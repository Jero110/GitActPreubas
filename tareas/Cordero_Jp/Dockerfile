# Utiliza una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu aplicación (opcional)
COPY . /app/

# Comando para ejecutar la aplicación (ajusta según sea necesario)
CMD ["python", "prueba1.py"]

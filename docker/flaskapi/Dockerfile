# Empezamos de una imagen de python ligero
FROM python:3.8-slim-buster
# Nuestro contenedor tendrá una carpeta llamada app, dentro de esta carpeta estará disponible todo el código
# y servirá como raiz del proyecto, el comando WORKDIR crear la carpeta y automáticamente hace CD a la carpeta
WORKDIR /app
# de mi máquina local copia el archivo requirements.txt al contenedor con el nombre requirements.txt
COPY requirements.txt requirements.txt
# En el contenedor instala los requisitos de python
RUN pip3 install -r requirements.txt
# Termina de copiar todo lo que había en la carpeta raíz del proyecto local al contenedor
COPY . .
# Ejecuta el servidor flask en el host 0.0.0.0 y puerto 8181
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8181"]

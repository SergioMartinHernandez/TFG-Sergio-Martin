# Herramienta para el análisis de datos en Twitter
## Instrucciones de uso mediante descarga del proyecto
**Requisitos previos:** 
Tener instalado [docker](https://docs.docker.com/desktop/windows/install/) y [docker compose](https://docs.docker.com/compose/install/) en nuestro equipo.
1. Descargar el zip con el proyecto y descomprimirlo.
2. Abrir una terminal desde la carpeta del proyecto.
3. Ejecutar la orden *docker-compose up -d --build*.

## Instrucciones de uso mediante VPS
**Requisitos previos:** 
Tener instalado [putty](https://www.putty.org/) en nuestro equipo.
1. Descargar el archivo *clavePrivadaVPS.ppk* del repositorio.
2. Abrir una sesión de putty.
3. En la pestaña *Session* introducir **ubuntu@141.145.196.17** en el campo *Host Name*.
3. En la pestaña *Connection/Ssh/Auth* adjuntar nuestro archivo anteriomente descargado en el campo *Private key file for authentication*.
4. Hacer click en el botón *Open* de la parte inferior derecha.
5. Una vez abierto el terminal ejecutar la orden *sudo docker-compose up -d --build*.

**En ambos casos acceder a la dirección http://localhost:8080 para encontrar la pantalla principal de la aplicación.**

FROM node:lts-alpine

# hacer la carpeta 'app' el directorio de trabajo actual
WORKDIR /app

# copiar 'package.json' y 'package-lock.json' (si están disponibles)
COPY package*.json ./

# instalar dependencias del proyecto
RUN npm install

# copiar los archivos y carpetas del proyecto al directorio de trabajo actual (es decir, la carpeta 'app')
COPY . .

CMD ["npm", "run", "dev_mode"]

# CMD ["npm", "run", "build"]

# RUN npm install -g serve

# RUN serve -s dist
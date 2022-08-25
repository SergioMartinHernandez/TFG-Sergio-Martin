# FROM node:lts-alpine

# WORKDIR /app

# ENV PATH /app/node_modules/.bin:$PATH

# RUN npm install @vue/cli -g
# RUN npm i --save chart.js
# RUN npm i --save vue-chartjs
# RUN npm install --save axios vuex vuex-persistedstate bootstrap@4.0

# COPY package.json .
# COPY package-lock.json .
# RUN npm install

# CMD ["npm", "run", "serve"]

FROM node:lts-alpine

# hacer la carpeta 'app' el directorio de trabajo actual
WORKDIR /app

# copiar 'package.json' y 'package-lock.json' (si están disponibles)
COPY package*.json ./

# instalar dependencias del proyecto
RUN npm install

# copiar los archivos y carpetas del proyecto al directorio de trabajo actual (es decir, la carpeta 'app')
COPY . .

CMD ["npm", "run", "serve"]
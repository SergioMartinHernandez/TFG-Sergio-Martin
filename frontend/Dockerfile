FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli -g
# RUN npm i vue-chartjs chart.js
RUN npm install --save axios vuex vuex-persistedstate bootstrap@4.0

COPY package.json .
COPY package-lock.json .
RUN npm install

CMD ["npm", "run", "serve"]
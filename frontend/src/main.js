import 'bootstrap/dist/css/bootstrap.css';
// Es un cliente HTTP
import axios from 'axios';
import Vue from 'vue';

import App from './App.vue';
import router from './router';
import store from './store';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';  // Direccion del backend

// SOLO QUITA UN MENSAJE AL HACER F12 EN LA PAGINA WEB
//Vue.config.productionTip = false;

// Para que desloguee al usuario cuando pasen 30 minutos
// axios.interceptors.response.use(undefined, function (error) {
//   if (error) {
//     const originalRequest = error.config;
//     if (error.response.status === 401 && !originalRequest._retry) {
//       originalRequest._retry = true;
//       store.dispatch('logOut');
//       return router.push('/login')
//     }
//   }
// });

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
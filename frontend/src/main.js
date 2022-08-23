import 'bootstrap/dist/css/bootstrap.css';
// Es un cliente HTTP
import axios from 'axios';
import Vue from 'vue';

import App from './App.vue';
import router from './router';
import store from './store';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

// Cierra sesion al usuario cuando pasen 30 minutos del token de autentificacion
axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config;
    if ((error.response.status === 401 || error.response.status=== 403) && !originalRequest._retry) {
      originalRequest._retry = true;
      store.dispatch('logOut');
      return router.push('/login')
    }
  }
});
try {
  window.$ = window.jQuery = require('jquery');
  window.Popper = require('popper.js').default;
  require('bootstrap');
} catch (e) {}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
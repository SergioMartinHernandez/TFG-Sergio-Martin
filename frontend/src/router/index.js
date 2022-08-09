import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home.vue'
import LogIn from '@/views/LogIn.vue';
import SignUp from '@/views/SignUp.vue';
import Account from '@/views/Account.vue';
import Analysis from '@/views/Analysis.vue';
import BarChart from '@/views/graphs/BarChart.vue';
import SearchHistory from '@/views/SearchHistory.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
    meta: {requiresAuth: true}
  },
  {
    path: '/account',
    name: 'Account',
    component: Account,
    meta: {requiresAuth: true}
  },
  {
    path: '/analysis',
    name: 'Analysis',
    component: Analysis,
    meta: {requiresAuth: true}
  },
  {
    path: '/searchhistory',
    name: 'SearchHistory',
    component: SearchHistory,
    meta: {requiresAuth: true}
  },
  {
    path: '/bar',
    name: 'Bar',
    component: BarChart
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

// Para asegurarse que un usuario no logueado entre a secciones que no deberia entrar 
// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     if (store.getters.isAuthenticated) {
//       next();
//       return;
//     }
//     next('/login');
//   } else {
//     next();
//   }
// });

export default router;
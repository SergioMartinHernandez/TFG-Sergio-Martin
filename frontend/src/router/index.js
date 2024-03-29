import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'; 

import Home from '@/views/Home.vue'
import LogIn from '@/views/LogIn.vue';
import SignUp from '@/views/SignUp.vue';
import Search from '@/views/Search.vue';
import Account from '@/views/Account.vue';
import UserAnalysis from '@/views/UserAnalysis.vue';
import TweetAnalysis from '@/views/TweetAnalysis.vue';
import SearchHistory from '@/views/SearchHistory.vue';
import TweetSaved from '@/views/TweetSaved.vue';
import Faq from '@/views/FAQ.vue';
import About from '@/views/About.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
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
  },
  {
    path: '/search',
    name: 'Search',
    component: Search,
    meta: {requiresAuth: true}
  },
  {
    path: '/account',
    name: 'Account',
    component: Account,
    meta: {requiresAuth: true}
  },
  {
    path: '/useranalysis',
    name: 'UserAnalysis',
    component: UserAnalysis,
    meta: {requiresAuth: true}
  },
  {
    path: '/searchhistory',
    name: 'SearchHistory',
    component: SearchHistory,
    meta: {requiresAuth: true}
  },
  {
    path: '/tweetanalysis',
    name: 'TweetAnalysis',
    component: TweetAnalysis,
    meta: {requiresAuth: true}
  },
  {
    path: '/tweetsaved',
    name: 'TweetSaved',
    component: TweetSaved,
    meta: {requiresAuth: true}
  },
  {
    path: '/faq',
    name: 'Faq',
    component: Faq,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

// Para asegurarse que un usuario no logueado entre a secciones que no deberia entrar 
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;
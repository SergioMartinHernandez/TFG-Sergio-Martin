import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import users from './user';
//import searchs from './searchs';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    //searchs,
    users,
  },
  plugins: [createPersistedState()]
});
import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

//import tweets from './modules';
import users from './modules';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    //tweets,
    users,
  },
  plugins: [createPersistedState()]
});
import axios from 'axios';

const state = {
  user: null,
  searchs: null,
  search: null,
  userSearch: null,
  tweetSearch: null
};

const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
  stateSearchs: state => state.searchs,
  stateUserSearch: state => state.userSearch,
  stateTweetSearch: state => state.tweetSearch,
};

const actions = {
  async signUp({dispatch}, form) {
    await axios.post('signup', form);
    let UserForm = new FormData();
    UserForm.append('username', form.username);
    UserForm.append('password', form.password);
    await dispatch('logIn', UserForm);
  },
  async logIn({dispatch}, user) {
    await axios.post('login', user);
    await dispatch('viewMe');
  },
  async viewMe({commit}) {
    let {data} = await axios.get('/users/me/');
    await commit('setUser', data);
  },
  async updateUser({}, updatedUser) {
    console.log(updatedUser)
    await axios.patch('updateUser/', updatedUser);
  },
  async deleteUser({}, id) {
    await axios.delete(`deleteUser/${id}`);
  },
  async logOut({commit}) {
    let user = null;
    commit('logout', user);
  },
  async createSearch({},search) {
    await axios.post('user/search/', search);
    //await dispatch('getNotes');
  },
  async viewUserSearch({commit}) {
    let {data} = await axios.get('search/user/');
    await commit('setUserSearch', data);
  },
  async viewTweetSearch({commit}) {
    let {data} = await axios.get('search/tweets/');
    await commit('setTweetSearch', data);
  }
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  setUserSearch(state, userSearch) {
    state.userSearch = userSearch;
  },
  setTweetSearch(state, tweetSearch) {
    state.tweetSearch = tweetSearch;
  },
  logout(state, user){
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
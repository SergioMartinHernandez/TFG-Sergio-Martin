import axios from 'axios';

const state = {
  searchs: null,
  search: null
};

const getters = {
  stateSearchs: state => state.searchs,
  stateSearch: state => state.search,
};

const actions = {
  async createSearch(search) {
    console.log(this.search)
    await axios.post('user/search/', search);
    //await dispatch('getNotes');
  },
  // async getTweets({commit}) {
  //   let {data} = await axios.get('tweets');
  //   commit('setTweets', data);
  // },
  // async viewTweet({commit}, id) {
  //   let {data} = await axios.get(`tweet/${id}`);
  //   commit('setTweet', data);
  // },
  // eslint-disable-next-line no-empty-pattern
//   async updateNote({}, note) {
//     await axios.patch(`note/${note.id}`, note.form);
//   },
  // eslint-disable-next-line no-empty-pattern
  // async deleteTweet({}, id) {
  //   await axios.delete(`tweet/${id}`);
  // }
};

const mutations = {
  setTweets(state, tweets){
    state.tweets = tweets;
  },
  setTweet(state, tweet){
    state.tweet = tweet;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
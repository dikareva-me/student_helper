import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: {
      id:'',
      username: '',
      email: '',
    },
    isAuthenticated: false,
    token: ''
  },
  getters: {},
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username')
        state.user.email = localStorage.getItem('email')
        state.user.id = localStorage.getItem('userid')
        console.log(state.isAuthenticated)
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.username = ''
        state.user.id = ''
        state.user.email = ''
      }
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
      
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
      state.user.id = ''
      state.user.username = ''
      state.user.email = ''
        
    },
    setUser(state, user) {
      state.user = user
    }
  },
  actions: {},
  modules: {},
});

import Vuex from 'vuex';

Vue.use(Vuex)
import { createStore } from 'vuex'

export default new Vuex.createStore({
  state: {
    user: {
      username: ''
    },
    isAuthenticated: false,
    token: ''
  },
  mutations: {
    initializeStore(state) {
        console.log("Initializing store");
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})

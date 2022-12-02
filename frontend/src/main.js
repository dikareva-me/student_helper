import Vue from "vue";
import App from "./App.vue";
import store from './store'
import router from "./router";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

//createApp(App).use(store).use(router, axios).mount('#app')

new Vue({
  router,
  vuetify,
  store: store,
  render: (h) => h(App),
}).$mount("#app");

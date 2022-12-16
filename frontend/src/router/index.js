import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import MainPage from "../views/MainPage.vue";
import UserProfile from "../views/UserProfile.vue"

import SignUp from "../views/SignUp.vue";
import LogIn from "../views/LogIn.vue";

import store from '../store'


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/main-page"
 //   name: "home",
  //  component: HomeView
  },
  {
    path: "/main-page",
    name: "MainPage",
    component: MainPage,
    meta: {
      requireLogin: true
    }
  },
  {
    path: "/user-profile",
    name: "UserProfile",
    component: UserProfile,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});


router.beforeEach((to, from, next) => {
  store.commit('initializeStore');
  if ( to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
   /* next({
      path: 'log-in',
      replace: true
    });*/
    next('/log-in');
    console.log(to.matched.some(record => record.meta.requireLogin));
    console.log("store.state.isAuthenticated=", store.state.isAuthenticated);
    
  } else {
    next()
  }
})

export default router;

<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Student helper</v-toolbar-title>
        
      <div class="navbar-menu">
        <div class="navbar-end">

          <template v-if="$store.state.isAuthenticated">
            <div class="navbar-item">
              <div class="buttons">
                
                <router-link to="/main-page" class="button is-success"><strong>Главная страница</strong></router-link>
                <router-link to="/user-profile" class="button is-light">Профиль</router-link>
              </div>
            </div>      
          </template>

          <template v-else>
            <div class="navbar-item">
              <div class="buttons">
                  <router-link to="/sign-up" class="button is-success"><strong>Зарегистрироваться</strong></router-link>
                  <router-link to="/log-in" class="button is-light">Войти</router-link>
                </div>
            </div> 
          </template>
                      
          </div> 
        </div>



    </v-app-bar>

    <v-main>
    
    <section class="section">
      <router-view/>
    </section>


    </v-main>
  </v-app>
</template>



<script>

import axios from "axios";
export default {
  name: "App",
  beforeCreate() {
      console.log(localStorage.getItem('token'))
      const token = this.$store.state.token;

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },

};
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>

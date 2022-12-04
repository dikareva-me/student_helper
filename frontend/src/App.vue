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
    <!--  
      <template v-if="$store.state.isAuthenticated">
        <v-container>
          
          <v-btn
            v-if="allTasksMode"
            color="primary"
            elevation="6"
            @click="createTask"
          >
            Создать новое задание
          </v-btn>
        </v-container>

        <template v-if="newTaskMode">
          <AddTask @hide-new-task="hideNewTask" />
        </template>

          <v-alert
          color="red"
          v-if="taskDel"
          >
          Задание удалено.
          </v-alert>
                
        <template v-if="taskPageMode">
          <Task @hide-task="hideTask" :task="task" />
        </template>


        <template v-if="allTasksMode">
          <AllTasks @task-page="taskPage" />
        </template>
      </template>
      
      <template v-else>
     
      </template> -->

         <section class="section">
      <router-view/>
    </section>


    </v-main>
  </v-app>
</template>



<!--
<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Invoicely</strong></router-link>
      </div>

      <div class="navbar-menu">
        <div class="navbar-end">
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/dashboard/my-account" class="button is-light">My account</router-link>
              </div>
            </div>      
          </template>

          <template v-else>
            <router-link to="/" class="navbar-item">Home</router-link>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/sign-up" class="button is-success"><strong>Sign up</strong></router-link>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </div>
            </div> 
          </template>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>
-->

<script>

import axios from "axios";
import AddTask from "@/components/AddTask";
//import Test from '@/components/Test';
import Task from "@/components/Task";
import AllTasks from "@/components/AllTasks";
import SignUp from "@/views/SignUp";
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

  components: {
    AllTasks,
    Task,
    AddTask,
    SignUp,
  },
  data() {
    return {
      taskList: [],
      taskDel:false,
      newTaskMode: false,
      allTasksMode: true,
      taskPageMode: false,
      task: null,
    };
  },
  methods: {
    setFlagsFalse(){
      this.newTaskMode = false;
      this.allTasksMode = false;
      this.taskPageMode = false;
      this.taskDel = false;

    },

    hideNewTask() {
      this.setFlagsFalse();
      this.allTasksMode = true;
    },

    createTask() {
      this.setFlagsFalse();
      this.newTaskMode = true;
    },

    taskPage(event) {
      this.setFlagsFalse();
      this.task = event;
      this.taskPageMode = true;
    },

    hideTask(e){
      this.setFlagsFalse();
      console.log(e);
      this.taskDel = e;
      this.allTasksMode = true;
    }


  },
};
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>

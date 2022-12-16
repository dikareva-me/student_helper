<template>
  <div class="main-page">   
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
  </div>
</template>

<script>

import axios from "axios";
import AddTask from "@/components/AddTask";
//import Test from '@/components/Test';
import Task from "@/components/Task";
import AllTasks from "@/components/AllTasks";
import SignUp from "@/views/SignUp";
export default {
  name: "MainPage",

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

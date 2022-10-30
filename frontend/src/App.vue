<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-toolbar-title>Student helper</v-toolbar-title>
      </div>
    </v-app-bar>



    <v-main>
      <v-container>
   <v-btn
    v-if="!newTaskMode"
    color="primary"
    elevation="6"
    @click="createTask"
    >
    Create new task
    </v-btn>
</v-container>



    <template v-if="newTaskMode">
      <AddTask  
        @hide-new-task="hideNewTask" />
    </template>
     <template v-if="allTasksMode">
    <AllTasks />   
      </template>
  <!--     <NewTask />
     
     <router-view /> -->
    </v-main>
  </v-app>
</template>

<script>

import AddTask from '@/components/AddTask';
//import Test from '@/components/Test';
import AllTasks from '@/components/AllTasks';
export default {
  name: "App",
  components: {
    AllTasks,
    AddTask
  },
  data() {
    return {
      taskList:[],
      flag:"",
      tag : null,
      date : null,
      newTaskMode:false,
      allTasksMode:true,
    }
  },
  methods:{
    hideNewTask(){
      this.newTaskMode = false;
      this.allTasksMode = true;
    },
    createTask(){
      this.newTaskMode = true;
      this.allTasksMode = false;
    }
  }
};
</script>
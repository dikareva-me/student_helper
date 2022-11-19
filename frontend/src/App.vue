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
    <AllTasks 
      @task-page="taskPage"
    />   
      </template>
      
     <template v-if="taskPageMode">
    <Task 
      @task-page="taskPage"
      :task="task"
    />   
      </template>

    </v-main>
  </v-app>
</template>

<script>

import AddTask from '@/components/AddTask';
//import Test from '@/components/Test';
import Task from '@/components/Task';
import AllTasks from '@/components/AllTasks';
export default {
  name: "App",
  components: {
    AllTasks,
    Task,
    AddTask
  },
  data() {
    return {
      taskList:[],
      newTaskMode:false,
      allTasksMode:true,
      taskPageMode:false,
      task:null,
    }
  },
  methods:{
    hideNewTask(){
      this.newTaskMode = false;
      this.allTasksMode = true;
      this.taskPageMode = false;
    },
    createTask(){
      this.newTaskMode = true;
      this.allTasksMode = false;
      this.taskPageMode = false;
    },
    taskPage(event){
      this.task = event;
      console.log(this.task);
      this.newTaskMode = false;
      this.allTasksMode = false;
      this.taskPageMode = true;
    }
  }
};
</script>
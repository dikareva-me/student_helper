<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-toolbar-title>Student helper</v-toolbar-title>
      </div>
    </v-app-bar>

    <v-main>
      
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
    </v-main>
  </v-app>
</template>

<script>
import AddTask from "@/components/AddTask";
import Task from "@/components/Task";
import AllTasks from "@/components/AllTasks";
export default {
  name: "App",
  beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.token;
      //ef175c99790058c4b0899d09c37b312229e3a6b335d57e387e1430fbd971c223;
      console.log(token);
      //this.$store.state.token

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
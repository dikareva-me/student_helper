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




      <template v-if="allTasksMode">
        <AllTasks @task-page="taskPage" />
      </template>

      <template v-if="taskPageMode">
        <Task @task-deleted="taskDeleted" :task="task" />
      </template>
    </v-main>
  </v-app>
</template>

<script>
import AddTask from "@/components/AddTask";
//import Test from '@/components/Test';
import Task from "@/components/Task";
import AllTasks from "@/components/AllTasks";
export default {
  name: "App",
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

    taskDeleted(){
      this.setFlagsFalse();
      this.taskDel = true;
      this.allTasksMode = true;

    }


  },
};
</script>
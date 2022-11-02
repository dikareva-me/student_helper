<template>
  <v-container>

    <v-divider></v-divider>


    <v-row>
      <v-col cols = "12" v-if="taskList.length">
        <h3>List:</h3>
        
          <template>
            <v-layout>
              <v-flex xs12 sm6 md11>
                <v-card
                v-bind:class="{done: task.is_complete}" 
                v-for="task in taskList"
                :key="task.id"
                >
                  <v-card-title
                  
                   primary-title>
                    <div>
                      <div
                      v-if="task.is_complete">
                      <span class="red--text">Task is complete</span>

                      </div>

                      <h3 class="headline mb-0">{{ task.title }}</h3>
                      <div> {{ task.description }} </div>
                      <div>{{ task.deadline }}</div>
                    </div>
                  </v-card-title>

                  <v-card-actions>
                    <v-btn 
                    flat color="orange"
                 
                    >Go to task page
                    </v-btn>

                    <v-btn 
                    flat color="orange"
                    @click="updateStatus(task);"
                    v-if="!task.is_complete"
                    >Complete task
                    </v-btn>
                    <v-btn 
                    flat color="orange"
                    @click="updateStatus(task);"
                    v-else>Uncomplete task</v-btn>

                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
          </template>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  components: {},
   props: {
   // taskList: Array
    },
  data: () => ({
    selected: [],
    taskList: [],
    url: "http://localhost:8000/api/task/",
  }),
   mounted() {
    this.getTasks();
  },
  methods: {
   getTasks() {
       axios.get(`${this.url}?ordering=is_complete`).then((response) => {
        this.taskList = response.data;
        response.data.forEach((element, index) => {
          if (!element.is_complete) this.selected.push(index);
          this.$forceUpdate();
        });
    })
   },
    onNewTaskCreated(event) {
      console.log(event);
      const newTask={
        title:event.title,
        description:event.description,
        is_complete:event.is_complete,
        email:event.email,
        deadline:event.deadline,
        user:event.user
      }
      this.taskList.push(newTask)
    },
    reset() {
      this.$refs.form.reset();
    },
    
    updateStatus(item) {
      item.is_complete = !item.is_complete;
      const url = `${this.url}${item.id}/`;
      var data = {
        is_complete: item.is_complete,
      };
      axios.patch(url, data)
      .then((response) => {
        console.log(response);
        this.getTasks();
      })
      .catch((error) => {
        console.log(error);
      });
    },
   

  },
  
};
</script>

<style scoped>
.done{
  background-color:rgb(192, 187, 187)
}
</style>
<template>
  <v-container>

    <v-divider></v-divider>


    <v-row>
      <v-col cols = "12" v-if="taskList.length">
        <h3>List:</h3>
       <!-- <v-flex --xs12 sm6 md11-->
          <template>
            <v-layout>
              <v-flex >
                <v-card
                v-bind:class="{done: task.is_complete}" 
                class="mb-3"
                v-for="task in taskList"
                :key="task.id"
                >
                  <!--  
                    ANOTHER VERSION OF A CARD: маленький серый текст в описании и дедлайне. 
                    Эту версию лучше использоват, т.к. разделены v-card-title и v-card-text (в прошлой все в тайтле),
                    но надо отредактировать стиль.
                 <v-card-title
                  primary-title
                  style="text-align:center">

                    <div>
                      <div
                      v-if="task.is_complete">
                      <span class="red--text">Task is complete</span>

                      </div>
                      <div>
                      <h3 class="headline mb-2"
                      > {{ task.title }}</h3>
                      </div>
                    </div>
  
                  </v-card-title>
                  <v-card-text>
                      <div>{{ task.description }} </div>
                      <div>Deadline date: {{ task.deadline }}</div>
              
                  </v-card-text>

    -->
                 
                 
                 <!-- ЧТО ИСПРАВИТЬ: сделать по центру тайтл и мб другие элементы карточки -->
                  <v-card-title
                   primary-title style="text-align:center">
                    <div>
                      <div
                      v-if="task.is_complete">
                      <span class="red--text">Task is complete</span>

                      </div>

                      <h3 class="headline mb-2"
                      > {{ task.title }}</h3>
                      <div>{{ task.description }} </div>
                      <div>Deadline date: {{ task.deadline }}</div>
                    </div>
                  </v-card-title>

                  <v-card-actions>
                    <v-btn 
                    color="orange"
                    @click="taskPage(task)"
                    >Go to task page
                    </v-btn>

                    <v-btn 
                    color="orange"
                    @click="updateStatus(task);"
                    v-if="!task.is_complete"
                    >Complete task
                    </v-btn>
                    <v-btn 
                    color="orange"
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
    reset() {
      this.$refs.form.reset();
    },
    updateStatus(item) {
      console.log(item);
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
    taskPage(task){
      console.log(task);
      this.$emit("task-page", task);
    }
   

  },
  
};
</script>

<style scoped>
.done{
  background-color:rgb(192, 187, 187)
}
</style>
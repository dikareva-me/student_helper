<template>
  <v-container>
    <v-divider></v-divider>

    <v-col v-if="taskList.length">
      
      <h2 class="title">Список заданий:</h2>
      <template>
        <v-layout>
          <v-flex>
            <v-card
              v-bind:class="{ done: task.is_complete }"
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

              <v-card-title>
                <div>
                  <div v-if="task.is_complete">
                    <span class="red--text">Задание выполнено</span>
                  </div>

                  <h3 class="headline mb-2">{{ task.title }}</h3>
                  <div>{{ task.description }}</div>
                  <div>Дедлайн: {{ task.deadline }}</div>
                </div>
              </v-card-title>

              <v-card-actions>
                <v-btn color="orange" @click="taskPage(task)"
                  >Перейти на страницу задания
                </v-btn>

                <v-btn
                  color="orange"
                  @click="updateStatus(task)"
                  v-if="!task.is_complete"
                  >Задание выполнено
                </v-btn>
                <v-btn color="orange" @click="updateStatus(task)" v-else
                  >Вернуть в невыполненные</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </template>
    </v-col>
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
    //selected: [],
    taskList: [],
    url: "http://localhost:8000/api/task/",
  }),
  mounted() {
    this.getTasks();
  },
  methods: {
    getTasks() {
      axios
        .get(`${this.url}?ordering=is_complete`)
        .then((response) => {
          this.taskList = response.data;

 
        })
        .catch((error) => {  
          if (error.response.status === 401) {
            
            this.$router.push('/log-in');
    
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            this.$store.commit('removeToken')
          }
        });
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
      axios
        .patch(url, data)
        .then((response) => {
          console.log(response);
          this.getTasks();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    taskPage(task) {
      console.log(task);
      this.$emit("task-page", task);
    },
  },
};
</script>

<style scoped>
.done {
  background-color: rgb(192, 187, 187);
}
</style>

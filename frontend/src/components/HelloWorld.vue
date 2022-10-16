<template>
  <v-container>

     <v-row class="mb-3">
      <v-col cols="12">
        <v-form ref="form" lazy-validation class="text-center">
          <v-text-field
            v-model="newTask.title"
            :counter="128"
            :rules="newTask.titleRules"
            label="Title"
            required
          ></v-text-field>

          <v-textarea
            v-model="newTask.description"
            autocomplete="Description"
            label="Description"
          ></v-textarea>

           <v-text-field
            v-model="newTask.email"
            :rules="newTask.emailRules"
            label="E-mail"
          ></v-text-field>

      <!--    <v-date-picker v-model="newTask.deadline"></v-date-picker>    -->
 
          <v-text-field
            v-model="newTask.deadline"
            label="Deadline date"
          ></v-text-field>
            
          <v-checkbox
            v-model="newTask.is_complete"
            label="Is task completed?"
          ></v-checkbox>

          <v-btn 
          color="error" 
          class="mr-4"
          @click="reset"
           >
           Clear
           </v-btn>

          <v-btn
            color="success"
            class="mr-4"
            :disabled="!newTask.title"
            @click="add"
          >
            Add
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
    <v-divider></v-divider>


    <v-row>
      <v-col cols = "12" v-if="taskList.length">
        <h3>List:</h3>

        <v-list>
          <v-list-item-group 
            multiple
          >
            <v-list-item
              v-for="item in taskList"
              :key="item.id"
              @click="updateStatus(item);"
            >
              <v-list-item-icon>
                {{ item.id }}
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>
                  <strong>{{ item.title }}</strong>
                </v-list-item-title>

                <v-list-item-subtitle>
                  {{ item.description }}
                </v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-action>
                <v-checkbox
                  :input-value="item.is_complete"
                  color="deep-purple "
                ></v-checkbox>
              </v-list-item-action>

            </v-list-item>
          </v-list-item-group>
        </v-list>


      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {

  data: () => ({
    selected: [],
     newTask: {
      title:null,
      description:null,
      titleRules: [
        (v) => !!v || "Title is required",
        (v) => (v && v.length <= 128) || "Title must be less than 128 characters",
      ],
      is_complete: false,
      email:null,
      emailRules: [ 
        (v) => /.+@.+/.test(v) || 'E-mail must be valid' 
      ],
      deadline: "",
      user: 1,
    },
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

    add() {
      console.log(this.newTask);
      var data = this.newTask;
      axios.post("http://localhost:8000/api/task/", data)
      .then((response) => {
        console.log(response);
        this.getTasks();
      })
      .catch((error) => {
        console.log(error);
      });
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

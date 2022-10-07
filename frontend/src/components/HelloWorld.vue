<template>
  <v-container>

     <v-row class="mb-3">
      <v-col cols="12">
        <v-form ref="form" lazy-validation class="text-center">
          <v-text-field
            label="Title"
            required
          ></v-text-field>

          <v-textarea
            autocomplete="Description"
            label="Description"
          ></v-textarea>

           <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
          ></v-text-field>

          <v-text-field
            label="Deadline date"
            required
          ></v-text-field>
          
          <v-checkbox
            label="Is task completed?"
          ></v-checkbox>

          <v-btn 
          color="error" 
          class="mr-4"
           >
           Clear
           </v-btn>

          <v-btn
            color="success"
            class="mr-4"
            
          >
            Add
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
    <v-divider></v-divider>


    <v-row>
      <v-col cols = "12">
        <h3>List:</h3>

        <v-list>
          <v-list-item-group 
            v-model="selected" 
            color="deep-purple" 
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
    taskList: [],
  }),
   mounted() {
    this.getTodos();
  },
  methods: {
   getTodos() {
       axios.get("http://127.0.0.1:8000/api/task/").then((response) => {
        this.taskList = response.data;
    })
   },
  },
  
};
</script>

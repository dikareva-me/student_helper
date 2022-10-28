<template>
<div>

<v-container>
     <v-row class="mb-3">
      <v-col cols="12">
        <v-form ref="form" lazy-validation class="text-center">
          <v-text-field
            v-model="title"
            :counter="128"
            :rules="titleRules"
            label="Title"
            required
          ></v-text-field>

          <v-textarea
            v-model="description"
            autocomplete="Description"
            label="Description"
          ></v-textarea>

           <v-combobox
          v-model="subject"
          :items="items"
          label="Subject"
          multiple
          outlined
          dense
        ></v-combobox>

           <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
          ></v-text-field>

           <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="date"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="deadline"
            label="Deadline date"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>

        </template>
        <v-date-picker
          v-model="deadline"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="menu = false"
          >
            Cancel
          </v-btn>
          <v-btn
            text
            color="primary"
            @click="$refs.menu.save(deadline)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>

          <v-checkbox
            v-model="is_complete"
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
            @click="createNewTask"
          >
            Add
          </v-btn> 
        </v-form>
      </v-col>
    </v-row>
    
</v-container>

</div>
</template>


<script>
import axios from "axios";
export default {
    name: "NewTask",
    data () {
        return{
          title:"Title",
          description:null,
          titleRules: [
            (v) => !!v || "Title is required",
            (v) => (v && v.length <= 128) || "Title must be less than 128 characters",
          ],
          is_complete: false,
          subject:null,
          email:null,
          emailRules: [ 
            (v) => /.+@.+/.test(v) || 'E-mail must be valid' 
          ],
          deadline: "",
          user: 1,
                
    }
    
  },
  methods:{
  async createNewTask(){
        task = {
        title:this.title,
        description:this.description,
        is_complete:this.is_complete,
        email:this.email,
        deadline:this.deadline,
        user:this.user
      }
       console.log(data);
  //    await addTask(task)
      console.log("a have added a new task!")
      this.$emit("newTaskCreated", task)
    },
     reset() {
      this.$refs.form.reset();
    },
    add() {
      console.log(data);
      /*var data = this.data;
      axios.post("http://localhost:8000/api/task/", data)
      .then((response) => {
        console.log(response);
      //  this.getTasks();
      })
      .catch((error) => {
        console.log(error);
      });*/
    },
    
  }
  
    
}
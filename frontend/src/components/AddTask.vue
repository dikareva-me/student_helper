<template>
<v-container>
    <v-btn
    color="primary"
    elevation="6"
    @click="backToTasks"
    >
    ← Вернуться к заданиям
    </v-btn>
    
    <h3>Создать новое задание:</h3>

     <v-row class="mb-3">
      <v-col cols="12">
        <v-form ref="form" lazy-validation class="text-center">
          <v-text-field
            v-model="title"
            :counter="128"
            :rules="titleRules"
            label="Название"
            required
          ></v-text-field>
        
        <v-textarea
            v-model="description"
            autocomplete="Описание"
            label="Описание"
          ></v-textarea>

          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
          ></v-text-field>

         <v-text-field
          v-model="subject"
          label="Предмет"
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
            label="Дата дедлайна"
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
            label="Задание выполнено?"
          ></v-checkbox>

<div class="mb-3">
    <v-btn 
          color="error" 
          class="mr-4"
          @click="reset"
           >
           Очистить
           </v-btn>
 
          <v-btn 
            type="submit"
            color="success"
            class="mr-4"
            :disabled="!this.title"
            @click.prevent="onSubmit"
          >
            Создать
          </v-btn> 
          </div>
            
            <v-alert
            color="green"
            type="success"
            v-if="taskAdded"
            >
            Задание успешно создано.
        </v-alert>
            <v-alert
            color="red"
            type="error"
            v-if="taskError"
            >
            Ошибка: невозможно создать такое задание. Пожалуйста, попробуйте снова.
        </v-alert>



        </v-form>
      </v-col>
    </v-row>

</v-container>

</template>



<script>
import axios from "axios";
export default {
 data() {
    return {
        title:null,
        titleRules: [
            (v) => !!v || "Title is required",
            (v) => (v && v.length <= 128) || "Title must be less than 128 characters",
        ],
        description:null,
        is_complete: false,
        subject:null,
        email:null,
        emailRules: [ 
            (v) => !v || /.+@.+/.test(v) || 'E-mail must be valid' 
          ],
        deadline:null,
        taskAdded:false,
        taskError:false,
    }
  },
  methods: {
    onSubmit() {
        const newTask = {
            title: this.title,
            description:this.description,
            is_complete:this.is_complete,
            email:this.email,
            deadline:this.deadline,
            user:1
        }
     console.log("Submiit");
     console.log(newTask);
     axios.post("http://localhost:8000/api/task/", newTask)
      .then((response) => {
        console.log(response);
        this.taskAdded = true;
        this.taskError = false;
      })
      .catch((error) => {
        console.log(error);
        this.taskAdded = false;
        this.taskError = true;
      });

    // this.$emit("task-created", newTask);
    },
    reset() {
      this.$refs.form.reset();
      this.taskAdded = false;
      this.taskError = false;
    },
    backToTasks(){
        this.$emit("hide-new-task");
    }
  }
}
</script>
    

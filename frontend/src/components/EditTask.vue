<template>
  <v-container>
    
    <v-btn 
    color="primary" 
    elevation="6" 
    @click="backToTask">
      ← Вернуться к просмотру задания
    </v-btn>

    <v-row class="mb-3">
      <v-col cols="12">
        <v-form ref="form" lazy-validation class="text-center">
          <v-text-field
            v-model="task.title"
            :counter="128"
            :rules="titleRules"
            label="Title"
            required
          ></v-text-field>

          <v-textarea
            v-model="task.description"
            autocomplete="Description"
            label="Description"
          ></v-textarea>

          <v-text-field
            v-model="task.email"
            :rules="emailRules"
            label="E-mail"
          ></v-text-field>

          <v-combobox
            v-model="task.subject"
            :items="items"
            label="Subject"
            multiple
            outlined
            dense
          ></v-combobox>

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
                v-model="task.deadline"
                label="Deadline date"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="task.deadline" no-title scrollable>
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="menu = false"> Cancel </v-btn>
              <v-btn
                text
                color="primary"
                @click="$refs.menu.save(task.deadline)"
              >
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>

          <div class="mb-3">
            <v-btn 
            color="primary" 
            class="mr-4" 
            @click="cancelChanges"
              >Отменить изменения
            </v-btn>

            <v-btn 
            color="green" 
            class="mr-4" 
            @click="editTask"
              >Сохранить изменения
            </v-btn>
          </div>

          <v-alert 
          color="green" 
          type="success" 
          v-if="saved_changes">
            Изменения сохранены.
          </v-alert>
          
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import axios from "axios";
export default {
  props: {
    task: Object,
  },
  data: () => ({
    before_editing: {},
    saved_changes: false,
    titleRules: [
      (v) => !!v || "Title is required",
      (v) => (v && v.length <= 128) || "Title must be less than 128 characters",
    ],
    emailRules: [(v) => !v || /.+@.+/.test(v) || "E-mail must be valid"],
    url: "http://localhost:8000/api/task/",
  }),
  created() {
    this.before_editing = Object.assign({}, this.task);
    console.log(this.before_editing);
  },
  methods: {
    editTask() {
      const url = `${this.url}${this.task.id}/`;

      axios
        .patch(url, this.task)
        .then((response) => {
          console.log(response);
          this.saved_changes = true;
          Object.assign(this.before_editing, this.task);
        })
        .catch((error) => {
          console.log(error);
          this.saved_changes = false;
        });
    },
    cancelChanges() {
      Object.assign(this.task, this.before_editing);
      this.saved_changes = false;
      console.log(this.task);
      console.log(this.before_editing);
    },
    backToTask() {
      this.$emit("hide-edit-form");
    },
  },
};
</script>
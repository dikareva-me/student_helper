<template>
  <v-container>
    <template v-if="taskPageMode">
      <div>{{ this.task }}</div>
      <h3 lazy-validation class="text-center">Задание</h3>

      <v-row class="mb-3">
        <v-col cols="12">
          <v-form ref="form" lazy-validation class="text-center">

            <v-btn color="blue" 
            class="mr-4" 
            @click="editTask">
              Редактировать задание
            </v-btn>

            <v-dialog 
            v-model="dialog" 
            width="550">
              <template v-slot:activator="{ on, attrs }">
                <v-btn 
                color="red" 
                v-bind="attrs" 
                v-on="on">
                  Удалить задание
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h5">
                  Вы уверены, что хотите удалить задание?
                </v-card-title>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn 
                  color="primary"
                  text
                  @click="dialog = false">
                    Отмена
                  </v-btn>

                  <v-btn 
                  color="Red" 
                  @click="deleteTask">
                    Удалить
                  </v-btn>

                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-form>
        </v-col>
      </v-row>
    </template>

    <template v-if="editTaskMode">
      <EditTask @hide-edit-form="hideEditForm" :task="task" />
    </template>
  </v-container>
</template>

<script>
import EditTask from "@/components/EditTask";
import axios from "axios";
export default {
  props: {
    task: Object,
  },
  components: {
    EditTask,
  },
  data() {
    return {
      dialog: false,
      editTaskMode: false,
      taskPageMode: true,
      url: "http://localhost:8000/api/task/",
    };
  },

  methods: {
    editTask() {
      this.editTaskMode = true;
      this.taskPageMode = false;
    },

    hideEditForm() {
      this.editTaskMode = false;
      this.taskPageMode = true;
    },

    deleteTask() {
      this.dialog = false;
      const url = `${this.url}${this.task.id}/`;
      axios.delete(url, this.task)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
      this.$emit("task-deleted");
    },
  },
};
</script>
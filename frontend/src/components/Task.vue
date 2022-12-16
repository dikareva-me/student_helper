<template>
  <v-container>
    <template v-if="taskPageMode">
      <v-btn color="primary" elevation="6" @click="backToTasks">
        ← Вернуться к заданиям
      </v-btn>

      <v-row class="mb-3">
        <v-col cols="12">
          <v-form ref="form" lazy-validation class="text-center">
            <h2 lazy-validation class="text-center">Задание</h2>
            <br />
            <br />

            <div>
              <strong>Название:</strong>
              {{ task.title }}
              <br />
              <br />
              <template v-if="task.description != null">
                <strong>Описание:</strong>
                {{ task.description }}
                <br />
                <br />
              </template>

              <template v-if="task.subject != null">
                <strong>Предмет:</strong>
                <br />
                <br />
              </template>

              <template v-if="task.email != null">
                <strong>Email:</strong>
                {{ task.email }}
                <br />
                <br />
              </template>

              <strong>Дедлайн:</strong>
              {{ task.deadline }}
              <br />
              <br />

              <template v-if="task.is_complete != true">
                <strong>Задание не выполнено</strong>
              </template>
              <template v-else>
                <strong>Задание выполнено</strong>
              </template>
            </div>
            <br />

            <v-btn color="blue" class="mr-4" @click="editTask">
              Редактировать задание
            </v-btn>

            <v-dialog v-model="dialog" width="550">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="red" v-bind="attrs" v-on="on">
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
                  <v-btn color="primary" text @click="dialog = false">
                    Отмена
                  </v-btn>

                  <v-btn color="Red" @click="deleteTask"> Удалить </v-btn>
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
      taskDeleted: false,
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

    async deleteTask() {
      this.dialog = false;
      const url = `${this.url}${this.task.id}/`;
      await axios
        .delete(url, this.task)
        .then((response) => {
          console.log(response);
          console.log("no err");
        })
        .catch((error) => {
          console.log(error);
          console.log("err");
        });
      this.taskDeleted = true;
      console.log(this.taskDeleted);
      this.$emit("hide-task", this.taskDeleted);
    },
    backToTasks() {
      this.$emit("hide-task", this.taskDeleted);
    },
  },
};
</script>

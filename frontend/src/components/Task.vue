<template>
    <v-container>
    <h2 lazy-validation class="text-center">Full information of Task</h2>
    <br>
    <br>

    <div>
    <strong>Title:</strong>
     {{task.title}}
    <br>
    <br>
    <template v-if="task.description != null">
    <strong>Description:</strong>
     {{task.description}}
    <br>
    <br>
    </template>

    <template v-if="task.subject != null">
    <strong>Subject:</strong>
    <br>
    <br>
    </template>

    <template v-if="task.email != null">
    <strong>Email:</strong>
     {{task.email}}
    <br>
    <br>
    </template>

    <strong>Deadline:</strong>
     {{task.deadline}}
    <br>
    <br>

    <template v-if="task.is_complete != true">
    <strong>Task is not completed</strong>
    </template>
    <template v-else>
    <strong>Task is completed</strong>
    </template>

    </div>

     <v-row class="mb-3">
      <v-col cols="12">
        <v-form ref="form" lazy-validation class="text-center">


        </v-form>
      </v-col>
     </v-row>
    </v-container>


</template>

<script>
import axios from "axios";
export default {
    props:{
        task: Object
    },
}
</script>

<style scoped>

</style>
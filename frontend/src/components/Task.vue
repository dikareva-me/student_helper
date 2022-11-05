<template>
    <v-container>
    <div>{{this.task}}"</div>
    <h3 lazy-validation class="text-center">Task</h3>

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
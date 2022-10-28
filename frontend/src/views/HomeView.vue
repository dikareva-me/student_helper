<template>
    <v-container>
       
  
     

    <AllTasks />




  </v-container>

  

</template>

<script>
import AllTasks from "../components/AllTasks";
//import NewTask from "../components/NewTask";
export default {
  name: "Home",

  components: {
    AllTasks,
  //  NewTask
  },
};
</script>

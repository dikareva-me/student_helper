<template>
  <form @submit.prevent="onSubmit">
    <input type="text" v-model="title">
    <button type="submit">Create</button>
  </form>
</template>



<script>
export default {

  methods: {
    onSubmit() {
     console.log("Submit");
    }
  }
}
</script>
<template>
    <div class="page-login">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Войти в аккаунт</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Логин</label>
                        <div class="control">
                            <input name="username" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                     <v-btn color="green" class="mr-4" @click="login"
                    >Войти
                    </v-btn>
                    
                </form>
            </div>
        </div>
    </div>
</template>



<script>
import axios from 'axios'

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        async login() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("http://127.0.0.1:8000/auth/login/", formData)
                .then(response => {
                    const token = response.data.token

                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)
                    console.log(localStorage.getItem('token'))

                    
              //      console.log(this.$store.state.token)
                 //   console.log(token)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }

                        console.log(JSON.stringify(error.response.data))
                    } else if (error.message) {
                        console.log(JSON.stringify(error.message))
                    } else {
                        console.log(JSON.stringify(error))
                    }
                });


                axios
                .get("http://127.0.0.1:8000/auth/user/")
                .then(response => {
                    this.$store.commit('setUser', {'username': response.data.username, 'id': response.data.id})

                    localStorage.setItem('username', response.data.username)
                    localStorage.setItem('email', response.data.email)
                    localStorage.setItem('userid', response.data.id)
                    
                    console.log("response data");
                    console.log(response.data);

                    
                    console.log("user id in store");
                    console.log(this.$store.state.user.id);

                    
                    this.$router.push('/main-page')



                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
        }
    }

</script>
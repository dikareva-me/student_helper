<template>
    <div class="page-signup">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">

                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input name="username" class="input" v-model="username">
                        </div>
                    </div>

                        <label>E-mail</label>
                        <div class="control">
                            <input type="email" name="Email" class="input" v-model="email">
                        </div>
                    </div>
                    

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>


                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" name="Repeat password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p 
                            v-for="error in errors" 
                            v-bind:key="error"
                        >
                            {{ error }}
                        </p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Sign up</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SignUp',
    data () {
        return {
            username: '',
            email:'',
            password: '',
            password2:'',
            errors: []
        }
    },
    methods: {
        submitForm(e) {
            const formData = {
                username: this.username,
                password: this.password,
                password2:this.password2,
                email:this.email,
            }

            axios
                .post("http://127.0.0.1:8000/auth/register/", formData)
                .then(response => {
                    console.log(response)

                    this.$router.push('/log-in')
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
                })
        }
    }
}
</script>
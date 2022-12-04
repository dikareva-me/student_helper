<template>
    <div class="page-profile">
        <h1 class="title">Информация о профиле</h1>
        
        <strong>Логин: </strong>{{ $store.state.user.username }}
        <br>
        <strong>Почта: </strong>{{ $store.state.user.email }}
        
        <hr>

        <button @click="logout()" class="button is-danger">Выйти из аккаунта</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MyAccount',
    methods: {
        logout() {
            axios
                .post("http://127.0.0.1:8000/auth/logout/")
                .then(response => {
                    axios.defaults.headers.common["Authorization"] = ""

                    localStorage.removeItem("token")

                    this.$store.commit('removeToken')

                    this.$router.push('/')
                })
                .catch(error => {
                    if (error.response) {
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
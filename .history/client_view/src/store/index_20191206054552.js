import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import routes from '../router/index'
Vue.use(Vuex)

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default new Vuex.Store({
    state: {
        idToken: "",
        loggedIn: false,
        login_error: false,
        loading: false
    },
    getters: {
        idToken: state => state.idToken,
        loggedIn: state => state.loggedIn,
        login_error: state => state.login_error,
        loading: state => state.loading
    },
    mutations: {
        storeIdToken(state, idToken) {
            state.idToken = idToken;
            localStorage.setItem("jwt", JSON.stringify(idToken))
            state.loggedIn = true
        },
        login_success(state) {
            state.login_error = false
        },
        login_error(state) {
            state.login_error = true
        },
        loading_on(state) {
            state.loading = true
        },
        loading_off(state) {
            state.loading = false
        }
    },
    actions: {
        login({
            commit
        }, auth) {
            commit('loading_on')
            axios
                .post("http://127.0.0.1:8000/auth/", {
                    username: auth.username,
                    password: auth.password,
                })
                .then(response => {
                    console.log(response)
                    commit('storeIdToken', response.data)
                    routes.push("/admin")
                }).catch(error => {
                    console.log(error.response); // responceを追加
                });
        },
        reset({
            commit
        }) {
            commit('login_success')
        }
    }
})
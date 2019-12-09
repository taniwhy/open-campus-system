import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default new Vuex.Store({
    state: {
        idToken: "",
        loggedIn: false
    },
    getters: {
        idToken: state => state.idToken,
        loggedIn: state => state.loggedIn
    },
    mutations: {
        storeIdToken(state, idToken) {
            state.idToken = idToken;
            localStorage.setItem("jwt", JSON.stringify(idToken))
            state.loggedIn = true
        }
    },
    actions: {
        login({ commit }, auth) {
            console.log(auth)
            axios
                .post("http://127.0.0.1:8000/auth/", {
                    username: auth.username,
                    password: auth.password,
                })
                .then(response => {
                    console.log(response)
                    commit('storeIdToken', response.data.token)
                    this.$router.push({ path: "/admin" });
                });
        }
    }
})
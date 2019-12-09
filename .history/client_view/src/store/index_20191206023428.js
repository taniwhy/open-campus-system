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
    }
})
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import routes from '../router/index'

Vue.use(Vuex)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

/**
 * 全てのページで使用できる全体の状態管理
 */
export default new Vuex.Store({
    /**
     * idTokn: 認証用のトークン
     * loggedIn: ログイン状態管理
     * login_erro: 表示出力判定
     * loading: 表示出力判定
     */
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
            state.loggedIn = true
        },
        remove_storeIdToken(state) {
            state.idToken = "";
            state.loggedIn = false
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
        /**
         * ログイン処理
         * @param {Object} auth 認証に使用するIDとPASS
         */
        login({
            commit
        }, auth) {
            commit('login_success')
            commit('loading_on')
            axios
            /**
             * 
             */
                .post("http://127.0.0.1:8000/auth/", {
                    username: auth.username,
                    password: auth.password,
                })
                .then(response => {
                    commit('storeIdToken', response.data)
                    routes.push("/admin")
                }).catch(error => {
                    console.log(error.response);
                    commit('loading_off')
                    commit('login_error')
                });
        },
        logout({
            commit
        }) {
            commit('remove_storeIdToken')
            routes.push("/login")
        }
    }
})
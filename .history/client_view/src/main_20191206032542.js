import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;
Vue.config.devtools = true;

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')

router.beforeEach((to, from, next) => {
    if (to.matched.some(url => url.meta.isPublic) || store.getters.loggedIn) {
        next()
    } else {
        next('login')
    }
});
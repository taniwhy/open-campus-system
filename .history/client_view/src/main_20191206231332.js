import Vue from 'vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;
Vue.config.devtools = true;

new Vue({
    router,
    store,
    vuetify,
}).$mount('#app')
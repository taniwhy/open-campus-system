import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    router,
    vuetify,
    components: { App },
    template: '<App/>'
})
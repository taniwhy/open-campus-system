/**
 * 全てのページに適用されるScript
 */
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;
Vue.config.devtools = true;

new Vue({
    /***
     * プラグイン設定
     */
    router,
    store,
    vuetify,
    /**
     * App配下をレンダリング
     */
    render: h => h(App)
        /**
         * /public/index.htmlのid: appにマウント
         */
}).$mount('#app')
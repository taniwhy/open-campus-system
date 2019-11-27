import Vue from 'vue'
import Router from 'vue-router'



Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            component: page1
        },
        {
            path: '/page2',
            component: page2
        }
    ]
})
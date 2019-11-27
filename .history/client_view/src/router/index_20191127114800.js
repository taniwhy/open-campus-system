import Vue from 'vue'
import Router from 'vue-router'

import page1 from '@/components/page1'
import page2 from '@/components/page2'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
        path: '/page2',
        component: page2
    }]
})
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/home' // new add

Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            name: 'HelloWorld',
            component: HelloWorld
        }, // , の追加を忘れずに
        {
            path: '/home', // new add
            name: 'Home', // new add
            component: Home // new add
        }
    ]
})
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Branch from '../components/Branch.vue'
import Base_form from '../components/Base_form.vue'
import Register from '../components/Register.vue'
import Confirmation from '../components/Confirmation.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/branch',
        name: 'branch',
        component: Branch
    },
    {
        path: '/register',
        name: 'baseform',
        component: Base_form,
        children: [{
                path: '/',
                component: Register
            },
            {
                path: '/confirmation',
                component: Confirmation
            },
        ]
    },
]

const router = new VueRouter({
    routes
})

export default router
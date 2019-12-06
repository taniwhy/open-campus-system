import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Branch from '../components/Branch.vue'
import Register from '../components/Register.vue'
import Base_form from '../components/Base_form.vue'
import Confirmation from '../components/Confirmation.vue'
import Login from '../components/Login.vue'
import Admin from '../components/Admin.vue'
import Base from '../components/Base.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        component: Base,
        children: [{
                path: '/',
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
        ]
    },
    {
        path: '/register',
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
    {
        path: '/admin',
        name: 'admin',
        component: Admin
    },
]

const router = new VueRouter({
    routes,
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        } else {
            return {
                x: 0,
                y: 0
            }
        }
    }
})

export default router
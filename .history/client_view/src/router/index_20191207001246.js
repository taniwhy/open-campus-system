import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Admin from '../views/Admin.vue'
import Base from '../views/Base.vue'
import Base_form from '../views/Base_form.vue'

import Register from '../components/Register.vue'
import Confirmation from '../components/Confirmation.vue'
import Reregister from '../components/Reregister.vue'
import Reconfirmation from '../components/Reconfirmation.vue'
import Participant_register from '../components/Participant_register.vue'
import Participant_confirmation from '../components/Participant_confirmation.vue'
import Allparticipant from '../components/Allparticipant.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        component: Base,
        children: [{
            path: '/',
            component: Home
        }]
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
            {
                path: '/re_register',
                component: Reregister
            },
            {
                path: '/re_confirmation',
                component: Reconfirmation

            },
            {
                path: '/participant_confirmation',
                component: Participant_confirmation
            },
            {
                path: '/participant_register',
                component: Participant_register
            }
        ]
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/admin',
        name: 'admin',
        component: Admin,
        children: [{
            path: '/',
            component: Allparticipant
        }]
    },
]

const router = new VueRouter({
    routes,
    /**
     * 画面遷移時に画面上部に移動する
     * @param {*} savedPosition 画面一の履歴
     */
    scrollBehavior(savedPosition) {
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
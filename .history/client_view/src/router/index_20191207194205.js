import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Admin from '../views/Admin.vue'
import Base from '../views/Base.vue'
import FormBase from '../views/FormBase.vue'

import Register from '../components/Register.vue'
import RegisterConfirmation from '../components/RegisterConfirmation.vue'
import Entry from '../components/Entry.vue'
import EntryConfirmation from '../components/EntryConfirmation.vue'
import Participant_register from '../components/Participant_register.vue'
import Participant_confirmation from '../components/Participant_confirmation.vue'
import AllParticipant from '../components/AllParticipant.vue'

Vue.use(VueRouter)

/**
 * ルーティングに使用するパス
 */
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
        component: FormBase,
        children: [{
                path: '/',
                component: Register
            },
            {
                path: '/register_confirmation',
                component: RegisterConfirmation
            },
            {
                path: '/entry',
                component: Entry
            },
            {
                path: '/rentry_confirmation',
                component: EntryConfirmation

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
            component: AllParticipant
        }]
    },
]

/**
 * ルーター宣言
 */
const router = new VueRouter({
    /**
     * パスデータのインポート
     */
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
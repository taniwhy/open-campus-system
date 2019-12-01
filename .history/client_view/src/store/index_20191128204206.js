import Vue from 'vue'
import Vuex from 'vuex'

import spot from './spots.module'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        spots
    }
})
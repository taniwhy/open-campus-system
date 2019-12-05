import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        form: {
            family_name: null,
            first_name: null,
            family_name_reading: null,
            first_name_reding: null,
            birth_year: null,
            birth_month: null,
            birth_day: null,
            postal_code: null,
            street_address: null,
            address: null,
            job: null,
            school_year: null
        },
    },
    mutations: {},
    actions: {}
})
import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'
import config from "./config"

const vuexLocal = new VuexPersistence({
    storage: window.localStorage
})
Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        config
    },
    plugins: [vuexLocal.plugin]
})

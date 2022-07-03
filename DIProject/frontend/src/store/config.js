import houseController from "../../../server/controllers/House"

export default {
    namespaced: true,
    state: {
        houseList: [],
    },
    getters: {
        getHouseList: state => state.houseList,
    },
    mutations: {
        setHouseList(state, houseList) {
            state.houseList = houseList
        },
    },
    actions: {
        async getHouseList({commit}, {page}) {
            const houseList = await houseController.list(page)
            commit('setHouseList', houseList)
        },
    }
}


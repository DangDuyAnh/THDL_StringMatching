import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from "../views/HomeView";
import HouseDetail from "../views/HouseDetail";
import ChartView from "../views/ChartView";
import Homepage from "../views/HomePage";
Vue.use(VueRouter);

const routes = [
    {
        path: '/data',
        name: 'Data',
        component: HomeView,
    },
    {
        path: '/house/:id',
        component: HouseDetail,
    },
    {
        path: '/charts',
        name: 'Chart',
        component: ChartView,
    },
    {
        path: '/',
        component: Homepage
    }
]

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;
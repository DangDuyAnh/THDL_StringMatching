import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from "../views/HomeView";
import HouseDetail from "../views/HouseDetail";

Vue.use(VueRouter);

const routes = [
    {
        path: '/home',
        name: 'Home',
        component: HomeView,
    },
    {
        path: '/house/:id',
        component: HouseDetail,
    }
]

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;
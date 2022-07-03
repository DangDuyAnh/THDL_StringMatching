import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from "../views/HomeView";

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView,
        children: [
            {
                path: '/',
                component: index
            }
        ]
    }
]

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;
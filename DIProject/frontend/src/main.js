import Vue from 'vue'
import App from './App'
// import router from './router'

Vue.config.productionTip = false

// new Vue({
//   el: '#app',
//   // router,
//   // store,
//   components: {
//     App
//   },
//   template: '<App/>'
// })
new Vue({
  render: h => h(App),
}).$mount('#app')
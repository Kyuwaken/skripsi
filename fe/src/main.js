import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import "./plugins/vue-sweetalert2"
import interceptorsSetup from "@/plugins/interceptors";

Vue.config.productionTip = false
interceptorsSetup();
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

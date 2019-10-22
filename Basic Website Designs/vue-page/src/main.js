import Vue from "vue"
import Tachyons from "tachyons"
import App from "./App.vue"

Vue.config.productionTip = false

new Vue({
  Tachyons,
  render: h => h(App)
}).$mount("#app")

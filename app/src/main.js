import Vue from 'vue'
import app from './app.vue'
import router from './router'
import store from './store'

//引入element-ui及其样式
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(app)
}).$mount('#app')

import axios from 'axios'
axios.defaults.withCredentials = true
axios.defaults.baseURL = "http://192.168.0.137:80"
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
const app = createApp(App)

app.use(router)

app.mount('#app')

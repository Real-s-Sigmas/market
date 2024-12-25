import axios from 'axios'
axios.defaults.withCredentials = true
axios.defaults.baseURL = "http://127.0.0.1:80"
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
const app = createApp(App)

app.use(router)

app.mount('#app')

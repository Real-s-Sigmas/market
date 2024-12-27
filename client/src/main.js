import axios from 'axios'
axios.defaults.withCredentials = true
axios.defaults.baseURL = "https://api.sir-stroyremont.ru/"
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
const app = createApp(App)

app.use(router)

app.mount('#app')

import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../componets/Main/MainPage.vue')
    },
    {
      path: '/Product',
      name: 'home',
      component: () => import('../componets/Product/CardProduct.vue')
    },
  ]
})

export default router

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
      name: 'product',
      component: () => import('../componets/Product/ProductPage.vue')
    },
    {
      path: '/Products',
      name: 'product',
      component: () => import('../componets/Product/ProductsPage.vue')
    },
  ]
})

export default router

import { createRouter, createWebHistory } from "vue-router";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../componets/Main/MainPage.vue"),
    },
    {
      path: "/Product",
      name: "product",
      component: () => import("../componets/Product/ProductPage.vue"),
    },
    {
      path: "/Login",
      name: "login",
      component: () => import("../componets/Forms/EmailPage.vue"),
    },
    {
      path: "/Enter",
      name: "enter",
      component: () => import("../componets/Forms/EnterPage.vue"),
    },
    {
      path: "/Category",
      name: "category",
      component: () => import("../componets/Product/ProductsPage.vue"),
    },
    {
      path: "/Favorites",
      name: "favorites",
      component: () => import("../componets/favorites/Favorites.vue"),
    },
    {
      path: "/myorders",
      name: "myorders",
      component: () => import("../componets/orders/MyordersPage.vue"),
    },
    {
      path: "/myorders/arkhiv",
      name: "arkhiv",
      component: () => import("../componets/orders/ArkhivPage.vue"),
    },
    {
      path: "/AddProduct",
      name: "AddProduct",
      component: () => import("../componets/admin/AddProduct.vue"),
    },
    {
      path: "/Login",
      name: "Login",
      component: () => import("../componets/Forms/EmailPage.vue"),
    },
    {
      path: "/EnterEmail",
      name: "EnterEmail",
      component: () => import("../componets/Forms/EnterPage.vue"),
    },
    {
      path: "/edit",
      name: "Edit",
      component: () => import("../componets/TestsComp/MenuComp.vue")
    }
],
});

export default router;

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
      path: "/Product/:id",
      name: "product",
      component: () => import("../componets/Product/ProductPage.vue"),
    },
    {
      path: "/Login",
      name: "login",
      component: () => import("../componets/Forms/LoginPage.vue"),
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
      component: () => import("../componets/Forms/LoginPage.vue"),
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
    },
    {
      path: "/aboutus",
      name: "AboutUs",
      component: () => import("../componets/AboutUs/AboutComp.vue")
    },
    {
      path: "/basket",
      name: "MyBasket",
      component: () => import("../componets/orders/BasketPage.vue")
    },
    {
      path: "/:pathMatch(.*)",
      name: "NotFound",
      component: () => import("../componets/reuse/NotFound.vue")
    },
    // {
    //   path: "/catalog",
    //   name: "Catalog",
    //   component: () => import("../componets/Product/CatalogPage.vue")
    // },
    {
      path: "/Catalog",
      name: "catalog",
      component: () => import("../componets/Catalog/Catalog.vue")
    },
    {
      path: "/Category/:firstParametr/:secondParametr/:thirdParametr?",
      name: "category",
      component: () => import("../componets/Category/Category.vue")
    },
    {
      path: "/SignUp",
      name: "signup",
      component: () => import("../componets/Forms/RegisterPage.vue")
    },
    {
      path: "/ResetPassword",
      name: "reset password",
      component: () => import("../componets/Forms/EmailPassword.vue")
    },
      {
      path: "/NewPassword",
      name: "NewPassword",
      component: () => import("../componets/Forms/NewPassword.vue")
    },
    {
      path: "/FindProducts",
      name: "findproduct",
      component: () => import("../componets/FindProducts/FindProducts.vue")
    },
    {
      path: "/ProductComp",
      name: "productcomp",
      component: () => import("../componets/Product/ProductComp.vue")
    },
    {
      path: "/AdminPanel/actions",
      name: "adminpanelActions",
      component: () => import("../componets/admin/PanelComp.vue")
    },
    {
      path: "/AdminPanel/orders",
      name: "adminpanelOrders",
      component: () => import("../componets/admin/AdminOrders.vue")
    },
    {
      path: "/OrdersAdminComp",
      name: "ordersadmincomp",
      component: () => import("../componets/admin/OrdersAdminComp.vue")
    }
  ],
});

export default router;

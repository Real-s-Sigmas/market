import { createRouter, createWebHistory } from "vue-router";
// import Home from '@/componets/Main/MainPage.vue';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../componets/Main/MainPage.vue"),
      meta: {
        title: 'Сир - Строительство и Ремонт'
      }
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
      meta: {
        title: 'Вход | Сир'
      }
    },
    {
      path: "/Enter",
      name: "enter",
      component: () => import("../componets/Forms/EnterPage.vue"),
      meta: {
        title: 'Код подтверждения | Сир'
      }
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
      meta: {
        title: 'Избранные | Сир'
      }
    },
    {
      path: "/myorders",
      name: "myorders",
      component: () => import("../componets/orders/MyordersPage.vue"),
      meta: {
        title: 'Мои заказы | Сир'
      }
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
      meta: {
        title: 'Добавление товара | Сир'
      }
    },
    {
      path: "/Login",
      name: "Login",
      component: () => import("../componets/Forms/LoginPage.vue"),
      meta: {
        title: 'Вход | Сир'
      }
    },
    {
      path: "/EnterEmail",
      name: "EnterEmail",
      component: () => import("../componets/Forms/EnterPage.vue"),
      meta: {
        title: 'Код подтверждения | Сир'
      }
    },
    {
      path: "/edit",
      name: "Edit",
      component: () => import("../componets/TestsComp/MenuComp.vue"),
      meta: {
        title: 'Редоктирование | Сир'
      }
    },
    {
      path: "/aboutus",
      name: "AboutUs",
      component: () => import("../componets/AboutUs/AboutComp.vue"),
      meta: {
        title: 'О нас | Сир'
      }
    },
    {
      path: "/basket",
      name: "MyBasket",
      component: () => import("../componets/orders/BasketPage.vue"),
      meta: {
        title: 'Корзина | Сир'
      }
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
      component: () => import("../componets/Catalog/Catalog.vue"),
      meta: {
        title: 'Каталог | Сир'
      }
    },
    {
      path: "/Category/:firstParametr/:secondParametr",
      name: "category",
      component: () => import("../componets/Category/Category.vue"),
      meta: {
        title: 'Категория'
      }
    },
    {
      path: "/SignUp",
      name: "signup",
      component: () => import("../componets/Forms/RegisterPage.vue"),
      meta: {
        title: 'Регистрация | Сир'
      }
    },
    {
      path: "/ResetPassword",
      name: "reset password",
      component: () => import("../componets/Forms/EmailPassword.vue"),
      meta: {
        title: 'Сброс пароля | Сир'
      }
    },
    {
      path: "/NewPassword",
      name: "NewPassword",
      component: () => import("../componets/Forms/NewPassword.vue"),
      meta: {
        title: 'Новый пароль | Сир'
      }
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
      component: () => import("../componets/admin/PanelComp.vue"),
      meta: {
        title: 'Действия | Сир'
      }
    },
    {
      path: "/AdminPanel/orders",
      name: "adminpanelOrders",
      component: () => import("../componets/admin/AdminOrders.vue"),
      meta: {
        title: 'Заказы | Сир'
      }
    },
    {
      path: "/OrdersAdminComp",
      name: "ordersadmincomp",
      component: () => import("../componets/admin/OrdersAdminComp.vue")
    },
    {
      path: "/BasketAdmin/:id",
      name: "basketadmin",
      component: () => import("../componets/admin/BasketAdmin.vue"),
      meta: {
        title: 'Заказ | Сир'
      }
    },
    {
      path: "/TestComp",
      name: "testcomp",
      component: () => import("../componets/admin/TestComp.vue")
    },
    {
      path: "/Profile",
      name: "profile",
      component: () => import("../componets/Profile/ProfileComp.vue"),
      meta: {
        title: 'Профиль | Сир'
      }
    },
    {
      path: "/changeProduct/:id",
      name: "changeProduct",
      component: () => import("../componets/changeProduct/changeProduct.vue")
    },
  ],
});

router.beforeEach((to, from, next) => {
  const title = to.meta.title || 'Сир - Строительство и ремонт';
  document.title = title;
  next();
})

export default router;

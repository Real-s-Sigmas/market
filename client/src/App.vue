<script>
import MainPage from './componets/Main/MainPage.vue'
import HeaderPage from './componets/reuse/HeaderPage.vue'
import FooterPage from './componets/reuse/FooterPage.vue'
import ProductsPage from './componets/Product/ProductsPage.vue';
import CardProduct from './componets/Product/ProductPage.vue'
import StarRaiting from './componets/otherComp/StarRaiting.vue'

export default {
  components: {
    MainPage,
    HeaderPage,
    FooterPage,
    ProductsPage,
    CardProduct,
    StarRaiting,
  }
}
</script>

<template>
  <header-page></header-page>

  <!-- <main-page></main-page> -->
  <!-- <products-page></products-page> -->
  <!-- <card-product></card-product> -->
  <!-- <star-raiting></star-raiting> -->
   <router-view/>
   
  <footer-page></footer-page>
</template>

<style scoped></style>

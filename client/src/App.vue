<script>
import MainPage from './Main/MainPage.vue'
import HeaderPage from './HeaderAndFooter/HeaderPage.vue'
import FooterPage from './HeaderAndFooter/FooterPage.vue'
import ProductsPage from './Product/ProductsPage.vue';

export default {
  components: {
    MainPage,
    HeaderPage,
    FooterPage,
    ProductsPage 
  }
}
</script>

<template>
  <header-page></header-page>

  <!-- <main-page></main-page> -->
   <products-page></products-page>
   
  <footer-page></footer-page>
</template>

<style scoped></style>

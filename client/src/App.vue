<script>
import MainPage from './Main/MainPage.vue'
import HeaderPage from './HeaderAndFooter/HeaderPage.vue'
import FooterPage from './HeaderAndFooter/FooterPage.vue'
import ProductsPage from './Product/ProductsPage.vue';
import CardProduct from './Product/CardProduct.vue'
import StarRaiting from './otherComp/StarRaiting.vue'

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
  <card-product></card-product>
  <!-- <star-raiting></star-raiting> -->
   
  <footer-page></footer-page>
</template>

<style scoped></style>

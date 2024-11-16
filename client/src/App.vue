<script>
import MainPage from './componets/Main/MainPage.vue'
import HeaderPage from './componets/reuse/HeaderPage.vue'
import FooterPage from './componets/reuse/FooterPage.vue'
import ProductsPage from './componets/Product/ProductsPage.vue';
import CardProduct from './componets/Product/ProductPage.vue'
import StarRaiting from './componets/otherComp/StarRaiting.vue'
import CategoryComp from './componets/reuse/CategoryComp.vue'

export default {
  components: {
    MainPage,
    HeaderPage,
    FooterPage,
    ProductsPage,
    CardProduct,
    StarRaiting,
    CategoryComp,
  }
}
</script>

<template>
  <header-page></header-page>

  <!-- <main-page></main-page> -->
  <!-- <products-page></products-page> -->
  <!-- <card-product></card-product> -->
  <!-- <star-raiting></star-raiting> -->
  <!-- <category-comp></category-comp>  -->
   <div class="mh">
     <router-view/>
   </div>
   
  <footer-page></footer-page>
</template>

<style>
.mh {
  min-height: 67.65vh !important;
}
</style>

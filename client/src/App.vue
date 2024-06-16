<script>
import MainPage from './Main/MainPage.vue'
import HeaderPage from './HeaderAndFooter/HeaderPage.vue'

export default {
  components: {
    MainPage,
    HeaderPage,
  }
}
</script>

<template>
  <!-- <div
    class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center space-x-4 mt-7"
  >
    <div class="shrink-0">
      <img
        class="h-12 w-12"
        src="https://t3.ftcdn.net/jpg/05/36/46/64/360_F_536466456_ROneSNBzDA10yJfMQkLFsq9412N8yCiG.jpg"
        alt="ChitChat Logo"
      />
    </div>
    <div>
      <div class="text-xl font-medium text-black">Market</div>
      <p class="text-slate-500">У вас новое сообщение!</p>
    </div>
  </div> -->
  <!-- <header-page></header-page> -->
  <main-page></main-page>
</template>

<style scoped></style>

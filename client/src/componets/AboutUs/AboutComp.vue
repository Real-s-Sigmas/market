<script>
import YandexMap from '../reuse/YandexMap.vue'

export default {
  components: {
    YandexMap,
  }
}
</script>

<template>
  <div class="wind">
    <h1 class="about-title">О нас</h1>
    <div class="img-text">
      <img class="aboutus-img" src="../../assets/1111.jpeg" alt="">
      <p class="text"> lalalalalalalalalalalalalal </p>
    </div>
    <h3>Как нас найти?</h3>
    <div class="map">
      <YandexMap :center="[ 55.784428, 37.236963 ]" zoom="15" /> 
    </div>
  </div>
</template>

<style>
.wind {
  display: flex;
  flex-direction: column;
  gap: 40px;
  padding: 0 40px 0 40px;
}

.about-title {
  font-size: 30px;
  font-weight: 600;
  border-bottom: 2px solid #000;
  width: 90px;
}

.img-text {
  display: flex;
  gap: 60px;
}

.text {
  font-size: 22px;
}

.aboutus-img {
  width: 650px;
  border: 2px solid #000;
  border-radius: 12px;
}

h3 {
  font-size: 26px;
  font-weight: 600;
  border-bottom: 2px solid #000;
  width: 200px;
}

@media (max-width: 1000px) {
  .aboutus-img{
    width: 100%;
  }

  .img-text {
    flex-direction: column;
    gap: 20px;
  }
}

@media (max-width: 500px) {
  .about-title{
    font-size: 24px;
  }

  h3{
    font-size: 20px;
  }
}

@media (max-width: 430px) {
  .text {
    font-size: 20px;
  }
}
</style>

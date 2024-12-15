<script>
import YandexMap from "../reuse/YandexMap.vue";

export default {
  components: {
    YandexMap,
  },
};
</script>

<template>
  <div class="wind">
    <h1 class="about-title">О нас</h1>
    <div class="img-text">
      <img class="aboutus-img" src="../../assets/1111.jpeg" alt="" />
      <p class="text">
        <span>С.и.Р </span>- это магазин <span>Строительства и Ремонта</span>,
        который специализируется на продаже товаров, которые помогут вам сделать
        качественный ремонт и не только. У нас вы можете найти
        электроинструменты, отвертки, шпателя, лопаты, бензопилы, газонокосилки,
        газовые балоны, гвозди и саморезы, гаечные ключи и биты, батарейки и
        многое многое другое. С полным ассортиментом товаров вы можете
        ознакомиться в нашем <a href="/Catalog">Каталоге</a>. У вас, так же, есть
        возможность заказать интересующий вас товар.
      </p>
    </div>
    <h3 class="title-2">Как происходит заказ и получение товара?</h3>
    <p class="text">
      Выберите интересующий вас товар и добавьте его <span>в корзину</span>. После перехода в
      корзину нажмите кнопку <span> «Заказать».</span> На ваш электронный адрес (указанный при
      регистрации) придет подтверждение о принятии заказа. После сбора заказа вы
      получите уведомление с <span>адресом</span> самовывоза (он также указан на этой
      странице) и уникальным <span>кодом</span> заказа. Придя по указанному адресу,
      <span>предъявите код продавцу,</span> оплатите заказ и получите свой товар.
    </p>
    <h3>Как нас найти?</h3>
    <div class="map">
      <YandexMap :center="[55.784428, 37.236963]" zoom="15" />
    </div>
  </div>
</template>

<style scoped>
.wind {
  display: flex;
  flex-direction: column;
  gap: 40px;
  padding: 0 100px 0 100px;
}

.title-2 {
  width: 680px;
}

span,
a {
  color: #ff813c;
  font-weight: 600;
}

a {
  text-decoration: underline;
  transition: all 100ms;
}

a:hover {
  color: #d95700;
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
  text-align: justify;
}

.aboutus-img {
  width: 650px;
  border-radius: 12px;
}

h3 {
  font-size: 26px;
  font-weight: 600;
  border-bottom: 2px solid #000;
  width: 300px;
}

@media (max-width: 1250px) {
  .aboutus-img {
    width: 550px;
  }
}

@media (max-width: 1300px) {
  .wind {
    padding: 0 40px;
  }
}

@media (max-width: 1000px) {
  .aboutus-img {
    width: 100%;
  }

  .img-text {
    flex-direction: column;
    gap: 20px;
  }
}

@media (max-width: 790px) {
  .title-2 {
    width: 550px;
  }

  h3 {
    font-size: 22px;
  }
}

@media (max-width: 616px) {
  .title-2 {
    width: 90%;
  }
}

@media (max-width: 500px) {
  .wind {
    padding: 0 5px;
  }

  .about-title {
    font-size: 24px;
  }

  h3 {
    font-size: 20px;
  }
}

@media (max-width: 430px) {
  .text {
    font-size: 18px;
  }
}
</style>

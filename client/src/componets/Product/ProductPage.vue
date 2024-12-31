<script>
import axios from 'axios';

export default {
  data() {
    return {
      product_count: 1,
      isInCart: false,
      isInFavorite: false, // Является ли товар избранным у клинта

      text: "", // Текст отзыва клиента
      symb_count: 0, // Количество символов в комментарии
      red_text: false,
      rating: null, // Столько звезд, сколько выбрал пользователь
      mouseOverRating: null, // Показывает, на сколко звезд наводит пользователь

      starFull: "src/assets/star-full.svg",
      starEmpty: "src/assets/star-empty.svg",

      product: {},

      currentImageIndex: 0,
      photos: [
        "http://localhost:5173/src/assets/shup.png",
        "https://avatars.mds.yandex.net/i?id=a63e656f4279da0e7ce32f3a7fa74c6b_l-4238413-images-thumbs&n=13",
      ],
      visibleImages: 5,
      error: ``,
      isAdmin: false,
    };
  },

  methods: {
    // Увеличивает счетчик количества товаров на 1
    plus() {
      if (this.product_count <= 10000) {
        this.product_count++;
      } else {
        return;
      }
    },

    // Уменьшает счетчик количества товаров на 1
    minus() {
      if (this.product_count > 1) {
        this.product_count--;
      } else {
        return;
      }
    },

    // Проверяет, чтобы счетчик не заходил за 10000 и не уходил дальше 1
    checkCount() {
      if (this.product_count > 10000) {
        this.product_count = 10000;
      } else if (this.product_count < 1) {
        this.product_count = 1;
      }
    },

    // Отображаем выбранную оценку

    showCurrentRating(rating) {
      this.mouseOverRating = rating === 0 ? null : rating;
    },

    // Ставит выбранную оценку
    setCurrentSelectedRating(rating) {
      this.rating = rating;
      this.mouseOverRating = null;
    },

    symbCount() {
      this.symb_count = this.text.length;

      if (this.symb_count >= 2000) {
        this.red_text = true;
      } else {
        this.red_text = false;
      }
    },

    nextImage() {
      if (this.photos.length > 1 && this.currentImageIndex < this.photos.length - 2) {
        this.currentImageIndex++
        console.log(this.photos.length);
      }
    },

    prevImage() {
      if (this.currentImageIndex > 0) {
        this.currentImageIndex--;
      }
    },

    selectImage(index) {
      this.currentImageIndex = index;
    },

    async cb() {
      let res = await axios.get('/item/check-basket', {
        params: {
          id: this.$route.params.id,
        }
      });
      this.isInCart = res.data.res.isInCart;
      this.isInFavorite = res.data.res.isInFavorite;
    },

    async addToCart() {
      try {
        for(let i = 0; i < this.product_count; i++) {
          await axios.post('/basket/add-item', {
            id: this.$route.params.id,
          });
        }
        this.checkInBasket();
      } catch (error) {
        console.error(error)
      }
    },

    async deleteFromCart() {
      try {
        await axios.delete('/basket/delete-item', {
          params: {
            id: this.$route.params.id,
          }
        });
        this.isInCart = false;
        this.checkInBasket();
      } catch (error) {
        console.error(error)
      }
    },

    async addToFavotite() {
      try {
        if(this.isInFavorite) {
          this.deleteFavorite();
        } else {
          await axios.post('/basket/add-fav', {
            id: this.$route.params.id,
          });
          this.isInFavorite = true;
        }
        this.checkInFavorite();
      } catch (error) {
        console.error(error);
      }
    },

    async deleteFavorite() {
      try {
        await axios.delete('/basket/delete-fav', {
            params: {
              id: this.$route.params.id,
            }
          });
          this.isInFavorite = false;
        // this.checkInFavorite();
      } catch (error) {
        console.error(error);
      }
    },

    async getProduct() {
      try {
        let res = await axios.get('/items/one-item', {
          params: {
            id: this.$route.params.id
          }
        });
        if(res.data.res) {
          this.product = res.data.res;
          console.log(this.product.photos);
        } else {
          this.error = 'Ошибка! Товара не существует либо он был удалён';
        }
      } catch (error) {
        console.error(error);
        this.error = 'Ошибка! Товара не существует либо он был удалён';
      }
    },

    async checkInBasket() {
      try {
        let res = await axios.get('/basket/show-basket');
        for(let i = 0; i < res.data.res.length; i++) {
          // console.log(res.data.res[i].id == this.$route.params.id) id
          if(this.$route.params.id == res.data.res[i].id) {
            this.isInCart = true;
          }
        }
      } catch (error) {
        console.error(error)
      }
    },

    async checkInFavorite() {
      try {
        let res = await axios.get('/basket/show-favs');
        console.log(res.data);
        for(let i = 0; i < res.data.length; i++) {
          console.log(this.$route.params.id, res.data[i].id);
          if(this.$route.params.id == res.data[i].id) {
            this.isInFavorite = true;
          } else {
            this.isInFavorite = false;
          }
        }
      } catch (error) {
        console.error(error)
      }
    },
  },

  computed: {
    stars() {
      let starsArray = [];
      console.log(5);

      for (let i = 0; i < 5; i++) {
        if (i < this.product.rating_product) {
          starsArray.push(this.starFull);
        } else {
          starsArray.push(this.starEmpty);
        }
      }

      return starsArray;
    },

    visibleThumbnails() {
      const halfVisible = Math.floor(this.visibleImages / 2);
      let start = this.currentImageIndex - halfVisible;
      let end = this.currentImageIndex + halfVisible + 1;

      if (start < 0) {
        start = 0;
        end = this.visibleImages;
      }
      if (end > this.photos.length) {
        end = this.photos.length;
        start = this.photos.length - this.visibleImages;
      }

      return this.photos.slice(start, end);
    },

    async checkIsAdmin() {
      try {
        let res = await axios.get('/other/is-admin');
        this.isAdmin = res.data.res;
      } catch (error) {
        console.log(error);
      }
    },

    async deleteProduct() {
      try {
        await axios.delete('/items/delete-items', {
          params: {
            id: this.$route.params.id,
          }
        });
      } catch (error) {
        console.log(error);
      }
    }
  },

  mounted() {
    this.checkInBasket();
    this.checkInFavorite();
    this.getProduct();
    // this.checkIsAdmin();
  }
};
</script>
<template>
  <!-- Главное окно -->
  <div class="main-page-window" v-if='this.product.title'>
    <h2 v-if='this.error' class='text-red-500 text-3xl text-center'>{{ error }}</h2>
    <!-- Блок с информацией о товара (с картинкой) -->
    <div class="product-info">
      <div class="images">
        <img class="prod-img" :src="product.photos[currentImageIndex]" alt="" />
        <div class="mini-img">
          <button @click="prevImage" :disabled="currentImageIndex === 0">
            <img class="arrow-btn" src="../../assets/arrow-prev.svg" alt="" />
          </button>
          <div
           
            class="img-mini"
            v-for="image in product.photos"
            :key="image"
            :class="{
              'active-thumbnail': product.photos.indexOf(image) == currentImageIndex,
            }"
            @click="selectImage(product.photos.indexOf(image))">
            <img :src="image" alt="" />
          </div>
          <button
            @click="nextImage"
            :disabled="currentImageIndex == photos.length - 1"
          >
            <img class="arrow-btn" src="../../assets/arrow-next.svg" alt="" />
          </button>
        </div>
      </div>

      <!-- Бллок с информацией о товаре -->
      <div class="main-info">
        <h3>{{ product.title }}</h3>

        <!-- Блок с коротким описанием товара -->
        <p class="short-description">
          <span>Описание: </span> {{ product.descriptions }}
        </p>
        <a class="anc-link" href="#full-desc">Подробное описание</a>
        <div class="star-price-sum-order-fav">
          <div class="star-price">
            <!-- Блок с ценой -->
            <div class="price">
              <p>
                <b>Цена:</b> <span>{{ product.price }}</span> ₽
              </p>
            </div>
          </div>

          <div class="sum-order-fav">
            <!-- Блок с выбором количества товаров -->
            <div class="sum">
              <p>Количество:</p>
              <div class="buts-count">
                <button @click="plus" class="plus-btn">
                  <img src="../../assets/Plus.svg" alt="" />
                </button>
                <!-- input проверяет, чтобы в поле вводились только числа -->
                <input
                  @input="checkCount"
                  v-model="product_count"
                  class="count"
                  onkeyup="this.value = this.value.replace(/[^\d]/g,'');"
                />
                <button @click="minus" class="minus-btn">
                  <img src="../../assets/minus.svg" alt="" />
                </button>
              </div>
            </div>

            <div class="order-fav">
              <!-- Блок с кнопкой заказть -->
              <div class="order">
                <button v-if='!this.isInCart' @click='addToCart'>Добавить в корзину</button>
                <button class='bg-white' v-else @click='deleteFromCart'>В Корзине</button>
              </div>

              <!-- Блок с кнопкой "В избранное" -->
              <div class="fav" :class="{ favDone: this.isInFavorite }">
                <button @click="addToFavotite">
                  <svg
                    width="30px"
                    height="30px"
                    viewBox="0 0 24 24"
                    fill="white"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z"
                      stroke="#ff812c"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="btns-container flex justify-end gap-4 mb-10" v-if='this.isAdmin'>
      <button @click='this.$router.push(`/changeProduct/${this.$route.params.id}`)' class='btn-change border-2 border-black p-4 rounded-2xl'>Изменить</button>
      <button @click='deleteProduct' class='btn-change border-2 border-black p-4 rounded-2xl'>Удалить</button>
    </div>
    <hr />
    <!-- Блок с полным описанием -->
    <div class="full-description" id="full-desc">
      <p>
        <span>Полное описание товара: </span>
        {{ product.characteristics }}
      </p>
    </div>
    <hr />
  </div>
</template>

<style scoped>
.btn-change {
  border-color: #ff812c;
  transition: all 180ms;

  &:hover {
    background-color: #ff812c;
    color: #fff;
  }
}

/* Тесты */

/* Служебное */

.count::-webkit-outer-spin-button,
.count::-webkit-inner-spin-button {
  /* display: none; <- Crashes Chrome on hover */
  -webkit-appearance: none;
  margin: 0; /* <-- Apparently some margin are still there even though it's hidden */
}

/* Блок с информацией о товаре */

.arrow-btn {
  width: 40px;
}

.images {
  min-width: 400px;
}

.images {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.mini-img {
  margin-top: 10px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.img-mini {
  cursor: pointer;
  width: 70px;
  height: 70px;
  border: 2px solid #000;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: border 0.2s;
}

.img-mini img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.active-thumbnail {
  outline: 2px solid #ff802c;
}

.main-page-window {
  width: 100%;
  height: auto;
  margin: 0;
  user-select: text;
  padding: 0 120px 0 120px;

  overflow-x: hidden;
  overflow-y: hidden;
}

.product-info {
  display: flex;
  margin-top: 30px;
  gap: 40px;

  width: 100%;
  height: auto;

  padding-bottom: 80px;
}

.prod-img {
  -webkit-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
  box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
  width: 400px;
  height: 361px;

  border-radius: 10px;
}

.main-info {
  display: flex;
  flex-direction: column;
  gap: 40px;

  width: 100%;
  padding-right: 40px;
}

.main-info h3 {
  font-size: 35px;
  line-height: 38px;
  font-weight: 700;
}

.short-description {
  font-size: 24px;
}

.short-description span {
  font-weight: 700;
}

.anc-link {
  width: 350px;
  font-size: 24px;
  font-weight: 700;
  color: #ff812c;

  transition: all 200ms;
}

.anc-link:hover {
  color: #dd732d;
}

.anc-link:active {
  color: #b65e23;
}

/* Четыре блока в одном */

.star-price-sum-order-fav {
  display: flex;
  justify-content: space-between;

  width: 100%;
  height: 120px;

  margin-top: -25px;

  /* border: 2px solid #000; */
}

/* Оценка и цена */

.star-price {
  display: flex;
  flex-direction: column;
  gap: 29px;

  width: 300px;
  height: 140px;
}

.star {
  display: flex;
  align-items: center;
  gap: 6px;

  font-size: 24px;
  font-weight: 700;
  user-select: none;
}
.price b {
    color: black;
}
.price {
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ff802c;
  font-size: 24px;
  font-weight: 500;  
  width: 240px;
  height: 55px;

  border-radius: 12px;

  -webkit-box-shadow: 0px 0px 8px 6px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 0px 0px 8px 6px rgba(34, 60, 80, 0.2);
  box-shadow: 0px 0px 8px 6px rgba(34, 60, 80, 0.2);
}

/* Счетчик, кнопка заказать и избранные */

.sum-order-fav {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  width: 400px;

  /* border: 2px solid #000; */
}

/* Счетчик количества товаров */

.sum {
  width: 100%;
  /* border: 2px solid #000; */

  user-select: none;
}

.sum {
  display: flex;
  /* align-items: center; */
  justify-content: end;
  gap: 30px;

  bottom: 140px;
  right: -130px;
}

.sum p {
  font-size: 24px;
}

.buts-count {
  display: flex;
  justify-content: space-between;
  align-items: center;

  width: 175px;
  height: 40px;

  border-radius: 12px;
}

.buts-count button {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 45px;
  height: 40px;
  border: 2px solid #000;
  background-color: #d9d9d9;
  font-size: 24px;

  transition: all 200ms;
}

.buts-count button:hover {
  background-color: #afafaf;
}

.buts-count button:active {
  background-color: #959595;
}

.buts-count .plus-btn {
  border-radius: 12px 0 0 12px;
}

.buts-count .minus-btn {
  border-radius: 0 12px 12px 0;
}

.buts-count .count {
  text-align: center;
  font-size: 24px;
  width: 85px;
  height: 40px;
  border-top: 2px solid #000;
  border-bottom: 2px solid #000;
}

/* Кнопка заказать и избранное */

.order-fav {
  display: flex;
  justify-content: space-between;

  width: 100%;
  /* border: 2px solid #000; */
}

/* Кнопка заказать */

.order button {
  padding: 15px 25px;
  background-color: #ff812c;
  border-radius: 12px;
  color: #fff;
  font-size: 24px;
  font-weight: 700;

  user-select: none;

  transition: all 200ms;
}

.order button:hover {
  background-color: #dd732d;
}

.order button:active {
  background-color: #b65e23;
}

/* Кнопка "Добавить в избранное" */

.fav {
  display: flex;
  justify-content: center;
  align-items: center;

  border: 2px solid #505050;
  border-radius: 12px;

  transition: all 200ms;

  user-select: none;

  height: 65px;
  width: 65px;
}

.fav button {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 65px;
  height: 65px;
}

.fav:hover {
  background-color: #ff812c;
}

.fav:active {
  background-color: #b65e23;
}

.favDone {
  background-color: #ff812c;
}

/* Блок с полным описанием о товаре */

.full-description {
  margin-top: 60px;
  padding: 0 30px 60px 30px;
  width: 100%;
  height: auto;
}

.full-description {
  font-size: 24px;
  text-align: justify;
}

.full-description span {
  font-weight: 700;
}

/* Блок с отзывами */

.feedback-cont {
  display: flex;
  flex-direction: column;

  margin-top: 50px;
  padding: 0 30px 60px 30px;

  width: 100%;
  height: 1500px; /* Изменить на auto*/
}

.feedback-cont h2 {
  font-size: 35px;
  font-weight: 700;
}

.your-comment {
  display: flex;
  flex-direction: column;
  gap: 20px;

  margin-bottom: 70px;
}

.your-text {
  width: 100%;
  position: relative;
  border: 2px solid #000;
  border-radius: 12px;
  height: 260px;
}

.text-comm {
  width: 100%;
  height: 210px;

  font-size: 24px;

  border-radius: 12px;
  padding: 10px 10px 10px 10px;

  resize: none;
}

.text-comm:focus {
  outline: none;
}

.rate {
  display: flex;
  align-items: center;

  position: absolute;
  bottom: 5px;
  left: 10px;

  gap: 6px;

  font-size: 24px;
  font-weight: 700;

  user-select: none;
}

.symbols-count {
  position: absolute;

  font-size: 20px;
  color: #959595;
  bottom: 10px;
  right: 10px;
}

.red_text {
  color: #cb0404;
}

/* Окрашивание звезд при выборе оценки */

.star {
  cursor: pointer;
}

.filled {
  background: url("../../assets/star-full.svg") no-repeat;
}

.empty {
  background: url("../../assets/star-empty.svg") no-repeat;
}

/* Кнопка "Отправить (отзыв)" */

.send-comm {
  width: 240px;
  padding: 14px 0;
  background-color: #ff812c;

  font-size: 24px;
  color: #fff;

  border-radius: 12px;
  transition: all 200ms;

  user-select: none;
}

.send-comm:hover {
  background-color: #dd732d;
}

.send-comm:active {
  background-color: #b65e23;
}

/* Другие отзывы */

.other-comments {
  display: flex;
  flex-direction: column;
  gap: 35px;

  overflow-y: auto;

  width: 100%;
  height: 1000px;
  /* border: 1px solid #000; */
}

.title-sort {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sort select {
  font-size: 24px;

  color: #fff;
  background-color: #262626;
  border-radius: 12px;
  max-width: auto;
  height: 50px;
  padding: 2px 10px 2px 10px;
}

.sort option {
  font-size: 20px;
}

/* Блок с отзывом покупателя */

.comment-cont {
  display: flex;
  align-items: start;
  flex-direction: column;
  gap: 20px;

  width: 100%;
  height: 300px;
  /* border: 1px solid #000; */
}

.user-name {
  font-size: 24px;
  text-align: center;
  padding: 5px 12px;
  border: 2px solid #000;
  border-radius: 12px;
}

.user-text {
  width: 100%;
  padding: 5px;
  height: 320px;
  border: 2px solid #000;
  border-radius: 12px;

  margin-bottom: 20px;
}

.user-comment {
  width: 100%;
  height: 230px;
  padding: 5px;

  font-size: 24px;
}

.user-comment:focus {
  outline: none;
}

/* АДАПТИВКА */

@media (max-width: 1600px) {
  .star-price-sum-order-fav {
  }

  .short-description {
  }
}

@media (max-width: 1500px) {
  .star-price-sum-order-fav {
  }

  .sum {
    align-items: start;
  }

  .order-fav {
    margin-top: -40px;
  }

  .short-description {
    font-size: 24px;
  }
}

@media (max-width: 1420px) {
  .prod-img {
    width: 300px;
    height: 280px;
  }

  .main-info h3 {
    font-size: 28px;
  }

  .short-description {
    font-size: 20px;
  }

  .product-info {
    position: relative;
    padding-bottom: 200px;
  }

  .star-price-sum-order-fav {
    position: absolute;
    left: 0;
    bottom: 40px;
  }
}

@media (max-width: 1355px) {
  .star-price-sum-order-fav {
    gap: 50px;
  }
}

@media (max-width: 1300px) {
}

@media (max-width: 1265px) {
  .short-description {
    width: 90%;
  }

  .img-mini {
    width: 50px;
    height: 50px;
  }
}

@media (max-width: 1000px) {
  .main-page-window {
    padding: 0 20px;
  }
}

@media (max-width: 760px) {
  .order button {
    font-size: 20px;
  }
}

@media (max-width: 740px) {
  .product-info {
    align-items: center;
    flex-direction: column;
  }

  .prod-img {
    width: 350px;
    height: 350px;
  }

  .main-info {
    padding: 0;
  }

  .main-info h3 {
    font-size: 26px;
  }

  .short-description {
    font-size: 16px;
    width: 100%;
  }

  .anc-link {
    font-size: 18px;
  }

  .price {
    font-size: 20px;
  }

  .full-description {
    padding: 0;
    padding-bottom: 20px;
  }

  .full-description p {
    font-size: 16px;
  }

  .sort select {
    font-size: 18px;
    height: 40px;
  }

  .your-comment h2 {
    font-size: 22px;
  }

  .text-comm {
    font-size: 16px;
  }

  .feedback-cont {
    padding: 0;
  }

  .symbols-count {
    font-size: 14px;
  }

  .rate p {
    font-size: 18px;
  }

  .star {
    font-size: 18px;
  }

  .order button {
    font-size: 18px;
  }

  .fav {
    width: 57px;
    height: 57px;
  }

  .send-comm {
    font-size: 16px;
    width: 160px;
    padding: 12px 0;
  }

  .title-sort h2 {
    font-size: 22px;
  }

  .user-name {
    font-size: 16px;
  }

  .fav button {
    width: 57px;
    height: 57px;
  }

  .sum p {
    font-size: 18px;
  }

  .buts-count {
    height: 30px;
  }

  .buts-count button {
    height: 30px;
  }

  .plus-btn {
    img {
      width: 16px;
    }
  }

  .minus-btn {
    img {
      width: 16px;
    }
  }

  .buts-count {
    .count {
      font-size: 18px;
      height: 30px;
    }
  }

  .mini-img {
    gap: 8px;
  }
}

@media (max-width: 640px) {
  .price {
    width: 180px;
  }
}

@media (max-width: 590px) {
  .star-price-sum-order-fav {
    flex-direction: column;
    bottom: 180px;
  }

  .order-fav {
    margin-top: 10px;
  }

  .sum-order-fav {
    width: 312px;
    gap: 15px;
  }

  .sum {
    justify-content: start;
  }

  .main-info {
    margin-bottom: 150px;
  }

  .order-fav {
  }
}

@media (max-width: 460px) {
  .title-sort {
    flex-direction: column;
    align-items: start;
    gap: 10px;
  }
}

@media (max-width: 370px) {
  .order-fav {
    gap: 30px;
  }

  .sum p {
    font-size: 22px;
  }

  .sum {
    gap: 10px;
  }

  .full-description p {
    font-size: 16px;
  }
}
</style>

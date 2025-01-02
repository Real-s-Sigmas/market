<script>
import axios from "axios";

export default {
  data() {
    return {
      products: [],
      title: ``,
      error: ``,
      errorProduct: ``,

      orderRead: false,

      errorOrder: ``,

      quantityMap: {},
      displayedItems: []
    };
  },

  mounted() {
    this.loadProducts();
  },

  methods: {
    async loadProducts() {
      try {
        const res = await axios.get("/basket/get-items");
        let keyys = res.data.res.basket_dict;

        const keys = Object.keys(keyys);

        for (let i = 0; i < keys.length; i++) {
          let responce = await axios.get('/items/one-item', {
            params: {
              id: keys[i]
            }
          });

          let item = responce.data.res;

          this.products.push({
            title: item.title,
            category: item.category,
            characteristics: item.characteristics,
            date_create: item.date_create,
            descriptions: item.descriptions,
            id: item.id,
            photos: item.photos,
            price: item.price,
            small_category: item.small_category,
            count: res.data.res.basket_dict[keys[i]]
          });

          console.log(this.products);
        }
      } catch (error) {
        this.error = "Ошибка! Невозможно найти товары";
      }
    },


    async deleteProduct(id) {
      try {
        await axios.put("/basket/update-item", {
          id: id,
          count: 0,
        });
        this.products.forEach((item) => {
          if(id == item.id) {
            let i = this.products.indexOf(item)
            this.products.splice(i, 1);
          }
        });
      } catch (error) {
        this.error = "Действие невозможно. Повторите попытку позже";
      }
    },
    async loadOrder() {
      try {
        let ids = [];

        for (let i = 0; i < this.products.length; i++) {
          ids.push({
            id: this.products[i].id,
            count: this.products[i].count
          },);
        }

        let res = await axios.post("/order/add-order", {
          ids: ids,
        });

        if (res.data.res == "Error") {
          this.errorOrder = "Ошибка! Невозможно создать заказ";
        } else {
          this.errorOrder = "";
        }
      } catch (error) {
        this.errorOrder = "Ошибка! Невозможно создать заказ";
      }

      this.orderRead = !this.orderRead;
    },
  },
};
</script>

<template>
  <div v-if="this.orderRead">
    <div class="modal-page">
      <h2 v-if="!this.errorOrder">
        Заказ сформирован, статус заказа вы можете посмотреть на почте, на
        которую регистрировали данный аккаунт. По готовности, заказ будет ждать
        вас в пункте выдачи. Адрес вы можете посмотреть, перейдя
        <a href="/aboutus" class="text-blue-500 hover:underline transition-all duration-500">по этой ссылке</a>
      </h2>
      <h2 v-else>{{ errorOrder }}</h2>
      <div class="close-img" @click="this.orderRead = !this.orderRead">x</div>
    </div>
    <div class="bg-black"></div>
  </div>

  <div class="orders-container mx-10" v-if="this.products.length != 0">
    <h2 class="mt-10 text-3xl font-bold">Корзина</h2>

    <h2 class="text-red-500 text-xl text-semibold flex justify-center mt-10 mb-4" v-if="this.errorProduct">
      {{ errorProduct }}
    </h2>

    <div class="products-container">
      <div class="card border-b-2  py-4 mt-1" v-for="product in products" v-if='this.products.length'>
        <div class="info-card flex gap-6 justify-between">
          <div class="info-container flex gap-6">
            <img class="rounded-xl" :src="product.photos[0]" />
            <div class="info-block flex flex-col gap-0 relative text-base">
              <h3 class="text-3xl font-bold">{{ product.title }}</h3>
              <p class="mt-5">
                <b>Описание:</b> {{ product.characteristics.substring(0, 40)
                }}<span v-if="product.characteristics.length >= 40">...</span>
              </p>
              <span>Количество: {{ product.count }}</span>
              <span class="absolute bottom-0 left-0"><b>Цена:</b>
                <p class="price">{{ product.price }} ₽</p>
              </span>
            </div>
          </div>
          <div class="actions flex gap-3">
            <button class="del-btn" @click="deleteProduct(product.id)">
              Удалить из корзины
            </button>
            <button class="order-btn" @click="this.$router.push(`/Product/${product.id}`)">
              К товару
            </button>
          </div>
        </div>
      </div>
      <h2 class="text-red-500 text-xl text-semibold flex justify-center mt-10" v-if="this.error">
        {{ error }}
      </h2>
    </div>
    <div class="ord">
      <button class="ord-button" @click="loadOrder">Заказать</button>
    </div>
  </div>




  <!-- центрируйте пж -->
  <h2 v-if='this.products.length == 0' class="mt-10 text-3xl bask-empty font-bold">Корзина пуста!</h2>

</template>

<style scoped>
.bask-empty {
  padding-top: 30px;
  text-align: center;
}

.price {
  font-size: 30px;
  color: #ff812c;
}

img {
  -webkit-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
  box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
}

.search {
  margin: 20px 0;
  /* width: 100%;  */

  display: flex;
  justify-content: center;
  align-items: center;

  gap: 55px;

  input {
    border: 2px solid #ff812c;
    border-radius: 12px;
    width: 720px;
    height: 45px;
    padding: 0 10px;
  }

  .search-find {
    padding: 10.5px 42px;
    border-radius: 50px;
    background-color: #ff812c;
    color: #fff;

    transition: all 100ms;
  }

  .search-find:hover {
    background-color: #d95700;
  }
}

.close-img {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 30px;
  font-weight: 500;
  cursor: pointer;
}

.bg-black {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background: #000;
  z-index: 50;
  opacity: 0.6;
}

.modal-page {
  position: fixed;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  padding: 30px;
  border: 2px solid black;
  border-radius: 20px;
  width: 40%;
  height: 40%;
  top: 30%;
  left: 30%;
  background: #fff;
  z-index: 52;
  opacity: 1;
}

.ord {
  width: 100%;
  display: flex;
  justify-content: end;
}

.actions {
  height: 80px;
  margin-top: 45px;
}

@media (max-width: 1030px) {
  .info-card {
    flex-direction: column;
    position: relative;
    gap: 0px;
  }

  .info-card img {
    width: 100% !important;
    height: 250px;
  }

  .info-container {
    flex-direction: column;
  }

  .info-block span {
    position: relative;
  }

  .actions {
    justify-content: space-between;
  }

  .search {
    gap: 20px;
  }

  .price {
    position: relative;
    margin-top: 10px;
    width: fit-content;
  }
}

@media (max-width: 920px) {
  .modal-page {
    left: 20%;
    top: 20%;
    width: 50%;
    height: 50%;
  }
}

@media (max-width: 630px) {
  .modal-page {
    left: 5%;
    width: 90%;
  }
}

@media (max-width: 800px) {
  .info-card {
    flex-direction: column;
    position: relative;
    gap: 0px;
  }

  .info-card img {
    width: 100% !important;
    height: 250px;
  }

  .info-container {
    flex-direction: column;
  }

  .info-block span {
    position: relative;
  }

  .actions {
    justify-content: space-between;
  }

  .text-3xl {
    font-size: 1.5rem;
  }
}


.del-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  border-radius: 12px;
  padding: 10px 20px;

  font-size: 18px;

  transition: all 200ms;

  background-color: #ffffff;
}

.del-btn {
  -webkit-box-shadow: 0px 2px 8px 7px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 0px 2px 8px 7px rgba(34, 60, 80, 0.2);
  box-shadow: 0px 2px 8px 7px rgba(34, 60, 80, 0.2);
}

.del-btn:hover {
  background-color: #000;
  /* border: 2px solid #FF812C; */
  color: #fff;
}

.order-btn {
  width: 200px;
  height: 50px;
  border-radius: 12px;
  color: #fff;

  font-size: 22px;

  transition: all 200ms;

  background-color: #fc6600;
}

.ord-button {
  margin-top: 30px;
  width: 200px;
  height: 50px;
  border-radius: 12px;
  border: 2px solid #ff812c;
  color: #fff;

  font-size: 22px;

  transition: all 200ms;

  background-color: #fc6600;
}

.ord-button:hover,
.order-btn:hover {
  background-color: #fff !important;
  color: #fc6600;
}

.btn {
  width: 260px;
  height: 50px;
  border-radius: 12px;
  border: 2px solid #ff812c;
  color: #ff812c;

  font-size: 22px;

  transition: all 200ms;
}

.btn:hover {
  background-color: #ff812c;
  color: #fff;
}

.btn:active {
  background-color: #d95700;
  border-color: #d95700;
}

input {
  border-radius: 12px;
  border: 2px solid #ff812c;

  font-size: 19px;

  transition: all 200ms;

  padding: 0 10px;

  outline: none;
}

.info-card img {
  width: 250px;
  height: 250px;
  object-fit: cover;
}

@media (max-width: 620px) {
  .orders-container {
    margin-left: 0.5rem;
    margin-right: 0.5rem;
  }
}

@media (max-width: 470px) {
  .del-btn {
    font-size: 16px;
  }

  .order-btn {
    font-size: 16px;
    width: auto;
    padding: 0 40px;
  }
}

@media (max-width: 400px) {
  .actions {
    flex-direction: column;
    height: auto;
  }


}
</style>  

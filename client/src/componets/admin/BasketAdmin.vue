<script>
import axios from 'axios';
export default {
  data() {
    return {
      order: {},
      error: ``,
      status: ``,

      orderProducts: [],
    }
  },

  methods: {
    async getOrder() {
      try {
        let res = await axios.get('/admin/order', {
          params: {
            id: this.$route.params.id
          }
        });

        this.order = res.data.res[0];

        for(let i = 0; i < this.order.ids_items.length; i++) {

          let responce = await axios.get('/items/one-item', {
              params: {
                  id: res.data.res[0].ids_items[i].id,
              }
          });
          let item = responce.data.res;
          this.orderProducts.push({
              category: item.category,
              characteristics: item.characteristics,
              date_create: item.date_create,
              descriptions: item.descriptions,
              id: res.data.res[0].id,
              photos: item.photos,
              price: item.price,
              small_category: item.small_category,
              title: item.title,
              count: res.data.res[0].ids_items[i].count
          });
        }

        this.status = res.data.res[0].status;

      } catch (err) {
        console.error(err);
        this.error = 'Невозможно найти заказ';
      }
    },

    async changeStatus() {
      try {
        await axios.put('/admin/change-status', {
          id: this.$route.params.id,
          status: this.status
        });
       // this.getOrder();
      } catch (error) {
        console.error(err);
      }
    }
  },

  mounted() {
    this.getOrder();
  }
}  
</script>

<template>
  <div class="window">
    <div class="tabs">
      <button @click="this.$router.push('/AdminPanel/actions')">
        Действия
      </button>
      <button @click="this.$router.push('/AdminPanel/orders')">
        Заказы
      </button>
    </div>
    <div class="orderNumber" v-if='!this.error'>
      <p>Номер телефона пользователя: {{ order.phonenumber }}</p>
      <p>{{order.id}}</p>
      <p>Дата создания: {{ order.date_create }}</p>
      <div class="select">
        <select class='border-2 rounded-2xl p-4' v-model='status'>
            <option value="" selected>Выбрать статус заказа</option>
            <option value="NEW">NEW</option>
            <option value="END">END</option>
            <option value="PROCESS">PROCESS</option>
            <option value="WAITING">WAITING</option>
        </select>
          
        <span>Текущий статус заказа: {{ status }}</span>  
        
        <button class='text-base' @click='changeStatus'>Изменить статус заказа</button>
      </div>
      
    </div>
    
    <div class="orders" v-if='!this.error && this.orderProducts.length'>
      <div class="card" v-for='(item, index) in orderProducts'>
        <div class="image-info">
          <div class="image">
            <img :src="item.photos[0]" alt="">
          </div>
          <div class="info">
            <div class="code-count">
              <p>Количество: {{ item.count }}шт</p>
            </div>

            <div class="title-desc">
              <h2><b>{{ item.title }}</b></h2>
              <h4>Описание: {{ item.descriptions }}</h4>
            </div>

            <p class="price">Цена: {{ item.price }} р</p>
          </div>
        </div>

        <div class="btns flex flex-col">
          <button @click='this.$router.push(`/Product/${order.ids_items[index].id}`)'>К товару</button>
          <div class="flex items-center gap-6">
            
          </div>
        </div>
      </div>
    </div>
    <h2 v-else class='text-red-500 font-bold text-2xl flex justify-center'>{{ error }}</h2>
  </div>
</template>

<style scoped>
.window {
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;

  padding: 0 100px;


  .tabs {
    display: flex;
    justify-content: center;
    gap: 80px;

    button {
      color: #fff;
      background-color: #ff813c;
      width: 250px;
      height: 45px;
      border-radius: 50px;

      font-size: 20px;
      font-weight: 500;

      transition: all 100ms;
    }

    button:hover {
      background-color: #d95700;
    }
  }

  .orderNumber {
    width: 100%;

    p {
      font-size: 20px;
    }

    .select {
      span {
        margin: 0 15px;
      }

      display: flex;
      gap: 15px;
      align-items: center;
      margin-top: 20px;

      .text-base {
        background-color: #ff813c;
        border-radius: 8px;
        padding: 8px 20px;
        color: #fff;
        transition: all 200ms;
      }

      .text-base:hover {
        background-color: #d95700;
      }
    }
  }

  .orders {
    width: 100%;
    height: 1000px;


    .card {
      display: flex;
      align-items: center;
      transition: all 200ms;
      padding: 20px;
      border-radius: 20px;

      h2,
      h4 {
        display: -webkit-box !important;
        -webkit-line-clamp: 2 !important;
        -webkit-box-orient: vertical !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }


      .btns {
        button {
          color: #fff;
          background-color: #ff813c;
          font-size: 20px;
          font-weight: 500;
          width: 200px;
          height: 50px;
          border-radius: 8px;
        }
      }

      .image-info {
        display: flex;
        align-items: center;
        width: 90%;
        gap: 30px;

        img {
          min-width: 250px;
          height: 250px;
          border-radius: 12px;
          -webkit-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
          -moz-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
          box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
        }

        .info {
          display: flex;
          flex-direction: column;
          height: 250px;
          justify-content: space-between;

          .code-count {
            p {
              margin-bottom: 10px;
            }
          }

          .price {
            text-align: center;
            border: 1px solid #000;
            border-radius: 6px;
            padding: 5px 0;
            font-weight: 500;
            width: 200px;
          }
        }
      }


    }

    .card:hover {
      transform: translateY(-10px);
      -webkit-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
      -moz-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
      box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);

    }
  }
}


@media (max-width: 1355px) {
  .window {
    padding: 30px;
  }
}

@media (max-width: 830px) {
  .window {
    padding: 5px;
  }

  .card {
    padding: 20px 5px !important;
  }
}

@media (max-width: 830px) {
  .card {
    flex-direction: column;

    .btns {
      padding-top: 20px;
    }

    .btns button {
      width: 360px ;
    }
  }
}

  @media (max-width: 780px) {
    .select {
      flex-direction: column;
      align-items: start !important;
    }
  }

@media (max-width: 670px) {
  .image-info {
    flex-direction: column;
  }
}


@media (max-width: 625px) {
  .tabs {
    gap: 10px !important;

    button {
      width: 200px !important;
      font-size: 16px !important;
    }
  }
}

@media (max-width: 420px) {
  .tabs {
    button {
      width: 150px !important;
    }
  }
}

@media (max-width: 400px) {
  .btns button {
  }
}
</style>

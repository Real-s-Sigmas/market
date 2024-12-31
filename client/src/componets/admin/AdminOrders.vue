<script>
import axios from 'axios';
import OrdersAdminComp from '../admin/OrdersAdminComp.vue';
  
  export default {
    data() {
      return {
        orders: [],
        error: ``,
      }
    },

    components: {
      OrdersAdminComp,
    },

    methods: {
      async getOrders() {
        try {
            let res = await axios.get('/admin/orders');
            
            for(let i = 0; i < res.data.res[0].ids_items.length; i++) {
                let responce = await axios.get('/items/one-item', {
                    params: {
                        id: res.data.res[0].ids_items[i].id,
                    }
                });
                let item = responce.data.res;
                this.orders.push({
                    category: item.category,
                    characteristics: item.characteristics,
                    date_create: item.date_create,
                    descriptions: item.descriptions,
                    id: res.data.res[i].id,
                    photos: item.photos,
                    price: item.price,
                    small_category: item.small_category,
                    title: item.title,
                    count: res.data.res[0].ids_items[i].count
                });
            }
            console.log(this.orders);
        } catch (err) {
            console.error(err)
        }
      },
    },

    mounted() {
      this.getOrders();
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
  <h2 v-if='this.error' class='text-red-500 font-bold text-2xl flex justify-center'>{{ error }}</h2>
  <div class="orders-list">
    <OrdersAdminComp v-for='order in orders' :order='order'></OrdersAdminComp>
  </div>
</div> 
</template>

<style scoped>
.window {
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
  
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

  

  .orders-list {
    display: grid;
    grid-auto-rows: auto; /* Высота строки задается автоматически */
    grid-template-columns: repeat(4, minmax(200px, 1fr)); /* Автоматическое добавление столбцов */
    grid-gap: 30px;
    width: auto;
    max-width: 90%;
    max-height: 1000px; /* Ограничиваем высоту блока */
    overflow-y: auto; /* Добавляем прокрутку, если элементы превышают высоту */

    justify-items: center;

  }
  
}

      @media (max-width: 1480px) {
        .orders-list {
          width: 98% !important;
        }
      }

      @media (max-width: 1325px) {
        .orders-list {
          grid-template-columns: repeat(3, minmax(200px, 1fr)) !important;
        }
      }
      
      @media (max-width: 1000px) {
        .orders-list {
          grid-template-columns: repeat(2, minmax(200px, 1fr)) !important;
          
        }
      }

      @media (max-width: 700px) {
        .orders-list {
          grid-template-columns: repeat(1, minmax(200px, 1fr)) !important;
          
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

      
</style>

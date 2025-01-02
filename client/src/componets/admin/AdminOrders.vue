<script>
import axios from 'axios';
import OrdersAdminComp from '../admin/OrdersAdminComp.vue';

export default {
  data() {
    return {
      orders: [],
      error: ``,
      search: ``,
    }
  },

  components: {
    OrdersAdminComp,
  },

  methods: {
    async getOrders() {
      try {
        let res = await axios.get('/admin/orders');
        this.orders = res.data.res.reverse();
      } catch (err) {
        console.error(err)
      }
    },

    async findOrders() {
      try {
        let res = await axios.get('/orders/search', {
          params: {
            search: this.search
          }
        });
        this.orders = res.data.res;
      } catch (error) {
        console.error(error)
      }
    }
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

    <div class="search">
      <input type="search" v-model='search' placeholder='Поиск заказов'>
      <button class="search-find flex gap-2" @click='findOrders'><span class="find-word">Найти</span> <img class="find-img"
          src="../../assets/icons/find-icon.svg"></button>
      <img src="" alt="">
    </div>

    <h2 v-if='this.error' class='text-red-500 font-bold text-2xl flex justify-center'>{{ error }}</h2>
    <div class="orders-list">
      <OrdersAdminComp v-for='order in orders' :order='order'></OrdersAdminComp>
    </div>
  </div>
</template>

<style scoped>
.search {
  margin-top: 40px;
  width: 55%;

  display: flex;
  justify-content: center;
  align-items: center;

  gap: 18px;

  input {
    border: 2px solid #ff812c;
    border-radius: 12px;
    width: 720px;
    height: 45px;
    padding: 0 10px;
    outline: none !important;
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

@media (max-width: 1250px) {
  .search {
    width: 80%;
  }
}

@media (max-width: 1035px) {
  .search {
    input {
      width: 90%;
    }
  }
}

@media (max-width: 775px) {
  .search {
    input {
      width: 60%;
    }

    .search-find {
      padding: 8px 20px;
    }
  }
}

@media (max-width: 400px) {
  .search {
    input {
      width: 48%;
    }
  }
}

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
    grid-auto-rows: auto;
    /* Высота строки задается автоматически */
    grid-template-columns: repeat(4, minmax(200px, 1fr));
    /* Автоматическое добавление столбцов */
    grid-gap: 30px;
    width: auto;
    max-width: 90%;
    max-height: 1000px;
    /* Ограничиваем высоту блока */
    overflow-y: auto;
    /* Добавляем прокрутку, если элементы превышают высоту */

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

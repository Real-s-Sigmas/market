<script>
import ProductComp from "./ProductComp.vue";
import CategoryComp from '../reuse/CategoryComp.vue'

export default {
  data() {
    return {
      // isOpen: false,
    };
  },
  components: {
    ProductComp,
    CategoryComp,
  },
};
</script>

<template>
  <div class="dark" v-if="this.isOpen"></div>
  <div class="main-page-window">
    <div class="search">
      <input type="text" name="" id="" class="search-inp" />
      <button class="find-btn">Найти</button>
    </div>

    <div class="category-and-products">
      <!-- <div class="category" :class="{ open: this.isOpen }">
        <ul>
          <button
            @click="this.isOpen = !this.isOpen"
            :class="{ 'btn-open': this.isOpen }"
          >
            <img src="../../assets/menu.svg" alt="" />
          </button>
          <li class="categ-item item-electro">Электроинструменты</li>
          <li class="categ-item">Ручные инструменты</li>
          <li class="categ-item">Крепеж</li>
          <li class="categ-item">Отделочные материалы</li>
          <li class="categ-item">Тепловые пушки</li>
        </ul>
      </div> -->

      <category-comp></category-comp>

      <div class="products">
        <h2>Название категории</h2>
        <div class="cards">
            <product-comp/>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dark {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: #000;
  opacity: 0.4;
  z-index: 51;
}

.margin-products {
  margin-left: 2.9%;
}

.main-page-window {
  width: 100%;
  height: 100vh;

  margin: 0 20px 0 20px;
  display: flex;
  flex-direction: column;

  user-select: none;
}

.search {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 60px;

  margin-top: 20px;

  width: 100%;
  height: 100px;

  /* Убрать потом */
  /* border: 2px solid #000; */
}

.search-inp {
  outline: none;
  border: 2px solid #ff812c;
  border-radius: 12px;
  padding: 0 20px 0 20px;

  width: 800px;
  height: 42px;
}

.find-btn {
  border: 2px solid #ff812c;
  border-radius: 12px;

  width: 100px;
  height: 42px;

  transition: all 100ms;
}

.find-btn:hover {
  background-color: #ff812c;
  color: #fff;
}

.find-btn:active {
  background-color: #d95700;
  border-color: #d95700;
}

.category-and-products {
  display: flex;
  gap: 60px;

  position: relative;

  width: 100%;
}
/*
.category {
  display: flex;
  justify-content: center;
  color: #fff;

  padding: 0 20px 0 20px;

  width: 300px;
  height: 750px;
  background-color: #ff812c;
  border-radius: 12px;

  transition: all 400ms;
}

.category ul {
  display: flex;
  flex-direction: column;

  gap: 5px;

  margin-top: 10px;
}

.categ-item {
  cursor: pointer;
  font-size: 16px;
} */

.products {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
  width: 100%;
  height: 100%;
  /* border: 3px solid #000; */
}

.products h2 {
  width: 100%;
  font-size: 45px;
}

.cards {
  width: 100%;
  height: 100%;
  /* border: 3px solid #000; */
  padding-top: 10px;

  display: flex;
  flex-wrap: wrap;
  gap: 40px;

  overflow-y: scroll;
}

.prod-card {
  width: 260px;
  height: 330px;
  /* border: 3px solid #000; */

  display: flex;
  flex-direction: column;
}

.prod-card img {
  width: 300px;
  height: 255px;
}

.product-name {
  font-size: 30px;
  color: #505050;
}

.btn-price {
  color: #fff;
  background-color: #ff812c;
  height: 50px;
  font-size: 30px;
  border-radius: 12px;
}

/* .category.open {
  margin-left: -30px;
  border-radius: 15px;
  padding: 10px 40px 0 10px;
  width: 250px;
  position: absolute;
}

.btn-open {
  position: absolute;
  margin-left: 180px !important;
  margin-top: -10px;
} */

/* @media (min-width: 800px) {
  .category button {
    display: none;
  }
} */

@media (max-width: 800px) {
  /* .category button {
    margin-left: 200px;
    position: absolute;
  }

  .category {
    margin-left: -270px;
    padding: 0;
    border-radius: 0 10px 15px 0;
    position: absolute;
    z-index: 52;

    transition: all 400ms;
  } */

  .cards {
    gap: 70px;
    justify-content: center;
  }

  .category-and-products {
    gap: 20px;
  }

  .products {
    margin-left: 40px;
  }

  .products h2 {
    font-size: 30px;
  }

  .prod-card {
    width: 250px;
    height: 300px;
  }

  .prod-card img {
    width: 250px;
    height: 300px;
  }

  .product-name {
    font-size: 20px;
  }

  .btn-price {
    height: 30px;
    font-size: 20px;
  }

  .search {
    gap: 10px;
    height: 80px;
  }
}

@media (max-width: 650px) {
  .prod-card {
    width: 190px;
    height: 260px;
  }

  .prod-card img {
    width: 190px;
    height: 280px;
  }

  .cards {
    padding-top: 0;
  }
}

@media (max-width: 530px) {
  .prod-card {
    width: 160px;
    height: 220px;
  }

  .cards {
    gap: 10px;
  }
}
</style>

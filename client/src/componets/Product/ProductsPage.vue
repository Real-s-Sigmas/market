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
  <div class="main-page-window">
    <div class="search">
        <input type="text">
        <button class="search-find">Найти</button>
    </div>

    <div class="products">
      <h2>Название категории</h2>
      <div class="cards">
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
          <product-comp/>
      </div>
    </div>
  </div>
</template>

<style scoped>

.products {
  h2 {
    font-size: 35px;
    font-weight: 600;
    margin-bottom: 40px;
  }
}

.cards {
  display: grid;
  grid-template-columns: auto auto auto auto;
  gap: 20px;
  justify-items: center;
}

.main-page-window {
    padding: 0 100px 0 100px;
    
    margin-top: 20px;
    
    display: flex;
    flex-direction: column;
    justify-content: start;
    gap: 40px;
    
    width: 100%;
    height: auto;
}

.search {
    margin-top: 40px;
    width: 100%; 
    
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

  @media (max-width: 1325px) {
    .cards {
      grid-template-columns: auto auto auto;
    }

    .main-page-window {
      padding: 0 40px;
    }

    
  }

  @media (max-width: 1000px) {
    .search {
        position: absolute;
        top: -10px;
        left: 20px;
        gap: 15px;

        input {
            width: 50%;
        }
    }
  }

  @media (max-width: 1000px) {
    .cards {
      grid-template-columns: auto auto;
    }
  }

  @media (max-width: 775px) {
    .search  {
        input {
            width: 35%;
        }

        .search-find {
            padding: 8px 20px;
        }
    }
  }

  @media (max-width: 490px) {
    .cards {
    }
  }

  @media (max-width: 465px) {
    .products {
      h2 {
        font-size: 28px;
      }
    }

    .search {
      left: 2px;
    }

    .main-page-window {
      padding: 0 5px;
    }
  }
</style>

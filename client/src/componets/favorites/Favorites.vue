<script>
import axios from "axios";

export default {
  data() {
    return {
      products: [
        {
          id: 52,
          photos: [`src/assets/1111.jpeg`],
          title: `Отвертка подзалупная. `,
          description: `loremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremlorem`,
          price: 52000,
          
        },
        {
          id: 52,
          photos: [`src/assets/1111.jpeg`],
          title: `Чё то тут`,
          description: `Чё то там`,
          price: 52000,
        },
      ],
      title: ``,
      error: ``,
      errorProduct: ``,
    };
  },

  mounted() {
    // this.loadProducts();
  },

  methods: {
    async loadProducts() {
      try {
        let res = await axios.get("/user/get-favorites");
        this.products = res.data.res;
      } catch (error) {
        this.error = "Ошибка! Невозможно найти товары";
      }
    },

    async deleteProduct(id, index) {
      try {
        if (!this.products[index].isFavorite) {
          await axios.delete("/user/delete-favorites", {
            params: {
              id: id,
            },
          });
          this.products[index].isFavorite = true;
        } else {
          await axios.post("/user/post-favorites", {
            params: {
              id: id,
            },
          });
          this.products[index].isFavorite = false;
        }
      } catch (error) {
        this.error = "Действие невозможно. Повторите попытку позже";
        console.log(error)
      }
      
    },
  },
};
</script>

<template>
  <div class="orders-container mx-10">
    <h2 class="mt-10 text-3xl font-bold">Избранные товары</h2>

    <h2
      class="text-red-500 text-xl text-semibold flex justify-center mt-10 mb-4"
      v-if="this.errorProduct"
    >
      {{ errorProduct }}
    </h2>

    <div class="products-container">
      <div
        class="card border-b-2  py-4 mt-1"
        v-for="(product, index) in products"
      >
        <div class="info-card flex gap-6 justify-between">
          <div class="info-container flex gap-6">
            <img class="rounded-xl image" :src="product.photos[0]" />
            <div class="info-block flex flex-col gap-0 relative text-base">
              <h3 class="text-3xl font-bold">{{ product.title }}</h3>
              <p class="mt-5"> 
                <b>Описание:</b> {{ product.description.substring(0, 30)
                }}<span v-if="product.description.length >= 40">...</span>
              </p>
              <span class="absolute bottom-0 left-0"
                ><b>Цена:</b>  <p class="price">{{ product.price }} ₽</p></span
              >
            </div>
          </div>
          <div class="actions flex gap-3">
            <button
              class="like-btn mt-4"
              @click="deleteProduct(product.id, index)"
            >
              <svg v-if="product.isFavorite"  width="29px" height="29px" viewBox="0 0 24 24" fill="#f0853f" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              
              <svg v-else width="29px" height="29px" viewBox="0 0 24 24" fill="#f0853f" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>

            </button>
            <button
              class="order-btn mt-4 btn-liink"
              @click="this.$router.push(`/Product/${product.id}`)"
            >
              К товару
            </button>
          </div>
        </div>
      </div>
      <h2
        class="text-red-500 text-xl text-semibold flex justify-center mt-10"
        v-if="this.error"
      >
        {{ error }}
      </h2>
    </div>
  </div>
</template>

<style scoped>
.price{
    font-size: 30px;
    color: #ff812c;
}
.btn-liink{
    -webkit-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
  box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2); 
}
.like-btn{
    -webkit-box-shadow: 0px 2px 8px 7px rgba(34, 60, 80, 0.2);
-moz-box-shadow: 0px 2px 8px 7px rgba(34, 60, 80, 0.2);
box-shadow: 0px 2px 8px 7px rgba(34, 60, 80, 0.2);
}
.image {
  -webkit-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
  box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
}


  .like-btn:hover {
    svg {
      fill: #fff;
    }
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

  .search {
    gap: 20px;
  }
}

@media (max-width: 500px) {
  .search {
    input {
      width: 100%;
    }
    .search-find {
      padding: 10.5px 20px;
    }
  }
}

.like-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50px;
  height: 50px;
  border-radius: 12px;
  color: #fff;

  font-size: 22px;

  transition: all 200ms;

  background-color: #ffffff;
}

.like-btn img {
  width: 30px !important;
  height: 30px !important;
}

.like-btn:hover {
  background-color: #fc6600;
  border: 2px solid #ff812c;
  color: #fff !important;
}

.order-btn {
  width: 200px;
  height: 50px;
  border-radius: 12px;
  border: 2px solid #ff812c;
  color: #fff;

  font-size: 22px;

  transition: all 200ms;

  background-color: #fc6600;
}

.order-btn:hover {
  background-color: #fff;
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
</style>

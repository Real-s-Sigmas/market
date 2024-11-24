<script>
import axios from 'axios';

export default {
    data() {
        return {
            products: [
                {
                    id: 52,
                    image: `src/assets/1111.jpeg`,
                    title: `Чё то тут`,
                    description: `Чё то там, Чё то тамЧё то тамЧё то тамЧё то тамЧё то там`,
                    price: 52000,
                },
                {
                    id: 52,
                    image: `src/assets/1111.jpeg`,
                    title: `Чё то тут`,
                    description: `Чё то там`,
                    price: 52000,
                },
            ],
            title: ``,
            error: ``,
            errorProduct: ``,
        }
    },

    mounted() {
        // this.loadProducts();
    },

    methods: {
        async loadProducts() {
            try {
                let res = await axios.get('/favorites');
                this.products = res.data.res;
            } catch (error) {
                this.error = 'Ошибка! Невозможно найти товары';
            }
        },

        async deleteProduct(id, index) {
            try {
                if(!this.products[index].isFavorite) {
                    await axios.delete('/favorites', {
                        params: {
                            id: id
                        }
                    });
                    this.products[index].isFavorite = true;
                } else {
                    await axios.post('/favorites', {
                        params: {
                            id: id
                        }
                    });
                    this.products[index].isFavorite = false;
                }
            } catch (error) {
                this.error = 'Действие невозможно. Повторите попытку позже';
            }
        },

        async findProducts() {
            try {
                let res = await axios.get('/favorites/find-by-title', {
                    params: {
                        title: this.title,
                    }
                });
                if(res.data.res) {
                    this.products = res.data.res;
                } else {
                    this.errorProduct = 'Товаров не найдено';
                }
            } catch (error) {
                this.errorProduct = 'Невозможно найти товар. Повторите попытку позже';
            }
        }
    }
}
</script>


<template>
    <div class="orders-container mx-10">
        <h2 class='mt-10 text-3xl font-bold'>Избранные товары</h2>
        <form class="search" @submit.prevent='findProducts()'>
            <input type="text" v-model='title'>
            <button class="search-find" type="submit">Найти</button>
        </form>


        <h2 class='text-red-500 text-xl text-semibold flex justify-center mt-10 mb-4' v-if='this.errorProduct'>{{ errorProduct }}</h2>

        <div class="products-container">
            <div class="card border-b-2 border-black py-4 mt-1" v-for='(product, index) in products'>
                <div class="info-card flex gap-6 justify-between">
                    <div class="info-container flex gap-6">
                        <img class='rounded-xl border-2 border-black' :src="product.image">
                        <div class="info-block flex flex-col gap-0 relative text-base">
                            <h3 class='text-4xl font-bold'>{{ product.title }}</h3>
                            <p>Описание: {{ product.description.substring(0, 40) }}<span v-if='product.description.length >= 40'>...</span> </p>
                            <span class='absolute bottom-0 left-0'>Цена: {{ product.price }}</span>
                        </div>
                    </div>
                    <div class="actions flex gap-3">
                        <button class="like-btn mt-4" @click='deleteProduct(product.id, index)'>
                            <img v-if='product.isFavorite' src="../../assets/icons/favoriteDelete.svg" alt="favorite">
                            <img v-else src="../../assets/icons/favorite.svg" alt="favorite">
                        </button>
                        <button class="order-btn mt-4" @click='this.$router.push(`/Product/${product.id}`)'>К товару</button>
                    </div>
                </div>
            </div>
            <h2 class='text-red-500 text-xl text-semibold flex justify-center mt-10' v-if='this.error'>{{ error }}</h2>
        </div>
    </div>
</template>


<style scoped>
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
        justify-content: space-between
    }

    .search {
        gap: 20px;
    }
}
    
@media (max-width: 500px) {
    .search  {
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
    border: 2px solid #000000;
    color: #fff;

    font-size: 22px;

    transition: all 200ms;

    background-color: #ffffff;
}

.like-btn img {
    width: 20px !important;
    height: 20px !important;
}

.like-btn:hover {
    background-color: #FC6600;
    border: 2px solid #FF812C;
    color: #fff !important;
}

.order-btn {
    width: 200px;
    height: 50px;
    border-radius: 12px;
    border: 2px solid #FF812C;
    color: #fff;

    font-size: 22px;

    transition: all 200ms;

    background-color: #FC6600;
}

.order-btn:hover {
    background-color: #fff;
    color: #FC6600;
}

.btn {
    width: 260px;
    height: 50px;
    border-radius: 12px;
    border: 2px solid #FF812C;
    color: #FF812C;

    font-size: 22px;

    transition: all 200ms;
}

.btn:hover {
    background-color: #FF812C;
    color: #fff;
}

.btn:active {
    background-color: #d95700;
    border-color: #d95700;
}

input {
    border-radius: 12px;
    border: 2px solid #FF812C;

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
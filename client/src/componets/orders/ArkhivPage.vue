<script>
import axios from 'axios';

export default {
    data() {
        return {
            products: [
                {
                    code: 8652525252,
                    image: `src/assets/1111.jpeg`,
                    title: `Чё то тут`,
                    count: 52,
                    description: `Чё то там, Чё то тамЧё то тамЧё то тамЧё то тамЧё то там`,
                    price: 52000,
                },
                {
                    code: 8652525252,
                    image: `src/assets/1111.jpeg`,
                    title: `Чё то тут`,
                    count: 52,
                    description: `Чё то там`,
                    price: 52000,
                },
            ],
            title: ``,
        }
    },

    mounted() {
        // this.loadProducts();
    },

    methods: {
        async loadProducts() {
            let res = await axios.get('/basket/history');
            this.products = res.data;
        },

        async findProducts() {
            let res = await axios.get('/favorites/find-by-title', {
                params: {
                    title: this.title,
                }
            });
            this.products = res.data;
        }
    }
}
</script>


<template>
    <div class="orders-container mx-10">
        <div class="flex gap-8">
            <h2 @click="this.$router.push('/myorders')" class='mt-10 text-3xl font-bold w-fit cursor-pointer'>Все заказы</h2>
            <h2 class='mt-10 text-3xl font-bold border-b-2 border-black w-fit cursor-pointer'>Архив</h2>
        </div>
        

        <div class="products-container">
            <div class="card border-b-2 border-black py-4 mt-1" v-for='(product) in products'>
                <div class="info-card flex gap-6 justify-between">
                    <div class="info-container flex gap-6">
                        <img class='rounded-xl border-2 border-black' :src="product.image">
                        <div class="info-block flex flex-col gap-0 relative text-base">
                            <h3 class='text-4xl font-bold'>{{ product.title }}</h3>
                            <span>Код товара: {{ product.code }}</span>
                            <span>Количество: {{ product.count }}</span>
                            <p>Описание: {{ product.description.substring(0, 40) }}<span v-if='product.description.length >= 40'>...</span> </p>
    
                            <span class='absolute bottom-0 left-0'>Цена: {{ product.price }}</span>
                        </div>
                    </div>
                    <button class="order-btn mt-4" @click='this.$router.push(`/Product/${product.id}`)'>К товару</button>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
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
    width: 300px;
    height: 300px;
    object-fit: cover;
}
</style>

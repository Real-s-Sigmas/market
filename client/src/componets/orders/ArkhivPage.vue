<script>
import axios from 'axios';

export default {
    data() {
        return {
            products: [],
            title: ``,
        }
    },

    mounted() {
        this.loadProducts();
    },

    methods: {
        async loadProducts() {
            try {
                let res = await axios.get('/admin/get-arc');
                
                for(let i = 0; i < res.data.res[0].ids_items.length; i++) {
                    let responce = await axios.get('/items/one-item', {
                        params: {
                            id: res.data.res[0].ids_items[i].id,
                        }
                    });
                    this.status = res.data.res[0].status;
                    let item = responce.data.res;
                    this.products.push({
                        category: item.category,
                        characteristics: item.characteristics,
                        date_create: item.date_create,
                        descriptions: item.descriptions,
                        id: item.id,
                        photos: item.photos,
                        price: item.price,
                        small_category: item.small_category,
                        title: item.title,
                        count: res.data.res[0].ids_items[i].count
                    });
                }
                console.log(this.products);
            } catch (err) {
                console.error(err)
            }
        },
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
                            <p>Описание: {{ product.descriptions.substring(0, 40) }}<span v-if='product.descriptions.length >= 40'>...</span> </p>
                            <p>Количество: {{ product.count }}</p>
                            <p>Статус товара: {{ status }}</p>
    
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

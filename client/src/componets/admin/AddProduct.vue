<script>
import axios from 'axios';

export default {
    data() {
        return {
            form: {
                title: ``, 
                description: ``, 
                price: null, 
                photos: [], 
                topic: ``,
                fullDescription: ``,
            },

            topics: [],
        }
    },

    mounted() {
        this.getTopics();
    },

    methods: {
        async addProduct() {
            await axios.post('/items/new-item', {
                form: this.form,
            });
        },

        async getTopics() {
            let res = await axios.get('/items/topics');
            this.topics = res.data.all;
        }
    }
}
</script>


<template>
    <form @submit.prevent='addProduct' class="post-container xl:mx-12 flex flex-col mt-16">
        <div class="up-info flex xl:gap-20 justify-center">
            <div class="image-container input-file border-black border-2 py-20 rounded-xl flex justify-center items-center select-none" role='button'>
                <input type="file" name="file">
                <span>+</span>
            </div>
            <div class="flex flex-col gap-2 text-5xl font-semibold">
                <label for="title">Название:</label>
                <input type="text" id='title' v-model='form.title' class='mb-5'>
                <label for="title">Краткое описание:</label>
                <input type="text" id='title' v-model='form.description'>
            </div>
            <select class='text-5xl' v-model='form.topic' >
                <option selected value="">Категория</option>
                <!-- v-for='topic in topics' -->
                <!-- <option value="topic">{{ topic }}</option> -->
            </select>
        </div>
        <div class="m-c flex flex-col">
            <label for="fullDescription" class='text-5xl font-semibold mt-16'>Подробное описание:</label>
            <textarea id='fullDescription' rows='7' v-model='form.fullDescription' class='border-2 border-black mt-3 p-1 rounded'></textarea>
        </div>
        <div class="price-block m-c flex flex-col">
            <label for="price" class='text-5xl font-semibold mt-16'>Цена товара:</label>
            <div class="flex gap-3">
                <input id='price' v-model='form.price' class='price border-2 border-black mt-3 p-1'>
                <span class='font-semibold relative'>₽ <div class="minus absolute">-</div></span>
            </div>
        </div>
    </form>
</template>


<style scoped>
.input-file {
	position: relative;
	display: flex;
}
.input-file span {
	font-size: 250px;
    font-weight: 100;
	transition: color 0.3s;
}
.input-file input[type=file] {
	position: absolute;
	z-index: -1;
	opacity: 0;
	display: block;
	width: 0;
	height: 0;
}

/* Focus */
.input-file input[type=file]:focus + span {
	box-shadow: 0 0 0 0.2rem rgba(0,123,255,.25);
}

/* Hover/active */
.input-file:hover span {
	color: #FF812C;
}
.input-file:active span {
	color: #c76a2c;

}
/* Disabled */
.input-file input[type=file]:disabled + span {
	color: #eee;
}

select {
    margin-top: 50px;
    height: 90px;
    background-color: #FF812C;
    color: #fff;
    border-radius: 10px;
    padding: 15px;
}

input {
    width: 100%;
    height: 80px;
    padding: 5px;

    font-size: 20px;

    border: 2px solid #000;

    border-radius: 5px;
}

.image-container {
    height: 300px;
    width: 30%;
    font-size: 250px;
    font-weight: 100;
}

.price {
    width: 500px;
    height: 50px;
}

.m-c {
    margin: 0 185px;
}

.price-block div span {
    font-size: 45px;
}

.minus {
    bottom: -25px;
    left: 0;
    width: 100000px;
}
</style>
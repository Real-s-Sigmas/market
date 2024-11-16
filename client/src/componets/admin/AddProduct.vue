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
        // this.getTopics();
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
        },


        convertImages(event) {
            let files = event.target.files;
            let imagesArray = [];

            for(let i = 0; i < files.length; i++) {
                const reader = new FileReader();
                reader.onload = () => {
                    imagesArray.push(reader.result);
                    if (imagesArray.length === files.length) {
                        this.form.photos = imagesArray;
                    }
                };
                reader.readAsDataURL(files[i]);
            };
        },

        deleteImage(index) {
            this.form.photos.splice(index, 1);
        }
    }
}
</script>


<template>
    <form @submit.prevent='addProduct' class="post-container xl:mx-12 mx-0 flex flex-col mt-16">
        <div class="up-info flex xl:gap-16 justify-between">
            <label for="filee" class="input-file">
                <div class="image-container border-black border-2 py-20 rounded-xl flex justify-center items-center select-none"
                    role='button'>
                    <input type="file" name="file[]" id='filee' multiple @change='convertImages' accept="image/*">
                    <span>+</span>
                </div>
            </label>
            <div class="main-info-block flex flex-col">
                <div class="main-inputs-block flex flex-row xl:gap-16 xl:mt-0 mt-4">
                    <div class="flex flex-col gap-2 text-5xl font-semibold flex-1">
                        <label for="title">Название:</label>
                        <input type="text" id='title' v-model='form.title' class='mb-5'>
                    </div>
                    <div class="select-block">
                        <select class='text-4xl font-semibold px-5 pe-16 mt-3' v-model='form.topic'>
                            <option selected value="">Категория</option>
                            <option :value="topic" v-for='topic in topics'>{{ topic }}</option>
                        </select>
                        <img class='arrow-down' src="../../assets/arrowDown.png">
                    </div>
                </div>
                <div class="text-5xl font-semibold">
                    <label for="desc_short mt-1">Краткое описание:</label>
                    <textarea class='short-desc border border-black mt-3' rows='10' type="text" id='desc_short'
                        v-model='form.description'></textarea>
                </div>
            </div>
        </div>

        <div id="imageContainer">
            <div class="one-image" v-for='(image, index) in form.photos'>
                <img class='image-one' :src="image" alt="Изображение">
                <img @click='deleteImage(index)' class='close-btn' src="../../assets/close-img.png">
            </div>
        </div>

        <div class="m-c flex flex-col">
            <label for="fullDescription" class='text-5xl font-semibold mt-8'>Подробное описание:</label>
            <textarea id='fullDescription' rows='10' v-model='form.fullDescription'
                class='border-2 border-black mt-3 p-1 rounded'></textarea>
        </div>
        <div class="price-block m-c flex flex-col">
            <label for="price" class='text-5xl font-semibold mt-8'>Цена товара:</label>
            <div class="flex gap-3">
                <input id='price' v-model='form.price' class='price border-2 border-black mt-3 p-1'>
                <span class='font-semibold relative'>Р</span>
            </div>
        </div>
    </form>
</template>


<style scoped>
.select-block {
    position: relative;
}

.arrow-down {
    position: absolute;
    bottom: 55px;
    right: 10px;
    z-index: 10;
}

.one-image {
    position: relative;
}

.close-btn {
    position: absolute;
    top: -15px;
    right: -15px;
    padding: 8px;
    background-color: #2B2B2B;
    z-index: 52;
    border-radius: 100%;
    cursor: pointer;
}

#imageContainer {
	display: flex;
	gap: 62px;
	flex-wrap: wrap;
	/* justify-content: space-between; */
    margin-top: 30px !important;
}

.image-one {
    width: 150px;
    height: 150px;
    border-radius: 15px;
    object-fit: cover;
    border: 3px solid #2B2B2B;
}

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

.input-file:hover span {
    color: #FF812C;
}

select {
    margin-top: 50px;
    height: 80px;
    background-color: #FF812C;
    color: #fff;
    border-radius: 10px;
    appearance: none;
    position: relative;
}

input,
textarea {
    width: 100%;
    padding: 5px;

    font-size: 20px;

    border: 2px solid #000;

    border-radius: 5px;
}

input {
    height: 80px;
}

.short-desc {
    width: 100%;
}

.image-container {
    height: 433px;
    width: 433px;
    font-size: 250px;
    font-weight: 100;
}

@media (min-width: 1400px) {

    .up-info {
        margin: 0 185px;
    }

    .main-info-block {
        flex-grow: 1;
    }


    .m-c {
        margin: 0 185px;
    }

    #imageContainer {
        margin: 0 185px;
    }
}

@media (max-width: 1400px) {

    .m-c,
    .up-info {
        margin: 0 30px;
    }
}

@media (max-width: 1284px) {
    .image-container {
        width: 100%;
    }

    .up-info,
    .main-inputs-block {
        flex-direction: column !important;
    }

    select {
        margin-top: 0;
        margin-bottom: 15px;
        width: 100%;
    }

    #imageContainer {
        margin: 10px 30px !important;
        gap: 15px;
        justify-content: center;
    }

    .image-one {
        width: 75px;
        height: 75px;
        border-radius: 15px;
        object-fit: cover;
        border: 3px solid #2B2B2B;
    }

    .close-btn {
        padding: 4px;
    }

    .text-5xl, .text-4xl {
        font-size: 20px !important;
    }

    select {
        padding-left: 10px;
    }

    .arrow-down {
        bottom: 45px;
    }
}

.price {
    width: 500px;
    height: 50px;
}

.price-block div span {
    font-size: 45px;
}
</style>
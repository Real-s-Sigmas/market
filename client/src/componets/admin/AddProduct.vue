<script>
import axios from 'axios';
import { Category } from "./categories.js";
import { Catalog } from "../Catalog/catalog.js";

export default {
    data() {
        return {
            form: {
                title: ``,
                description: ``,
                price: null,
                photos: [],
                topic: ``,
                descriptions: ``,
                characteristics: ``,
            },

            topics: Category,
            underTopics: [],
            error: ``,
        }
    },

    watch: {
       'form.topic'(newValue) {
           this.underTopics = [];
           for (let i = 0; i < Catalog.length; i++) {
               if (Object.keys(Catalog[i])[0] == this.form.topic.category) {
                   for (let j = 0; j < Catalog[i][Object.keys(Catalog[i])[0]].length; j++) {
                       this.underTopics.push(Catalog[i][Object.keys(Catalog[i])[0]][j].title);
                   }
               }
           }
       }
   },
   
    methods: {
        async addProduct() {
            try {
                let res = await axios.post('/items/new-item', {
                    form: this.form,
                });
                if (res.data.res == 'Error') {
                    this.error = 'Ошибка добавления товара';
                } else {
                    this.$router.push('/');
                }
            } catch (error) {
                this.error = 'Ошибка добавления товара';
            }
        },


        convertImages(event) {
            let files = event.target.files;
            let imagesArray = [];

            for (let i = 0; i < files.length; i++) {
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
    <form @submit.prevent='addProduct' class="post-container mx-0 flex flex-col mt-16">
        <div class="up-info flex xl:gap-16 justify-between">
            <label for="filee" class="input-file">
                <div class="image-container border-black py-20 rounded-xl flex justify-center items-center select-none"
                    role='button'>
                    <input type="file" name="file[]" id='filee' multiple @change='convertImages' accept="image/*">
                    <span>+</span>
                </div>
            </label>
            <div class="main-info-block flex flex-col">
                <div class="main-inputs-block flex flex-row xl:gap-12 xl:mt-0 mt-4">
                    <div class="flex flex-col gap-2 text-2xl  flex-1">
                        <label for="title">Название:</label>
                        <input type="text" id='title' v-model='form.title' class='mb-5'>
                    </div>
                    <div class="select-block">
                        <select class='sell text-2xl px-10 pe-16 mt-3' v-model='form.topic'>
                            <option selected value="">Категория</option>
                            <option :value="topic" v-for='topic in topics'>{{ topic.category }}</option>
                        </select>
                        <select class='sell text-2xl px-10 pe-16 mt-3' v-model='form.under_topic' v-if='this.form.topic'>
                            <option selected value="">Подкатегория</option>
                            <option :value="title" v-for='title in underTopics'>{{ title }}</option>
                        </select>
                    </div>
                </div>
                <div class="text-2xl ">
                    <label for="desc_short mt-1">Краткое описание:</label>
                    <textarea class='short-desc border border-black mt-3' rows='2' type="text" id='desc_short'
                        v-model='form.descriptions'></textarea>
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
            <label for="fullDescription" class='text-2xl  mt-8'>Подробное описание:</label>
            <textarea id='fullDescription' rows='10' v-model='form.characteristics'
                class='border-2 border-black mt-3 p-1 rounded'></textarea>
        </div>
        <div class="price-block m-c flex xl:justify-between xl:flex-row flex-col gap-10">
            <label for="price" class='text-2xl mt-8'>Цена товара:</label>
            <div class="flex gap-3">
                <input id='price' v-model='form.price' class='price border-2 border-black mt-3 p-1'>
            </div>
            <button type='submit' class='acc mt-8'>Добавить</button>
        </div>
        <h2 class='text-red-500 text-xl text-semibold mt-10' v-if='this.error'>{{ error }}</h2>
    </form>
</template>


<style scoped>
.acc {
    padding: 8px 34px;
    border-radius: 50px;

    background-color: #ff812c;
    color: #fff;

    font-size: 20px;
    font-weight: 600;

    transition: all 200ms;
}

.acc:hover {
    background-color: #d95700;
}

.select-block {
    position: relative;
}

.arrow-down {
    position: absolute;
    bottom: 40px;
    right: 35px;
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
    background-color: #1E1E1E;
    z-index: 52;
    border-radius: 100%;
    cursor: pointer;
}

#imageContainer {
    display: flex;
    gap: 62.8px;
    flex-wrap: wrap;
    /* justify-content: space-between; */
    margin-top: 30px !important;
}

.image-one {
    width: 120px;
    height: 120px;
    border-radius: 15px;
    object-fit: cover;
    border: 3px solid #1E1E1E;
}

.input-file {
    position: relative;
    display: flex;
}

.input-file span {
    font-size: 185px;
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
    margin-top: 38px;
    height: 52px;
    background-color: #FF812C;
    color: #fff;
    border-radius: 15px;
    appearance: none;
    position: relative;
    background-image: url('../../assets/arrowDown.png');
    background-size: 24px 12px;
    background-position: 85% 54%;
    background-repeat: no-repeat;
}

@media (max-width: 1124px) {
    select {
        background-position: 96% 54%;
    }
}

input,
textarea {
    width: 100%;
    padding: 8px;

    font-size: 20px;

    border: 3px solid #000;

    border-radius: 10px;
}

input {
    height: 52px;
}

textarea {
    height: 120px;
}

.short-desc {
    width: 100%;
}

.image-container {
    height: 280px;
    width: 280px;
    font-size: 185px;
    font-weight: 100 !important;
    border: 3px solid #1E1E1E;
}

@media (min-width: 1400px) {
    .post-container {
        margin-left: 260px;
        margin-right: 260px;
    }


    .up-info,
    .text-red-500 {
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
    .up-info,
    .text-red-500 {
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
        border-radius: 13px;
        object-fit: cover;
        border: 3px solid #1E1E1E;
    }

    .close-btn {
        padding: 4px;
    }

    .text-xl {
        font-size: 20px !important;
    }

    select {
        padding-left: 10px;
    }

    .arrow-down {
        bottom: 32px;
    }

    .price-block {
        flex-direction: column;
        gap: 0;
    }

    .price {
        margin-top: 0 !important;
    }
}

.price {
    width: 500px;
    height: 50px;
    border: none;
    border-bottom: 3px solid #1E1E1E;
    border-radius: 0 !important;
    margin-top: 24px;

    &:focus {
        outline: none;
    }
}

.price-block div span {
    font-size: 45px;
}
</style>

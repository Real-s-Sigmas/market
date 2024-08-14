<script>
import HeaderPage from '../reuse/HeaderPage.vue';
import FooterPage from '../reuse/FooterPage.vue'
import CategoryComp from '../reuse/CategoryComp.vue'

export default {
    data() {
        return {
            images: [
                'src/assets/1111.jpeg',
                'src/assets/112.jpg',
                'src/assets/123.webp',
                'src/assets/124.webp',
                'src/assets/125.webp',
            ],
            index: 0,
        }
    },

    components: {
        HeaderPage,
        FooterPage,
        CategoryComp,
    },

    methods: {
        plus() {
            if (this.index < this.images.length-1) {
                this.index++;
            } else {
                this.index = 0;
            }

        },

        minus() {
            if (this.index > 0) {
                this.index--;
            } else {
                this.index = this.images.length-1;
            } 
        },
    },
    
    computed: {
        
    }

    
}
</script>

<template>

    <!-- Главное окно -->
    <div class="main-page-window">

        <!-- Строка поиска -->
        <div class="search">
            <input type="text" name="" id="" class="search-inp" />
            <button class="find-btn">Найти</button>
        </div>

        <!-- Блок с категориями и баннером -->
        <div class="category-and-banner">

            <!-- Блок с категориями -->
            <div class="category">
                <category-comp></category-comp>
            </div>

            <!-- Блок с баннером -->
            <div class="banner">
                <button class="left-btn" @click="minus"><</button>
                <img :src="images[index]" alt="">
                <button class="right-btn" @click="plus">></button>
            </div>
        </div>
    </div>
</template>

<style scoped>


    /* Главное окно */
    .main-page-window {
        margin: 0 20px 0 20px;
        display: flex;
        flex-direction: column;
        
        width: 100%;
        height: auto;

    }


    /* Строка поиска */
    .search {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 60px;

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


    /* Категория и баннер */
    .category-and-banner {
        display: flex;
        justify-content: space-between;
        gap: 100px;

    }


    /* Блок с баннерoм */
    .banner {
        display: flex;
        justify-content: center;
        align-items: center;
        
        margin-top: 30px;
        width: 1000px;
        height: 600px;
        border: 2px solid #000;
        /* background-color: #ff812c; */
        border-radius: 14px;

        margin-right: 180px;

        position: relative;
    }

    .banner img {

        border: 2px solid #000;

        object-fit: cover;
        width: 985px;
        height: 585px;

        border-radius: 12px;
    }

    .banner button {
        position: absolute;
        top: 50%;
        border-top: 2px solid #000;
        border-bottom: 2px solid #000;
        z-index: 100;

        background-color: #fff;


        font-size: 35px;
        font-weight: 200;

        width: 120px;
        height: 80px;

    }

    .left-btn {
        border-right: 2px solid #000;

        border-radius: 0 12px 12px 0;
        left: 6px;
    }
    
    .right-btn { 
        border-left: 2px solid #000;

        border-radius: 12px 0 0 12px;
        right: 6px;
    }

</style>
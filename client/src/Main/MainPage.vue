<script>
import HeaderPage from '@/HeaderAndFooter/HeaderPage.vue';
import FooterPage from '@/HeaderAndFooter/FooterPage.vue'

export default {
    data() {
        return {
            images: [
                'src/assets/1111.jpeg',
                'src/assets/112.jpg'
            ],
            index: 0,
        }
    },

    components: {
        HeaderPage,
        FooterPage,
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
                this.index = 1;
            } 
        },
    },
    
    computed: {
        
    }

    
}
</script>

<template>
    <div class="main-page-window">
        <header-page></header-page>
        <div class="search">
            <input type="text" name="" id="" class="search-inp">
            <button class="find-btn">Найти</button>
        </div>

        <div class="category-and-banner">
            <div class="category">
                <ul>
                    <li class="categ-item">Электроинструменты</li>
                    <!-- <li class="categ-item"></li> -->
                    <li class="categ-item">Ручные инструменты</li>
                    <li class="categ-item">Крепеж</li>
                    <li class="categ-item">Отделочные материалы</li>
                    <li class="categ-item">Тепловые пушки</li>
                </ul>
            </div>
            <div class="banner">
                <button class="ban-btn btn-left" @click="minus"><</button>
                <img :src="images[index]" alt="">
                <button class="ban-btn btn-right" @click="plus">></button>
            </div>
        </div>
    </div>
    <footer-page></footer-page>
</template>

<style>
    .main-page-window {
        margin: 0 50px 0 50px;
        display: flex;
        flex-direction: column;

        user-select: none;
    }

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
        border: 2px solid #FF812C;
        border-radius: 12px;
        padding: 0 20px 0 20px;

        width: 800px;
        height: 42px;
    }

    .find-btn {
        border: 2px solid #FF812C;
        border-radius: 12px;
        
        width: 100px;
        height: 42px;
        
        transition: all 100ms;
    }

    .find-btn:hover {
        background-color: #FF812C;
        color: #fff;
    }

    .find-btn:active {
        background-color: #d95700;
        border-color: #d95700;
    }
    

    .category-and-banner {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 200px;

        width: 100%;
        height: 750px;
        /* border: 2px solid #000; */
    }

    .category {
        display: flex;
        justify-content: center;
        color: #fff;

        width: 300px;
        height: 750px;
        background-color: #FF812C;
        /* border: 2px solid #FF812C; */
        border-radius: 12px;
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
    }

    .banner {
        width: 1050px;
        height: 550px;
        border: 2px solid #000;
        border-radius: 12px;

        position: relative;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .banner img {
        width: 841px;
    }

    .ban-btn {
        position: absolute;

        transition: all 100ms;
    }

    .ban-btn:hover {
        background-color: #b9b9b9;
    }

    .ban-btn:active {
        background-color: #a1a1a1;
    }

    .btn-left {
        left: 30px;
        background-color: #D9D9D9;
        font-size: 30px;

        width: 70px;
        height: 70px;
        border-radius: 12px;
    }

    .btn-right {
        right: 30px;
        background-color: #D9D9D9;
        font-size: 30px;


        width: 70px;
        height: 70px;
        border-radius: 12px;
    }

</style>
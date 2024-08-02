<script>
import HeaderPage from '../reuse/HeaderPage.vue';
import FooterPage from '../reuse/FooterPage.vue'

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

    <!-- Главное окно -->
    <div class="main-page-window">

        <!-- Строка поиска -->
        <div class="search">
            <input type="text" name="" id="" class="search-inp" />
            <button class="find-btn">Найти</button>
        </div>

        <!-- Блок с категориями и баннером -->
        <div class="category-and-banner">
            <div class="category">
                
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
        height: 100vh;
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
</style>
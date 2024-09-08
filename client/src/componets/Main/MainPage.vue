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
            
            categories: [
                {
                    name: 'Электроинструменты',
                    subItems: [
                        { name: 'Дрели', subSubItems: ['Аккумуляторные дрели', 'Сетевые дрели'] },
                        { name: 'Перфораторы', subSubItems: ['SDS+', 'SDS Max'] },
                        { name: 'Шуруповерты', subSubItems: ['Сетевые шуруповерты', 'Аккумуляторные шуруповерты'] },
                    ],
                },
                {
                    name: 'Ручные инструменты',
                    subItems: [
                        { name: 'Молотки', subSubItems: ['Кувалды', 'Столярные молотки'] },
                        { name: 'Отвертки', subSubItems: ['Крестовые', 'Плоские'] },
                        { name: 'Клещи', subSubItems: ['Комбинированные клещи', 'Длинногубцы'] },
                    ],
                }
            ],

            activeIndex: null,
            activeSubIndex: null,
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

        showSubMenu(index) {
            this.activeIndex = index;
            this.activeSubIndex = null;
        },
        
        showSubSubMenu(subIndex) {
            this.activeSubIndex = subIndex;
        },

        hideAllMenus() {
            this.activeIndex = null;
            this.activeSubIndex = null;
        }
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
            <div class="category" @mouseleave="hideAllMenus">
                <ul>
                    <li v-for="(item, index) in categories"
                        :key="index"
                        class="categ-item"
                        @mouseenter="showSubMenu(index)">
                        {{ item.name }}
                        <div class="submenu" v-show="activeIndex === index">
                            <ul>
                                <li v-for="(subItem, subIndex) in item.subItems"
                                    :key="subIndex"
                                    @mouseenter="showSubSubMenu(subIndex)">
                                    {{ subItem.name }}
                                    <div class="subsubmenu" v-show="activeSubIndex === subIndex">
                                        <ul>
                                            <li v-for="(subSubItem, subSubIndex) in subItem.subSubItems" :key="subSubIndex">
                                                <a href="#!">{{ subSubItem }}</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                            </ul>
                        </div>

                    </li>

                    <!-- <li class="categ-item item-electro">Электроинструменты</li>
                    <li class="categ-item">Ручные инструменты</li>
                    <li class="categ-item">Крепеж</li>
                    <li class="categ-item">Отделочные материалы</li>
                    <li class="categ-item">Тепловые пушки</li> -->
                </ul>
            </div>
            <div class="test">fffffff</div>

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

    /* TESTS */
    .test {
        width: 200px;
        height: 200px;
        background-color: #a5a5a5;

        display: none;
    }

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
        height: 55px;

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


    /* Блок с категориями */

    .category {
        display: flex;
        justify-content: center;
        color: #fff;

        margin-top: 10px;

        padding: 0 5px 0 5px;

        min-width: 250px;
        height: 750px;
        background-color: #ff812c;
        /* border: 2px solid #FF812C; */
        border-radius: 12px;

        transition: all 400ms;


    }

    .category ul {
        display: flex;
        flex-direction: column;

        gap: 10px;

        margin-top: 10px;
    }

    .categ-item {
        position: relative;
        width: 200px;
        cursor: pointer;
        font-size: 16px;
    }

    .categ-item:hover + .test {
        display: block;
    }

    .submenu {
        position: absolute;
        width: 200px;
        left: 200px;
        top: 0;
        background-color: #D9D9D9;
        /* border: 1px solid #000; */
        border-radius: 15px;
        padding: 10px;
        display: block;
        white-space: nowrap;
        z-index: 10000;

        color: #000;
    }

    .submenu ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }

    .submenu li {
        padding: 5px 0;
    }

    .subsubmenu {
        position: absolute;
        width: auto;
        left: 200px;
        top: 0;
        background-color: #D9D9D9;
        /* border: 1px solid #bbb; */
        border-radius: 15px;
        margin-left: 10px;
        padding: 10px;
        white-space: nowrap;
        z-index: 20000;
    }

    .subsubmenu ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }

    .subsubmenu li {
        padding: 5px 0;
    }

    a {
        text-decoration: none;
        color: black;
    }

    a:hover {
        text-decoration: underline;
    }


    /* АДАПТИВКА */

    @media (max-width: 1550px) {
        .banner {
            margin-right: 100px;
        }
    }

    @media (max-width: 1450px) {
        .left-btn {
            border-left: 2px solid #000;
            left: 0;
        }

        .right-btn {
            border-right: 2px solid #000;
            right: 0;
        }
    }

    @media (max-width: 1060px) {
        .search {
            gap: 40px;
            /* margin-right: 80px; */
        }

        .search-inp {
            width: 600px;
        }

    }

    @media (max-width: 1000px) {
        .banner img {
            width: 600px;
            height: 585px;
        }

        .banner button {
            width: 100px;
            height: 70px;
            font-size: 30px;
        }
    }

    @media (max-width: 900px) {
        .banner {
            display: none;
        }

        .category {
            width: 95%;
        }

        .category ul {
            flex-direction: row;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: start;
            height: 20px;
        }
    }


    @media (max-width: 850px) {
        .search {
            width: 95%;
        }

        .search-inp {
            width: 400px;
        }
    }

    @media (max-width: 450px) {
        .search {
            gap: 10px;
        }
    }

</style>

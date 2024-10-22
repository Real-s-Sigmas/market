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
                        {
                            name: 'Дрели',
                            subSubItems: ['Аккумуляторные дрели', 'Сетевые дрели'],
                        },
                        {
                            name: 'Перфораторы',
                            subSubItems: ['SDS+', 'SDS Max'],
                        },
                    ],
                },
                {
                    name: 'Ручные инструменты',
                    subItems: [
                        {
                            name: 'Молотки',
                            subSubItems: ['Кувалды', 'Столярные молотки'],
                        },
                        {
                            name: 'Отвертки',
                            subSubItems: ['Крестовые', 'Плоские'],
                        },
                    ],
                },
                {
                    name: 'fffffffffffffffffffff',
                    subItems: [
                        {
                            name: 'fff',
                            subSubItems: ['fff', 'ffff'],
                        },
                        {
                            name: 'ffffff',
                            subSubItems: ['fff', 'fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'],
                        },
                    ]
                },
                {
                    name: 'fffffffffffffffffffff',
                    subItems: [
                        {
                            name: 'fff',
                            subSubItems: ['fff', 'ffff'],
                        },
                        {
                            name: 'ffffff',
                            subSubItems: ['fff', 'ffffffff'],
                        },
                    ]
                },
                {
                    name: 'fffffffffffffffffffff',
                    subItems: [
                        {
                            name: 'fff',
                            subSubItems: ['fff', 'ffff'],
                        },
                        {
                            name: 'ffffff',
                            subSubItems: ['fff', 'ffffffff'],
                        },
                    ]
                },
                {
                    name: 'fffffffffffffffffffff',
                    subItems: [
                        {
                            name: 'fff',
                            subSubItems: ['fff', 'ffff'],
                        },
                        {
                            name: 'ffffff',
                            subSubItems: ['fff', 'ffffffff'],
                        },
                    ]
                },
                {
                    name: 'fffffffffffffffffffff',
                    subItems: [
                        {
                            name: 'fff',
                            subSubItems: ['fff', 'ffff'],
                        },
                        {
                            name: 'ffffff',
                            subSubItems: ['fff', 'ffffffff'],
                        },
                    ]
                },
            ],
            activeCategory: null, // Активная категория
            activeSubCategory: null, // Активная подкатегория

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

        selectCategory(index) {
            this.activeCategory = index;
            this.activeSubCategory = null; // Сбрасываем подкатегорию при выборе другой категории
        },

            // Выбор подкатегории
        selectSubCategory(subIndex) {
            this.activeSubCategory = subIndex;
        },

            // Переход к секции
        goToSection(subSubItem) {
            console.log('Переход к секции:', subSubItem);
            // Здесь можно использовать логику для якорного перехода или другой навигации
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
            <div class="category-container">

                <!-- Список категорий -->
                <ul class="categories">
                <li v-for="(category, index) in categories" :key="index">
                    <button @click="selectCategory(index)">{{ category.name }}</button>

                    <!-- Список подкатегорий -->
                    <ul class="subMenu" v-if="activeCategory === index">
                    <li v-for="(subCategory, subIndex) in category.subItems" :key="subIndex">
                        <button @click="selectSubCategory(subIndex)">{{ subCategory.name }}</button>

                        <!-- Список под-подкатегорий -->
                        <ul class="subsubUl" v-if="activeSubCategory === subIndex">
                        <li class="subsubIt" v-for="(subSubItem, subSubIndex) in subCategory.subSubItems" :key="subSubIndex">
                            <a href="#!" @click="goToSection(subSubItem)">- {{ subSubItem }}</a>
                        </li>
                        </ul>
                    </li>
                    </ul>
                </li>
                </ul>

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

        margin-right: 280px;

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
        color: #000;

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

    .category-container {
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        padding: 20px;
        width: 300px;
        background-color: #ff812c;
    }

    .categories {
        list-style-type: none;
        padding: 0;
        display: flex;
        flex-direction: column
    }

    .categories > li {
        margin-bottom: 10px;
    }

    button {
        background-color: #ff812c;
        border: none;
        padding: 10px;
        color: white;
        cursor: pointer;
        border-radius: 5px;
    }

    .subMenu {
        background-color: #e57123;
        border-top: 2px solid #fff;
        border-bottom: 2px solid #fff;
    }

    .subsubIt {
        margin-bottom: 10px;   
    }

    .subsubIt a {
        color: #000;
    }

    .subsubUl {
        background-color: #fff;
        margin: 5px 15px;
        border-radius: 4px;
        padding: 10px 0;
    }

    .subsubIt:last-child {
        margin-bottom: 0px;
    }

    .subMenu button ul {
    }

    .subMenu button {
        background-color: #e57123;
    }

    button:hover {
        background-color: #e96f1c;
    }

    

    ul {
        list-style-type: none;
    }

    a {
        text-decoration: none;
        color: #fff;
        padding: 10px;
        padding-left: 20px;
        cursor: pointer;
    }

    a:hover {
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

        .category-container {
            width: 95%;
            flex-direction: row;
        }

        .categories {
            flex-direction: row;
            flex-wrap: wrap;
        }

        

        .submenu {
            height: auto;
            width: 210px;
            left: 0;
            top: 32px;
        }

        .category ul {
            flex-direction: row;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: start;
            height: auto;
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

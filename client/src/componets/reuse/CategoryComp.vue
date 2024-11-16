<script>
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
                            subSubItems: ['fff', 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'],
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

    

    methods: {
        
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
</template>

<style scoped>
/* Блок с категориями */

    .category-container {
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        padding: 20px;
        min-width: 300px;
        background-color: #ff812c;
        margin-top: 30px;
    }

    .categories {
        list-style-type: none;
        padding: 0;
        display: flex;
        flex-direction: column
    }

    .categories > li {
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

        width: 100%;
        max-height: 30vh;
        overflow-wrap: break-word;
        word-break: break-all;
        overflow-y: hidden;
    }

    

    .subsubIt a {
        color: #000;
        padding-left: 0;
    }

    .subsubUl {
        background-color: #fff;
        margin: 5px 15px;
        border-radius: 4px;
        padding: 10px 20px;
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
    }    @media (max-width: 900px) {
        

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

        .subsubIt {
            width: 200px;
        }
    }
</style>

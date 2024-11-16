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

        <!-- Блок поиска -->
        <div class="search">
            <input type="text">
            <button class="search-find">Найти</button>
        </div>

        <!-- Блок приветствия -->
        <div class="greeting">
            <h1>Сайт интернет-магазина <br> по <span>С</span>троительству <span>и</span> <span>Р</span>емонту</h1>
            <h5>У нас вы найдете <span>большой</span> ассортимент товаров, который поможет <span>быстро</span><br> закончить ваш ремонт.</h5>
            <button>Посмотреть каталог</button>
        </div>
    </div>
</template>

<style scoped>
    /* Главное окно */
    .main-page-window {
        padding: 0 100px 0 100px;
        
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
        gap: 100px;
        
        width: 100%;
        height: 100vh;
    }

    .search {
       margin-top: 40px;
       width: 55%; 
       
       display: flex;
       justify-content: center;
       align-items: center;

       gap: 55px;

       input {
           border: 2px solid #ff812c;
           border-radius: 12px;
           width: 720px;
           height: 45px;
       }

       .search-find {
           padding: 10.5px 42px;
           border-radius: 50px;
           background-color: #ff812c;
           color: #fff;
       }
    }

    .greeting {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 64px;
        
        h1 {
            font-size: 64px;
            font-weight: 400;
            text-align: center;
            color: #2b2b2b;

            span {
                color: #ff812c;
                font-weight: 600;
            }
        }

        h5 {
            font-size: 32px;
            text-align: center;
            color: #2b2b2b;

            span {
                color: #ff812c;
                font-weight: 600;
            }
        }

        button {
            width: 715px;
            height: 75px;
            background-color: #ff812c;
            color: #fff;
            border-radius: 50px;

            font-size: 30px;
            font-weight: 600;
        }

        
    }

    @media (max-width: 1250px) {
        .search {
            width: 80%;
        }

        .greeting {
            h1 {
                font-size: 50px;
            }

            h5 {
                font-size: 24px;
            }

            button {
                width: 580px;
                height: 60px;
                font-size: 26px;
            }
        }
    }

    @media (max-width: 1000px) {
        .search {
            position: absolute;
            top: -10px;
            gap: 15px;

            input {
                width: 70%;
            }
        }

        .greeting {
            margin-top: 60px;
        }
    }

    @media (max-width: 775px) {
        .search  {
            input {
                width: 50%;
            }

            .search-find {
                padding: 8px 20px;
            }
        }

        .greeting {
            h1 {
                font-size: 34px;
            }

            h5 {
                font-size: 20px;
            }

            button {
                width: 400px;
                font-size: 20px;
            }
        }

        .main-page-window {
            padding: 0 40px;
        }
    }

    

    
    @media (max-width: 500px) {
        .greeting {
            button {
                width: 280px;
                font-size: 18px;
            }
        }
    }
    
    @media (max-width: 400px) {
        .search  {
            input {
                width: 28%;
            }
        }
    }

</style>

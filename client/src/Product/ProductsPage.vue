<script>
    export default {
        data() {
            return {
                isOpen: false,
            }
        }
    }
</script>

<template>
    <div class="main-page-window">
        <div class="search">
            <input type="text" name="" id="" class="search-inp">
            <button class="find-btn">Найти</button>
        </div>

        <div class="category-and-products">
            <div class="category" v-if="!this.isOpen">
                <ul>
                    <button @click="this.isOpen = !this.isOpen"><img src="../assets/menu.svg" alt=""></button>
                    <li class="categ-item item-electro">Электроинструменты</li>
                    <!-- <li class="categ-item"></li> -->
                    <li class="categ-item">Ручные инструменты</li>
                    <li class="categ-item">Крепеж</li>
                    <li class="categ-item">Отделочные материалы</li>
                    <li class="categ-item">Тепловые пушки</li>
                </ul>
            </div>

            <div class="category-sm" v-if="this.isOpen">
                <ul>
                    <button @click="this.isOpen = !this.isOpen"><img src="../assets/menu.svg" alt=""></button>
                    <li class="categ-item item-electro">Электроинструменты</li>
                    <!-- <li class="categ-item"></li> -->
                    <li class="categ-item">Ручные инструменты</li>
                    <li class="categ-item">Крепеж</li>
                    <li class="categ-item">Отделочные материалы</li>
                    <li class="categ-item">Тепловые пушки</li>
                </ul>
            </div>

            
            <div class="products">
                <h2>Название категории</h2>
                <div class="cards">
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>
                    <div class="prod-card">
                        <img src="../assets/shup.png" alt="">
                        <h4 class="product-name">Название</h4>
                        <button class="btn-price">Цена</button>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<style>

    .margin-products {
        margin-left: 2.90%;
    }

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
    

    .category-and-products {
        display: flex;
        align-items: center;
        /* justify-content: center; */
        gap: 60px;

        position: relative;

        width: 100%;
        height: 750px;
        /* border: 2px solid #000; */
    }

    .category {
        display: flex;
        justify-content: center;
        color: #fff;

        padding: 0 20px 0 20px;

        width: 300px;
        height: 750px;
        background-color: #FF812C;
        /* border: 2px solid #FF812C; */
        border-radius: 12px;

        transition: all 400ms;

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

    .products {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 40px;
        width: 100%;
        height: 100%;
        /* border: 3px solid #000; */
    }

    .products h2 {
        width: 100%;
        font-size: 45px;
    }

    .cards {
        width: 100%;
        height: 100%;
        /* border: 3px solid #000; */
        padding-top: 40px;
        
        display: flex;
        flex-wrap: wrap;
        gap: 40px;

        overflow-y: scroll;
    }

    .prod-card {
        width: 260px;
        height: 330px;
        /* border: 3px solid #000; */

        display: flex;
        flex-direction: column;
    }

    .prod-card img {
        width: 300px;
        height: 255px;
    }

    .product-name {
        font-size: 30px;
        color: #505050;
    }

    .btn-price {
        color: #fff;
        background-color: #FF812C;
        height: 50px;
        font-size: 30px;
        border-radius: 12px;
    }

    .category-sm {
        display: flex;
        justify-content: center;
        color: #fff;

        position: absolute;
        z-index: 52;

        padding: 10px 20px 0 20px;

        width: 170px;
        height: 750px;
        background-color: #FF812C;
        /* border: 2px solid #FF812C; */
        border-radius: 0 12px 12px 0;
        margin-left: -50px;

        transition: all 400ms;
    }

    @media (min-width: 800px) {
        .category button {
            display: none;
        }
    }

    @media (max-width: 800px) {
        .category li {
            display: none;
        }

        .category {
            margin-left: -50px;
            padding: 0;
            width: 50px;
            border-radius: 0 15px 15px 0;

            transition: all 400ms;
            
        }

        .cards {
            gap: 20px;
        }
        
        .category-and-products {
            gap: 20px;
        }

        .prod-card {
            width: 250px;
            height: 300px;
        }

        .prod-card img {
            width: 250px;
            height: 300px;
        }

        .product-name {
            font-size: 20px;
        }

        .btn-price {
            height: 30px;
            font-size: 20px;
        }
    }

</style>
<script>
    export default {
        data() {
            return {
                product_count: 1,
                isFav: false,
                text: '',
                symb_count: 0, // Количество символов в комментарии
                red_text: false,

                rating: null, // Столько звезд, сколько выбрал пользователь 
                mouseOverRating: null, // Показывает, на сколко звезд наводит пользователь
            }
        },

        methods: {

            // Увеличивает счетчик количества товаров на 1
            plus() {
                if (this.product_count <= 10000) {
                    this.product_count++;
                } else {
                    return;
                }
            },

            // Уменьшает счетчик количества товаров на 1
            minus() {
                if (this.product_count > 1) {
                    this.product_count--;
                } else {
                    return;
                }
            },

            // Проверяет, чтобы счетчик не заходил за 10001 и не уходил дальше 1
            checkCount() {
                if (this.product_count > 10000) {
                    this.product_count = 10000;
                } else if (this.product_count < 1) {
                    this.product_count = 1;
                }
            },

            // Отображаем выбранную оценку

            showCurrentRating(rating) {
                this.mouseOverRating = rating === 0 ? null : rating;
            },

            // Ставит выбранную оценку
            setCurrentSelectedRating(rating) {
                this.rating = rating;
                this.mouseOverRating = null;
            },

            symbCount() {
                this.symb_count = this.text.length;

                if (this.symb_count >= 2000) {
                    this.red_text = true;
                } else {
                    this.red_text = false;
                }
            }
        },
        
        computed: {
        }
    }
</script>

<template>
    <!-- Главное окно -->
    <div class="main-page-window">
        
        <!-- Блок с информацией о товара (с картинкой) -->
        <div class="product-info">
            <img class="prod-img"src="../assets/shup.png" alt="">

            <!-- Бллок с информацией о товаре -->
            <div class="main-info">
                <h3>Название товара</h3>

                <!-- Блок с коротким описанием товара -->
                <p class="short-description">
                    <span>Описание: </span>Очень хороший аппарат, всем советую
                    прям вообще во такой.ааааааааа аааааааа аааааааа
                    аааааааа аааааааарааааа ааааааааааааа аааааабааааа
                </p>
                <a class="anc-link" href="#full-desc">Подробное описание</a>
                <div class="star-price-sum-order-fav">
                    <div class="star-price">

                        <!-- Блок с оценкой -->
                        <p class="star">Оценка: 
                                    <img src="../assets/star-full.svg" alt="">
                                    <img src="../assets/star-full.svg" alt="">
                                    <img src="../assets/star-full.svg" alt="">
                                    <img src="../assets/star-full.svg" alt="">
                                    <img src="../assets/star-empty.svg" alt="">
                        </p>

                        <!-- Блок с ценой -->
                        <div class="price">
                            <p>Цена: <span>8 800</span> р</p>
                        </div>
                    </div>

                    <div class="sum-order-fav">
                    
                        <!-- Блок с выбором количества товаров -->
                        <div class="sum">
                            <p>Количество: </p>
                            <div class="buts-count">
                                <button @click="plus" class="plus-btn"><img src="../assets/Plus.svg" alt=""></button>
                                <!-- input проверяет, чтобы в поле вводились только числа -->
                                <input @input="checkCount" v-model="product_count" class="count"  onkeyup="this.value = this.value.replace(/[^\d]/g,'');">
                                <button @click="minus" class="minus-btn"><img src="../assets/minus.svg" alt=""></button>
                            </div>
                        </div>

                        <div class="order-fav">

                            <!-- Блок с кнопкой заказть -->
                            <div class="order">
                                <button>Заказать</button>
                            </div>

                            <!-- Блок с кнопкой "В избранное" -->
                            <div class="fav" :class="{'favDone': this.isFav}">
                                <button  @click="this.isFav = !this.isFav"> 
                                    <svg  width="40px" height="40px" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" clip-rule="evenodd" d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z" stroke="#ff812c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Блок с полным описанием -->
        <div class="full-description" id="full-desc">
            <p><span>Полное описание товара: </span>Аппарат Шуруповерт сверлило 3000 ультра мега про макс, 
                это не только ваша уверенность в том, что вы самодостаточный, гордый мужчина, это еще 
                и проход (как метро люблино) в трусики любой уважающей себя даме. Как говориться мужчина 
                рожден с дрелью в руках. Покажи всем свое величие. Жена ругается, что руки у тебя кривее 
                чем волосы на жопе, а поправить ты можешь только свой вес и то в большую 
                сторону? У нас есть для тебя решение: 
                Шуруповерт сверлило 3000 ультра мега про макс.
                Купи этот крутейший аппарат и отдолби ее до потери сознания, докажи кто в доме маТчо!
                    
            </p>
        </div>

        <!-- Блок с отзывами -->
        <div class="feedback-cont">
            <div class="your-comment">
                <h2>Оставить отзыв:</h2>
                <div class="your-text">
                    <!-- Поле для ввода текста -->
                    <textarea @input="symbCount"  v-model="this.text" class="text-comm" maxlength="2000"></textarea>
    
                    <!-- Выбор оценки -->
                    <div class="rate"><p>Оценка: </p>
                        <span v-for="n in 5" :key="n"
                            :class="['star', { filled: n <= (mouseOverRating || rating), empty: n > ( mouseOverRating || rating) }]"
                            @mouseover="showCurrentRating(n)"
                            @mouseleave="showCurrentRating(0)"
                            @click="setCurrentSelectedRating(n)">
                            
                                <img src="../assets/star-empty.svg" alt="">
                        
                        </span>
                    </div>

                    <!-- Счетчик символов -->
                    <p class="symbols-count" :class="{'red_text': this.red_text}">{{ this.symb_count }}/2000</p>
                </div>

                <!-- Кнопка "Добавить (отзыв)" -->
                <button class="send-comm">Отправить</button>
            </div>

            <!-- Другие отзывы -->
            <div class="other-comments">
                <div class="title-sort">
                    <h2>Другие отзывы:</h2>
                    <div class="sort">
                        <select name="" id="">
                            <option value="">Сортировать</option>
                            <option value="top-rate">С наибольшей оценкой</option>
                            <option value="low-rate">С наименьшей оценкой</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>

/* Тесты */


/* Служебное */

.count::-webkit-outer-spin-button,
.count::-webkit-inner-spin-button {
    /* display: none; <- Crashes Chrome on hover */
    -webkit-appearance: none;
    margin: 0; /* <-- Apparently some margin are still there even though it's hidden */
}

/* Блок с информацией о товаре */

.main-page-window {
    width: 100%;
    height: auto;
    margin: 0;
    user-select: text;
    padding: 0 20px 0 20px;

    overflow-x: hidden;    
}

.product-info {
    display: flex;
    margin-top: 30px;
    gap: 40px;

    width: 100%;
    height: 550px;
    
    border-bottom: 2px solid #000;
}

.prod-img {
    width: 460px;
    height: 460px;
}

.main-info {
    display: flex;
    flex-direction: column;
    gap: 40px;
    
    width: 100%;
    padding-right: 40px;

    
}

.main-info h3 {
    font-size: 35px;
    font-weight: 700;
}

.short-description {
    font-size: 30px;
    width: 1100px;
}

.short-description span {
    font-weight: 700;
}

.anc-link {
    width: 350px;
    font-size: 30px;
    font-weight: 700;
    color: #FF812C;

    transition: all 100ms;
}

.anc-link:hover {
    color: #dd732d;
}

.anc-link:active {
    color: #b65e23;
}




/* Четыре блока в одном */

.star-price-sum-order-fav {
    display: flex;
    justify-content: space-between;

    width: 100%;
    height: 150px;
    
    margin-top: -25px;
    
    /* border: 2px solid #000; */
}

/* Оценка и цена */

.star-price {
    display: flex;
    flex-direction: column;
    gap: 25px;

    width: 300px;
    height: 140px;
}

.star {
    display: flex;
    align-items: center;
    gap: 6px;

    font-size: 30px;
    font-weight: 700;

    user-select: none;
}

.price {
    display: flex;
    justify-content: center;
    align-items: center;

    font-size: 30px;

    width: 300px;
    height: 60px;

    border: 2px solid #000;
    border-radius: 12px;
}


/* Счетчик, кнопка заказать и избранные */

.sum-order-fav {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    
    width: 450px;
    height: 150px;
    /* border: 2px solid #000; */
}



/* Счетчик количества товаров */

.sum {
    width: 100%;
    height: 140px;
    /* border: 2px solid #000; */

    user-select: none;
}

.sum {
    display: flex;
    /* align-items: center; */
    justify-content: center;
    gap: 22px;

    bottom: 140px;
    right: -130px;
}

.sum p {
    font-size: 24px;
}

.buts-count {
    display: flex;
    justify-content: space-between;
    align-items: center;


    width: 175px;
    height: 40px;

    border-radius: 12px;
}

.buts-count button {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 45px;
    height: 40px;
    border: 2px solid #000;
    background-color: #d9d9d9;
    font-size: 24px;

    transition: all 100ms;
}

.buts-count button:hover {
    background-color: #afafaf;
}

.buts-count button:active {
    background-color: #959595;
}

.buts-count .plus-btn {
    border-radius: 12px 0 0 12px;
}

.buts-count .minus-btn {
    border-radius: 0 12px 12px 0;
}

.buts-count .count {
    text-align: center;
    font-size: 24px;
    width: 85px;
    height: 40px;
    border-top: 2px solid #000;
    border-bottom: 2px solid #000;
}



/* Кнопка заказать и избранное */

.order-fav {
    display: flex;
    justify-content: space-around;

    width: 100%;
    height: 140px;
    /* border: 2px solid #000; */
}



/* Кнопка заказать */

.order button {
    width: 260px;
    height: 80px;
    background-color: #FF812C;
    border-radius: 12px;
    color: #fff;
    font-size: 30px;
    font-weight: 700;

    user-select: none;

    transition: all 100ms;
}

.order button:hover {
    background-color: #dd732d;;
}

.order button:active {
    background-color: #b65e23;;;
}



/* Кнопка "Добавить в избранное" */

.fav {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 80px;
    height: 80px;

    border: 2px solid #505050;
    border-radius: 12px;

    transition: all 100ms;

    user-select: none;
}

.fav button {
    display: flex;
    justify-content: center;
    align-items: center;
    
    width: 80px;
    height: 80px;
}

.fav:hover {
    background-color: #FF812C;
}

.fav:active {
    background-color: #b65e23;
}


.favDone {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 80px;
    height: 80px;

    background-color: #FF812C;
    border-radius: 12px;

    transition: all 100ms;

    user-select: none;
}







/* Блок с полным описанием о товаре */

.full-description {
    margin-top: 60px;
    padding: 0 30px 60px 30px;
    width: 100%;
    height: auto;
    border-bottom: 2px solid #000;
}

.full-description {
    font-size: 30px;
}

.full-description span {
    font-weight: 700;
}







/* Блок с отзывами */

.feedback-cont {
    display: flex;
    flex-direction: column;

    margin-top: 50px;
    padding: 0 30px 60px 30px;

    width: 100%;
    height: 2000px;  /* Изменить на auto*/ 
}

.feedback-cont h2 {
    font-size: 35px;
    font-weight: 700;
}

.your-comment {
    display: flex;
    flex-direction: column;
    gap: 20px;

    margin-bottom: 70px;
}

.your-text {
    width: 100%;
    position: relative;
    border: 2px solid #000;
    border-radius: 12px;
    height: 260px;
}

.text-comm {
    width: 100%;
    height: 210px;


    font-size: 24px;

    border-radius: 12px;
    padding: 10px 10px 10px 10px;

    resize: none;

}

.text-comm:focus {
    outline: none;
}   

.rate {
    display: flex;
    align-items: center;

    position: absolute;
    bottom: 5px;
    left: 10px;

    gap: 6px;

    font-size: 30px;
    font-weight: 700;

    user-select: none;

}

.symbols-count {
    position: absolute;

    font-size: 24px;
    color: #959595;
    bottom: 10px;
    right: 10px;
}

.red_text {
    color: #cb0404;
}



/* Окрашивание звезд при выборе оценки */

.star {
    cursor: pointer;
}

.filled {
    background: url('../assets/star-full.svg') no-repeat;
}

.empty {
    background: url('../assets/star-empty.svg') no-repeat;
}



/* Кнопка "Отправить (отзыв)" */

.send-comm {
    width: 270px;
    height: 75px;
    background-color: #FF812C;

    font-size: 30px;
    color: #fff;

    border-radius: 12px;
    transition: all 100ms;
    
    user-select: none;
}

.send-comm:hover {
    background-color: #dd732d;
}

.send-comm:active {
    background-color: #b65e23;
}




/* Другие отзывы */

.other-comments {
    width: 100%;
    height: 500px;
    border: 1px solid #000;
}

.title-sort {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.sort select {
    font-size: 28px;

    color: #fff;
    background-color: #262626;
    border: 1px solid #000; 
    border-radius: 12px;
    width: auto;
    height: 50px;
    padding: 2px 10px 2px 10px;
}

</style>
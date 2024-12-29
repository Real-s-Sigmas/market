<script>
export default {
    data() {
        return {

        }
    }
}
</script>

<template>
    <div class="footer">
        <div class="block block-1">
            <h3>С.и.Р - Строительство и Ремонт</h3>

            <p><span>Наш адрес:</span> Московская область, <br> городской округ Красногорск, <br>Новорижское шоссе, 26-й километр, строение 6, 
павильон Б7</p>

            <p><span>Телефон для связи:</span> <br> +7 (925) 537-12-13</p>
            <p><span>Телефон для связи по вопросам работы сайта:</span> <br> +7 (925) 537-12-13</p>
        </div>
        <div class="block block-2">
            <h3>Ссылки для навигации:</h3>
            <p><a href="/">Главная</a></p>
            <p><a href="/Catalog">Каталог</a></p>
            <p><a href="/basket">Корзина</a></p>
            <p><a href="/favorites">Избранные</a></p>
            <p><a href="/AboutUs">О нас</a></p>
        </div>
        <div class="block block-3">
            <h3>Прочее:</h3>
            <p><span>Наши часы работы: </span> <br> Пн - Сб: 08:00 - 20:00 <br> Вс: 09:00 - 18:00</p>
            <p><span>Мы принимаем оплату: </span> <br> Картой <br> Наличными <br> Переводом</p>
        </div>
    </div>
</template>

<style scoped>
    
    a {
        text-decoration: underline;
    }

    .footer {
        display: grid;
        grid-template-columns: auto auto auto;

        
        margin-top: 20px;

        padding: 20px;
        width: 100%;
        height: auto;
        background-color: #252525;
    }

    .block {
        

        h3 {
            color: #fff;
            font-size: 22px;
            font-weight: 600;

            margin-bottom: 10px;
        }
        
        span {
            color: #fff;
            font-weight: 600;
        }

        p {
            color: #d1d1d1;
            margin-bottom: 10px;
        }
    }

    @media (max-width: 1020px) {
        .footer {
            grid-template-columns: auto auto;
        }

        .block-3 {
            margin-top: 30px;
        }
    }

    @media (max-width: 790px) {
        .block {
            p {
                font-size: 14px;
            }
        }
    }

    @media (max-width: 715px) {
        .footer {
            grid-template-columns: auto;
        }

        .block-2 {
            margin-top: 30px;
        }
    }
    
</style>

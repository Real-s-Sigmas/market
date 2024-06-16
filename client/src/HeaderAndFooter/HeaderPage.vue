<script>
export default {
    data() {
        return {

        }
    }
}
</script>

<template>
    <div class="header">
        <div class="div-ob logo-title">
            <div class="logo"></div>
            <p class="title">Строительство и Ремонт</p>
        </div>
        <ul>
            <li class="header-link"><a href="#!">Главная</a></li>
            <li class="header-link"><a href="#!">О нас</a></li>
        </ul>
        <div class="div-ob fav-acc">
            <a href="#!">
                <svg class="favorite" width="25px" height="25px" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>

            <button class="acc">Войти</button>
        </div>
    </div>
</template>

<style>
    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;

        width: 100%;
        height: 80px;
        border-bottom: 2px solid #000;

        padding: 0 20px 0 20px;
    }

    .header ul {
        /* margin-left: 450px; */
        display: flex;
        gap: 100px;
    }

    .title {
        margin-left: 20px;
    }

    .logo {
        width: 40px;
        height: 40px;

        border: 2px solid #000;
        border-radius: 50px
    }

    .acc {
        width: 100px;
        height: 35px;
        border-radius: 12px;
        border: 2px solid #FF812C;

        transition: all 100ms;
    }

    .acc:hover {
        background-color: #FF812C;
        color: #fff;
    }

    .acc:active {
        background-color: #d95700;
        border-color: #d95700;
    }

    .fav-acc a {
        margin-right: 20px;
    }

    .fav-acc svg {
        transition: all 100ms;
    }

    .fav-acc svg:hover {
        fill: #FF812C;
    }

    .fav-acc svg:active {
        fill: #d95700;
    }

    
    .div-ob {
        display: flex;
        align-items: center;
    }

</style>
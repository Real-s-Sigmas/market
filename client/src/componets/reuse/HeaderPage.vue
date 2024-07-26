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
    <div class="header" :class="{'open': this.isOpen}">
        <div class="div-ob logo-title">
            <img src="../../assets/icons/logo.svg" width="50" alt="">
            <p class="title">Строительство и Ремонт</p>
        </div>
        <div class="links">

            <button class="link-btn"><a class="header-link" href="#!">Главная</a></button>
            <button class="link-btn"><a class="header-link" href="#!">О нас</a></button>
        </div>
        <div class="div-ob fav-acc">
            <a href="#!">
                <svg class="favorite" width="35px" height="35px" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>

            <button class="acc">Войти</button>
        </div>
    </div>
    <div class="btn-top">
        <button @click="this.isOpen = !this.isOpen"><img src="../../assets/menu.svg" alt=""></button>
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

        transition: all 300ms;

    }

    .links {
        /* margin-left: 450px; */
        display: flex;
        gap: 300px;
    }
    
    .link-btn {
        width: 160px;
        height: 50px;

        border-radius: 12px;

        transition: all 100ms;
    }

    .link-btn a {
        font-size: 22px;
    }

    .link-btn:hover {
        background-color: #262626;
        color: #fff;
    }

    .link-btn:active {
        background-color: #191919
    }

    .btn-top {
        display: flex;
        justify-content: end;
        padding-right: 20px;
    }

    .title {
        font-weight: 700;
        margin-left: 20px;
        font-size: 25px;
    }

    .logo {
        width: 40px;
        height: 40px;

        border: 2px solid #000;
        border-radius: 50px
    }

    .acc {
        width: 160px;
        height: 50px;
        border-radius: 12px;
        border: 2px solid #FF812C;

        font-size: 22px;

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
        margin-right: 40px;
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

    .open {
        margin-top: 0px !important;
    }

    
    @media (min-width: 800px) {
        .btn-top {
            display: none;
        }
    }
    
    @media (max-width: 1230px) {
        .links {
            gap: 30px;
        }
    }

    @media (max-width: 900px) {
        .links {
            gap: 10px;
        }
    }

    @media (max-width: 950px) {
        .header ul {
            gap: 40px;
        }

        .fav-acc a {
            margin-right: 10px;
        }
    }

    @media (max-width: 830px) {
        .header ul {
            gap: 25px;
        }
    }

    @media (max-width: 800px) {
        .header {
            margin-top: -260px;
            flex-direction: column;
            align-items: start;
            height: 200px;
            gap: 10px;
            border-bottom: none;

            transition: all 300ms;
            
            /* padding-bottom: 50px; */
            /* background-color: #FF812C; */
        }

        .links {
            flex-direction: column;
            gap: 15px;
        }

        .link-btn {
            width: 100px;
            text-align: start;
            padding: 0 5px 0 5px;
        }

        .btn-top {
            margin-top: 75px;
        }

        .btn-top button {
            background-color: #191919;
            padding: 5px;
            border-radius: 12px;
        }
    }

    /* @media (max-width: 700px) {
        .header ul {
            gap: 20px;
        }
    } */
</style>
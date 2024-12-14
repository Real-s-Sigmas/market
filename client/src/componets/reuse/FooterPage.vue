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

            <p><span>Наш адрес:</span> Московская область, <br> городской округ Красногорск, <br>Новорижское шоссе, 26-й километр, с6
павильон Б7</p>

            <p><span>Телефон для связи:</span> +7 (925) 537-12-13</p>
            <p><span>Телефон для связи по вопросам работы сайта:</span> +7 (925) 537-12-13</p>
        </div>
        <div class="block block-2">
            block2
        </div>
        <div class="block block-3">
            block3
        </div>
    </div>
</template>

<style scoped>
    .footer {
        display: grid;
        grid-template-columns: auto auto auto;

        
        margin-top: 20px;

        padding: 20px;
        width: 100%;
        height: 300px;
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

    
</style>

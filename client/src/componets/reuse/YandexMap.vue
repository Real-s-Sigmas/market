<script>
export default {
    name: 'YandexMap',
    props: {
        center: {
            type: Array,
            default: () => [ 55.784428, 37.236963 ]
        },
        zoom: {
            type: Number,
            default: 10,
        },
    },

    mounted() {
        this.initMap();
    },

    methods: {
        initMap() {
            ymaps.ready(() => {
                this.map = new ymaps.Map(this.$refs.yandexMap, {
                    center: this.center,
                    zoom: this.zoom,
                });

                const placemark = new ymaps.Placemark(this.center, {
                    balloonContent: "Здесь ваша точка",
                });

                this.map.geoObjects.add(placemark);
            })
        }
    }
}
</script>

<template>
   <div ref="yandexMap" style="width: 100%; height: 600px;"></div> 
</template>

<style>

</style>

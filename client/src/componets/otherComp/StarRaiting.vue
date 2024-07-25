<script>
    export default {
        data() {
            return {
                rating: null,
                mouseOverRating: null,
            }
        },

        methods: {
            // Отображаем выбранную оценку

            showCurrentRating(rating) {
                this.mouseOverRating = rating === 0 ? null : rating;
            },

            // Ставит выбранную оценку
            setCurrentSelectedRating(rating) {
                this.rating = rating;
                this.mouseOverRating = null;
            }
        },
    }
</script>

<template>
    <div class="rate"><p>Оценка: </p>
        <span v-for="n in 5" :key="n"
            :class="['star', { filled: n <= (mouseOverRating || rating), empty: n > ( mouseOverRating || rating) }]"
            @mouseover="showCurrentRating(n)"
            @mouseleave="showCurrentRating(0)"
            @click="setCurrentSelectedRating(n)">
            
                <img src="../../assets/star-empty.svg" alt="">
        
        </span>
    </div>
</template>

<style scoped>

.star {
    cursor: pointer;
}

.filled {
    background: url('../../assets/star-full.svg') no-repeat;
}
.empty {
    background: url('../../assets/star-empty.svg') no-repeat;
}
</style>
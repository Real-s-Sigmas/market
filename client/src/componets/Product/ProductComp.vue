<script>
export default {
  data() {
    return {
      products: [ // потом убрать
				{
					id: 52,
					title: "Название товара",
					images: ['src/assets/shup.png'],
					short_description: "Очень хороший аппарат, всем советую прям вообще во такой.ааааааааа аааааааа аааааааа fffffffff  fffffffff",
					price: "8 800",
					full_desctiption: "Аппарат Шуруповерт сверлило 3000 ультра мега про макс, это не только ваша уверенность в том, что вы самодостаточный, гордый мужчина, это еще и проход (как метро люблино) в трусики любой уважающей себя даме. Как говориться мужчина рожден с дрелью в руках. Покажи всем свое величие. Жена ругается, что руки у тебя кривее чем волосы на жопе, а поправить ты можешь только свой вес и то в большую сторону? У нас есть для тебя решение: Шуруповерт сверлило 3000 ультра мега про макс. Купи этот крутейший аппарат и отдолби ее до потери сознания, докажи кто в доме маТчо!",
					rating_product: 5,
				},
      ]
    }
  },
  components: {
    
    },
    props: {
    
  }
};
</script>
<template>
  
  <div class="card-container flex xl:flex-row justify-center gap-6 mt-6 flex-wrap">
		<div class="card rounded-2xl transition-all duration-300 hover:-translate-y-5 cursor-pointer" v-for='product in products' @click='this.$router.push(`/Product/${product.id}`)'>
			<img class='rounded-t-2xl' :src="product.images[0]" :alt="product.title">
			<div class="info-block p-6 flex flex-col">
				<h3 class='text-2xl font-bold'>{{ product.title }}</h3>
				<p class='text-slate-500 short-desc'>{{ product.short_description}}...</p>
				<span>Рейтинг: {{ product.rating_product }} звёзд</span>
				<b>{{ product.price }} р.</b>
			</div>
		</div>
	</div>
	
</template>
<style scoped>

.card {
	border: 2px solid #ff812c;
	width: 300px;

	img {
		width: 100%;
		object-fit: cover;
		max-height: 250px;
	}

	h3 {
		color: #ff812c;
	}

	b {
		font-size: 20px;
	}

	.short-desc {
	  display: -webkit-box; /* Создает контейнер flex */
    -webkit-box-orient: vertical;
	  overflow: hidden;
	  text-overflow: ellipsis;
	  line-height: 1.5;
	  max-height: calc(1.5em * 3);
	}
}



@media (max-width: 1010px) {
  .card {
    width: 250px;
  }
}


@media (max-width: 800px) {
  
}

@media (max-width: 650px) {
  

}

@media (max-width: 580px) {
  .card {
    width: 230px;
  }
}

@media (max-width: 555px) {
  .card {
    width: 160px;

    h3 {
      font-size: 20px;
    }
  }
}

@media (max-width: 530px) {
  
}
</style>

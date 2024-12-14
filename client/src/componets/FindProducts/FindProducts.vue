<script>
import axios from 'axios';

export default {
	data() {
		return {
			search: ``,
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
			],
			error: ``,
		}
	},

	methods: {
		getSearch() {
			this.search = this.$route.query.search;
		},

		async loadProduct() {
			if(this.search) {
				try {
					let res = await axios.get('/items/one-item', {
						params: {
							search: this.search
						}
					});
	
					this.products = res.data.res;
	
					if(res.data.res.length == 0) {
						this.error = 'Таких товаров нет';
					} else {
						this.error = '';
					}
	
				} catch (error) {
					console.log(error);
					this.error = 'Невозможно найти товары';
				}
	
				this.$router.replace({ path: '/FindProducts', query: {search: this.search} });
			} else {
				this.error = 'Напишите название товара';
			}
		}
	},

	mounted() {
		this.getSearch();
		this.loadProduct();
	}
}
</script>

<template>
	<div class="flex flex-col md:mx-16 mx-6 mt-8">
		<div class="search">
				<input type="text" v-model='search' placeholder='Поиск товаров'>
				<button class="search-find" @click='loadProduct'>Найти</button>
		</div>

		<h2 v-if='this.error' class='mt-6 flex justify-center text-red-500 text-xl font-bold'>{{ error }}</h2>

		<div class="card-container flex xl:flex-row justify-center gap-6 mt-6 flex-wrap">
			<div class="card rounded-2xl transition-all duration-300 hover:-translate-y-5 cursor-pointer" v-for='product in products' @click='this.$router.push(`/Product/${product.id}`)'>
				<img class='rounded-t-2xl' :src="product.images[0]" :alt="product.title">
				<div class="info-block p-6 flex flex-col">
					<h3 class='text-2xl font-bold'>{{ product.title }}</h3>
					<p class='text-slate-500'>{{ product.short_description.substring(0, 50) }}...</p>
					<span>Рейтинг: {{ product.rating_product }} звёзд</span>
					<b>{{ product.price }} р.</b>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
.card {
	border: 2px solid #ff812c;
	width: 18%;

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
}

.search {
       margin: 20px 0;
       /* width: 100%;  */
       
       display: flex;
       justify-content: center;
       align-items: center;

       gap: 18px;

       input {
           border: 2px solid #ff812c;
           border-radius: 12px;
           width: 720px;
           height: 45px;
           padding: 0 10px;
       }

       .search-find {
           padding: 10.5px 42px;
           border-radius: 50px;
           background-color: #ff812c;
           color: #fff;

           transition: all 100ms;
       }

       .search-find:hover {
            background-color: #d95700;
       }
    }

@media (max-width: 500px) {
	.search  {
		input {
				width: 100%;
		}
		.search-find {
				padding: 10.5px 20px;
		}
	}

	.card {
		width: 100% !important;
	}
}

@media (max-width: 1030px) {
	.search {
			gap: 20px;
	}
	.card {
		width: 45%;
	}
}
</style>
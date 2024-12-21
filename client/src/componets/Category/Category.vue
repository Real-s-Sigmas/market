<script>
export default {
	data() {
		return {
			rusParametr: ``,
			error: ``,
			products: [ 
				
			],
		}
	},

	methods: {
		async loadProduct() {
			if(this.secondParametr) {
				try {
					let res = await axios.get('/items/show-items', {
						params: {
							topic: this.$route.params.rusParametr
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
			} else {
				this.error = 'Неправильная категория товаров';
			}
		}
	},

	mounted() {
		this.loadProduct();
	}
}
</script>


<template>

	<div class="flex flex-col md:mx-16 mx-6 mt-8">
		<h3 class='text-slate-500 text-2xl'>{{ this.$route.params.rusParametr }}</h3>
		<h2 v-if='this.error' class='mt-6 flex justify-center text-red-500 text-xl font-bold'>{{ error }}</h2>
		<div class="card-container flex xl:flex-row justify-center gap-6 mt-6 flex-wrap">
			<div class="card rounded-2xl transition-all duration-300 hover:-translate-y-5 cursor-pointer"
				v-for='product in products' @click='this.$router.push(`/Product/${product.id}`)' :key="product.title">
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

@media (max-width: 500px) {
	.card {
		width: 100% !important;
	}
}

@media (max-width: 1030px) {
	.card {
		width: 45%;
	}
}
</style>

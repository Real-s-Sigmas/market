<script>
export default {
  data() {
    return {

    };
  },
  components: {
    
    },
    props: {
    
  }
};
</script>
<template>
  <div class="prod-card">
    <img src="../../assets/shup.png" alt="" />
    <h4 class="product-name">Дрель Перфоратор</h4>
    <button class="btn-price">500p</button>
  </div>
</template>
<style scoped>
.prod-card {
  width: 260px;
  height: 330px;
  /* border: 3px solid #000; */
  cursor: pointer;
  display: flex;
  flex-direction: column;
}

.prod-card img {
  width: 300px;
  height: 255px;
}

.product-name {
  font-size: 27px;
  font-weight: 450;
  color: #505050;
}

.btn-price {
  color: #fff;
  background-color: #ff812c;
  height: 50px;
  font-size: 30px;
  border-radius: 12px;
}
@media (max-width: 800px) {
  .prod-card {
    width: 250px;
    height: 300px;
  }

  .prod-card img {
    width: 250px;
    height: 300px;
  }

  .product-name {
    font-size: 20px;
  }

  .btn-price {
    height: 30px;
    font-size: 20px;
  }
}

@media (max-width: 650px) {
  .prod-card {
    width: 190px;
    height: 260px;
  }

  .prod-card img {
    width: 190px;
    height: 280px;
  }
}

@media (max-width: 530px) {
  .prod-card {
    width: 160px;
    height: 220px;
  }
}
</style>

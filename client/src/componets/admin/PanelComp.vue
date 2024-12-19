<script>
  
</script>

<template>
  <div class="window">
    <div class="tabs">
      <button @click="this.$router.push('/AdminPanel/actions')">
        Действия
      </button>
      <button @click="this.$router.push('/AdminPanel/orders')">
        Заказы
      </button>
    </div>
    <div class="actions-block">
      <div class="add-product">
        <a href="/addproduct"><button ><img src="../../assets/Plus.svg" alt=""></button></a>
        <h3>Добавить товар</h3>
      </div>
      <div class="add-category">
        <!-- Место для возможности добавления товара -->
      </div>
    </div>
  </div>
</template>

<style scoped>
.window {
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
  
  .tabs {
    display: flex;
    justify-content: center;
    gap: 80px;

    button {
      color: #fff;
      background-color: #ff813c;
      width: 250px;
      height: 45px;
      border-radius: 50px;

      font-size: 20px;
      font-weight: 500;

      transition: all 100ms;
    }

    button:hover {
      background-color: #d95700;
    }
  }

  .actions-block {
    display: flex;
    width: 90%;

    .add-product {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 5px;
      
      button {
        width: 230px;
        height: 230px;
        border: 1px solid #ff813c;
        border-radius: 18px;

        display: grid;
        place-items: center;  
      }

      h3 {
        font-size: 22px;
        font-weight: 500;
      }
      
    }
  }
}

    @media (max-width: 625px) {
      .tabs {
        gap: 10px !important;

        button {
          width: 200px !important;
          font-size: 16px !important;
        }
      }
    }

    @media (max-width: 420px) {
      .tabs {
        button {
          width: 150px !important;
        }
      }
    }
</style>


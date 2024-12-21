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
  <div class="orderNumber">
    <p>№ 000001  / 19.12.2024</p>
  </div>
  <div class="orders">
    <div class="card">
      <div class="image-info">
        <div class="image">
          <img src="../../assets/shup.png" alt="">
        </div>
        <div class="info">
          <div class="code-count">
            <p>Код товара: 209181</p>
            <p>Количество: 1шт</p>  
          </div>
          
          <div class="title-desc">
            <h2>Шуруповерт “Сверлило 3000 ультра вибратор  298 в 1”</h2>
            <h4>Описание: Если вам сказали, что вы не мужик,  докажи всем обратное и купи эту херь</h4>  
          </div>
          
          <p class="price">Цена: 5 000 000 р</p>
        </div>  
      </div>
      
      <div class="btns">
        <button>К товару</button>
      </div>
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

  padding: 0 100px;

  
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

  .orderNumber {
    width: 100%;

    p {
      font-size: 20px;
    }
  }

  .orders {
    width: 100%;
    height: 1000px;
    

    .card {
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 200ms;
      padding: 20px;
      border-radius: 20px;

      h2, h4 {
        font-size: 18px;

        display: inline-block;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        width: 50ch;
      }


      .btns {
        button {
          color: #fff;
          background-color: #ff813c;
          font-size: 20px;
          font-weight: 500;
          width: 200px;
          height: 50px;
          border-radius: 8px;
        }
      }

      .image-info {
        display: flex;
        align-items: center;
        gap: 30px;
        
        img {
          min-width: 250px;
          height: 250px;
          border-radius: 12px;
          -webkit-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
          -moz-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
          box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
        }

        .info {
          display: flex;
          flex-direction: column;
          height: 250px;
          justify-content: space-between;

          .code-count {
            p {
              margin-bottom: 10px;
            }
          }

          .price {
            text-align: center;
            border: 1px solid #000;
            border-radius: 6px;
            padding: 5px 0;
            font-weight: 500;
            width: 200px;
          }
        }
      }

      
    }
    .card:hover {
      transform: translateY(-10px);
      -webkit-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
      -moz-box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
      box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);
      
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

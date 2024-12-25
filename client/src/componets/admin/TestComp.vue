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
  <div class="orderNumber" >
    <p>№  123456 / 13.12.2010</p>
  </div>
  <div class="orders" >
    <div class="card">
      <div class="image-info">
        <div class="image">
          <img src="../../assets/shup.png" alt="">
        </div>
        <div class="info">
          <div class="code-count">
            <p>Код товара: <b>123456</b></p>
            <p>Количество: 10шт</p>  
          </div>
          
          <div class="title-desc">
            <h2><b>Шуруповерт RT-20</b></h2>
            <h4>Описание: Обалденная штука, надо брать, по любому, 100 проц, куплю прям завтра</h4>  
          </div>
          
          <p class="price">Цена: 10000 р</p>
        </div>  
      </div>
      
      <div class="btns">
        <button @click='this.$router.push(`/Product/${order.idProduct}`)'>К товару</button>
      </div>
    </div>
  </div>
  <h2  class='text-red-500 font-bold text-2xl flex justify-center'>{{ error }}</h2>
</div>
</template>

<style>
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
      transition: all 200ms;
      padding: 20px;
      border-radius: 20px;

      h2, h4 {
           display: -webkit-box !important; 
          -webkit-line-clamp: 2 !important; 
          -webkit-box-orient: vertical !important; 
          overflow: hidden !important; 
          text-overflow: ellipsis !important;
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
        width: 90%;
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


@media (max-width: 1355px) {
  .window {
    padding: 30px;
  } 
}

@media (max-width: 830px) {
  .window {
    padding: 5px;
  }

  .card {
    padding: 20px 5px !important;
  }
}

@media (max-width: 830px) {
  .card {
    flex-direction: column;

    .btns {
      padding-top: 20px;
    }

    .btns button {
      width: 360px !important;
    }
  }
}

@media (max-width: 670px) {
  .image-info {
    flex-direction: column;
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

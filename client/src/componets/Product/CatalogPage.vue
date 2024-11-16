<script>
  
</script>

<template>
  <div class="main-page-window">
    <div class="search">
        <input type="text">
        <button class="search-find">Найти</button>
    </div>
    <div class="main-container">
      <div class="catalog-items">
        <ul>
          <li>Электроинструменты</li>
          <li>Газовое оборудование</li>
          <li>Ручные инструменты</li>
          <li>Крепеж</li>
          <li>Отделочные материалы</li>
          <li>Тепловые пушки</li>
        </ul>
      </div>
      <div class="catalog-view">
        <h1>Электроинструменты</h1>
        <div class="category-blocks">
          <div class="cat-block first-block">
            <h3>Электроинструменты</h3>
            <a href="#!">Аккумуляторные отвертки</a>
            <a href="#!">Лобзики</a>
            <a href="#!">Полировальные машины</a>
            <a href="#!">Аккумуляторные шуруповерты и дрели</a>
            <a href="#!">Миксеры и низкооборотистые дрели</a>
            <a href="#!">Пылесосы строительные</a>
            <a href="#!">Аккумуляторные инструменты</a>
            <a href="#!">Мини-пилы циркулярные</a>
            <a href="#!">Рубанки</a>
            <a href="#!">Бензопилы</a>
            <a href="#!">МФИ (реноваторы)</a>
            <a href="#!">Сабельные пилы</a>
          </div>  
          <div class="cat-block second-block">
            
          </div>
          <div class="cat-block thirt-block">
            
          </div>
        </div>
        
        
      </div>
    </div>
  </div>
  
 
</template>

<style scoped>
  .main-page-window {
      padding: 0 100px 0 100px;
      
      display: flex;
      flex-direction: column;
      justify-content: start;
      align-items: center;
      gap: 60px;
      
      width: 100%;
      height: 100vh;
  }

  .search {
      margin-top: 40px;
      width: 55%; 
      
      display: flex;
      justify-content: center;
      align-items: center;

      gap: 55px;

      input {
          border: 2px solid #ff812c;
          border-radius: 12px;
          width: 720px;
          height: 45px;
      }

      .search-find {
          padding: 10.5px 42px;
          border-radius: 50px;
          background-color: #ff812c;
          color: #fff;
      }
  }

  .main-container {
    width: 100%;
    display: flex;
    justify-content: start;
    gap: 30px;
  }

  .catalog-view {
    display: flex;
    flex-direction: column;
    gap: 20px;
    
    h1 {
      font-size: 25px;
      font-weight: 600;
    }
  }

  .catalog-items {
    width: 310px;
    height: 700px;
    background-color: #ff812c;
    border-radius: 12px;
    padding: 20px 16px;

    li {
      color: #fff;
      font-size: 18px;
      line-height: 40px;
    }
  }

  .category-blocks {
    display: flex;
  }

  .cat-block {
    display: flex;
    flex-direction: column;

    a {
      line-height: 35px;
    }

    h3 {
      font-weight: 600;
      margin-bottom: 10px;
    }
  }
  


</style>

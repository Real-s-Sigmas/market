<script>
export default {
  data() {
    return {
      isOpen: false,
    };
    
  },

  methods: {
    goCategory(name) {
      this.$emit("data-from-child", name);
    },

    catMenu() {
      this.isOpen = !this.isOpen;
    }
  },
};
</script>
<template>
  <div class="main-container ml-5 mt-7" :class="{ mainOpen: isOpen}">
    <button @click="catMenu" class="menu-btn" >|||</button>
    <div class="catalog-items grid gap-4">
      <ul>
        <li @click="goCategory(`Аккумуляторные инструменты`)">Аккумуляторные инструменты</li>
        <li @click="goCategory(`Электроинструменты`)">Электроинструменты</li>
        <li @click="goCategory(`Бензоинструмент`)">Бензоинструмент</li>
        <li @click="goCategory(`Компрессоры и пневмоинструменты`)">Компрессоры и пневмоинструменты</li>
        <li @click="goCategory(`Обогреватели`)">Обогреватели</li>
        <li @click="goCategory(`Сварочное оборудование`)">Сварочное оборудование</li>
        <li @click="goCategory(`Силовая техника`)">Силовая техника</li>
        <li @click="goCategory(`Сад и дача`)">Сад и дача</li>
        <li @click="goCategory(`Ручной инструмент`)">Ручной инструмент</li>
        <li @click="goCategory(`Крепеж и фурнитура`)">Крепеж и фурнитура</li>
        <li @click="goCategory(`Строительные материалы`)">Строительные материалы</li>
        <li @click="goCategory(`Отделочные материалы`)">Отделочные материалы</li>
        <li @click="goCategory(`Пиломатериалы`)">Пиломатериалы</li>
        <li @click="goCategory(`Хозтовары`)">Хозтовары</li>
        <li @click="goCategory(`Расходники`)">Расходники</li>
      </ul>
    </div>
  </div>
</template>
<style scoped>
.main-container {
  display: flex;
  justify-content: start;
  position: relative;
  background-color: #fff;
}

.menu-btn {
  color: #000;
  position: absolute;
  top: 10px;
  width: 30px;
  height: 30px;
  right: 10px;
}

.catalog-items ul {
  gap: 100px;
  justify-content: row;
  flex-wrap: nowrap;
}

.catalog-items {
  -webkit-box-shadow: 0px 1px 8px 0px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 0px 1px 8px 0px rgba(34, 60, 80, 0.2);
  box-shadow: 0px 1px 8px 0px rgba(34, 60, 80, 0.2);
  border-radius: 12px;
  overflow-y: scroll;
  height: 78vh;
  min-width: 360px;
  li {
    width: 100%;
    line-height: 55px;
    text-align: start;
    cursor: pointer;
    background-color: rgb(255, 255, 255);
    padding-left: 15px;
    padding-right: 31px;
    border-radius: 5px;
    transition: all 0.3s;
    font-size: 18px;
    font-weight: 570;
    color: black;
  }

  li:hover {
    background-color: rgb(250, 246, 246);
    color: rgb(255, 115, 0);
  }
}

  @media (min-width: 850px) {
    .menu-btn {
      display: none;
    }   
  }

@media (max-width: 850px) {
  .main-container {
  /*  margin-left: -320px; */
    position: absolute;
    left: -330px;   
  }

  .mainOpen {
    position: absolute;
    left: 0;
  }
}
</style>

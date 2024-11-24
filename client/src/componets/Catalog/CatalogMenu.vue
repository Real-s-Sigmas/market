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
        <li @click="goCategory(`Электроинструменты`)">Электроинструменты</li>
        <li @click="goCategory(`Садовая техника`)">Садовая техника</li>
        <li @click="goCategory(`Насосы и оборудование`)">Насосы и оборудование</li>
        <li @click="goCategory(`Садовый инструмент`)">Садовый инструмент</li>
        <li @click="goCategory(`Садовая сантехника`)">Садовая сантехника</li>
        <li @click="goCategory(`Расходные материалы`)">Расходные материалы</li>
        <li @click="goCategory(`Сварочные аппараты`)">Сварочные аппараты</li>
        <li @click="goCategory(`Аппараты плазменной резки`)">
          Аппараты плазменной резки
        </li>
        <li @click="goCategory(`Электроды, прутки, проволока`)">
          Электроды, прутки, проволока
        </li>
        <li @click="goCategory(`Принадлежности для сварки`)">
          Принадлежности для сварки
        </li>
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

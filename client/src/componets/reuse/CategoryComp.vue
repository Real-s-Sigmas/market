<script>
export default {
    data() {
        return {
            isOpen: false,
        }
    }
}
</script>

<template>
  <div class="category" :class="{ open: this.isOpen }">
      <ul>
          <button
              @click="this.isOpen = !this.isOpen"
              :class="{ 'btn-open': this.isOpen }"
              ><img src="../../assets/menu.svg" alt="" />
          </button>
          
          <li class="categ-item item-electro">Электроинструменты</li>
          <!-- <li class="categ-item"></li> -->
          <li class="categ-item">Ручные инструменты</li>
          <li class="categ-item">Крепеж</li>
          <li class="categ-item">Отделочные материалы</li>
          <li class="categ-item">Тепловые пушки</li>
      </ul>
  </div>
</template>

<style scoped>
.category {
  display: flex;
  justify-content: center;
  color: #fff;

  margin-top: 10px;

  padding: 0 5px 0 5px;

  width: 250px;
  height: 750px;
  background-color: #ff812c;
  /* border: 2px solid #FF812C; */
  border-radius: 12px;

  transition: all 400ms;


}

.category ul {
  display: flex;
  flex-direction: column;

  gap: 5px;

  margin-top: 10px;
}

.categ-item {
  cursor: pointer;
  font-size: 16px;
}


.category.open {
  margin-left: 0px;
  border-radius: 15px;
  padding: 10px 40px 0 10px;
  width: 250px;
  position: absolute;
}

.btn-open {
  position: absolute;
  margin-left: 180px !important;
  margin-top: -10px;
}

@media (min-width: 800px) {
  .category button {
    display: none;
  }
}

@media (max-width: 800px) {
  .category button {
    margin-left: 200px;
    position: absolute;
  }

  .category {
    width: 300px;
    margin-left: -255px;
    padding: 0;
    /* width: 50px; */
    border-radius: 0 10px 15px 0;
    position: absolute;
    z-index: 52;

    transition: all 400ms;
  }
}
</style>
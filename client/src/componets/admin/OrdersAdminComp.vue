<script>
  export default {
    data() {
      return {
        orderNum: "000001",
      }
    },

    props: {
      order: Object
    }
  }
</script>

<template>
  <a :href="`/basketadmin/${order.id}`">
    <div class="comp-block" :class="{'grey': order.status == 'END', 'yellow': order.status == 'WAITING', 'green': order.status == 'PROCESS'}">
      <p class='font-bold'>Номер пользователя: {{ order.phonenumber }}</p>
      <p>Количество товаров: {{ order.ids_items.length }}</p>
      <p>Статус: {{ order.status }}</p>
      <p>{{ order.date_create }}</p>
    </div>
  </a>
  
</template>

<style scoped>
.grey {
  background: rgb(201, 199, 199);
  border-color: rgb(201, 199, 199) !important;
}

.yellow {
  border-color: rgb(157, 255, 0) !important;
}

.green {
  border-color: rgb(255, 238, 0) !important;
}

a {
  width: 300px;
}
.comp-block {
  width: 300px;
  height: 150px;
  border: 1px solid #ff813c;
  border-radius: 16px;

  display: flex;
  flex-direction: column;
  justify-content: space-between;

  padding: 15px;

  h3 {
    margin-bottom: 20px;
    color: #ff813c;
    font-weight: 500;
  }

  p {
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
}
</style>

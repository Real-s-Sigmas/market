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
    <div class="comp-block">
      <h3>№ {{ order.orderNum }}</h3>
      <p>{{ order.description }}</p>
      <p>{{ order.date }}</p>
    </div>
  </a>
  
</template>

<style scoped>

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

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userName: "Meee",
    }
  }
}
  
</script>

<template>
<div class="window">
  <h2>Приветствую, {{userName}}</h2>
  <a href="/ResetPassword">Изменить пароль</a>
</div>
</template>

<style scoped>
.window {
  width: 100%;
  padding: 50px 100px;

  display: flex;
  flex-direction: column;
  gap: 20px;
}

h2 {
  font-size: 38px;
  font-weight: 500;
}

a {
  color: #ff812c;
  text-decoration: underline;
  font-size: 22px;
}
</style>

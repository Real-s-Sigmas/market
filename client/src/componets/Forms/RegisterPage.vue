<script>
import axios from 'axios';

export default {
  data() {
    return {
      disabled: false,
      email: "",
      password: "",
      error: "",
      phonenumber: "",
      name: "",
    };
  },
  methods: {
    async login() {
      try {
        let response = await axios.post(`/user/sign-up`, {
          email: this.email,
          password: this.password,
          phonenumber: this.phonenumber,
          name: this.name,
        });
        this.error = response.data.res;

        if (this.error == "ok") {
          this.$router.push("/EnterEmail");
        } else {
          this.error = "Заполните все поля правильно!";
        }
      } catch (err) {
        console.error(err);
        this.error = "Ошибка сервера";
      }
    },
  },
};
</script>
<template>
  <div class="window">
    <div class="container">
      <div class="div-nickname">
        <form @submit.prevent="login">
          <input
            type="text"
            class="input"
            autofocus
            required
            v-model="name"
            placeholder="Ваше имя"
          />
          <input
            type="text"
            class="input"
            autofocus
            required
            v-model="phonenumber"
            placeholder="Номер телефона"
          />
          <input
            type="text"
            class="input"
            autofocus
            required
            v-model="email"
            placeholder="Почта"
          />
          <input
            type="password"
            class="input"
            autofocus
            required
            v-model="password"
            placeholder="Пароль"
          />
          <button class="btn" type="submit">Зарегистрироваться</button>
        </form>
        <a href="/Login" class="haveAcc">Уже есть аккаунт?</a>
        <p class="error">{{ error }}</p>
      </div>
    </div>
  </div>
</template>
<style scoped>
:root {
  --font-family: "Rubik", sans-serif;
  --second-family: "Inter", sans-serif;
}
.error {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 17px;
  color: red;
  z-index: 10000;
}

.haveAcc {
  color: #ff812c;
  font-size: 18px;
  font-weight: 500;
  line-height: 50px;
}

.haveAcc:hover {
  color: #d95700;
}

.btn {
  top: 77px;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 20px;
  text-align: center;
  color: #ffffff;
  background: #ff812c;
  cursor: pointer;
  border-radius: 15px;
  width: 430px;
  height: 60px;
  border: none;
  z-index: 7000;
  transition: all 0.1s;
}

.btn:hover {
  background-color: #d95700;
}

.btn:disabled {
  top: 77px;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  text-align: center;
  background: #eae9e9;
  cursor: pointer;
  border-radius: 15px;
  width: 430px;
  height: 60px;
  border: none;
  cursor: pointer;
  z-index: 7000;
  color: #5b5a5a;
}
.btn:disabled:hover {
  background: #e1e1e1;
  transition: all 0.3s;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.window {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 600px;
}
.input {
  margin-bottom: 20px;
  border-radius: 15px;
  width: 430px;
  height: 60px;
  background: #eae9e9;
  border: none;
  padding: 20px;
  font-family: var(--font-family);
  font-weight: 500;
  font-size: 20px;
  color: #000000;
}
.div-nickname {
  position: relative;
  width: 420px;
}
.div-nickname span {
  position: absolute;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  color: #5b5a5a;
  top: 14px;
  left: 18px;
  pointer-events: none;
  transition: 0.3s ease;
  border-radius: 15px;
  width: 115px;
}
.input {
  margin-bottom: 20px;
  border-radius: 15px;
  width: 430px;
  height: 60px;
  background: #eae9e9;
  border: none;
  padding: 20px;
  font-family: var(--font-family);
  font-weight: 500;
  font-size: 20px;
  color: #000000;
}
.input:focus,
.input:valid {
  outline: none;
  border: none;
  border: 4px solid #ff812c;
  transition: all 0.1s;
}
.input:focus ~ span,
.input:valid ~ span {
  transform: translateY(-115%);
  font-size: 20px;
  left: 15px;
  border: solid #ff812c;
  background: #ff812c;
  color: #fff;
  width: 110px;
  text-align: center;
  border-radius: 15px;
}

@media (max-width: 505px) {
  .input {
    width: 350px;
    height: 60px;
  }
  .btn {
    width: 350px;
    height: 60px;
  }
  .btn:disabled {
    width: 350px;
    height: 60px;
  }
  .div-nickname {
    position: relative;
    width: 200px;
    margin-right: 150px;
  }
}
</style>

<script>
export default {
  data() {
    return {
      disabled: false,
      email: "",
      nickName: "",
      error: "",
    };
  },
  methods: {
    input($event) {
      this.disabled = true;
      this.error = "";
      
      if (this.email) {
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email)) {
          this.disabled = false;
        } else if (this.email.length > 7 ) {
            this.error = "Почта невалидна!";
        }
      }

      if (!this.nickName) {
        this.error = "Поле имени должно быть заполнено!";   
        this.disabled = true;
      } else if (this.nickName.length < 2) {
        this.error = "В имени должно быть не менее 2 букв!";
        this.disabled = true;
      } else if (!/^[a-zA-Zа-яА-ЯёЁ]+$/.test(this.nickName)) {
        this.error = "Имя должно содержать только буквы!";
        this.disabled = true;
      }
    },
  },
};
</script>
<template>
  <div class="window">
    <div class="container">
      <div class="div-nickname">
        <form>
          <input
            type="text"
            class="input input-nick-span"
            autofocus
            required
            v-model="email"
            @input="input($event)"
          />
          <span class="nick-span">Почта</span>

          <input
            type="text"
            class="input input-nickName"
            required
            v-model="nickName"
            @input="input($event)"
          />
          <span class="nickName">Имя</span>
          <button class="btn" :disabled="disabled">Зарегистрироваться</button>
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
  transition: all 0.1s;
}

.haveAcc:hover {
  color: #d95700;
}

.btn {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  color: #ffffff;
  background-color: #ff812c;
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

.div-nickname {
  position: relative;
  width: 420px;
}
.nick-span {
  position: absolute !important;
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

.nickName {
  position: absolute !important;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  color: #5b5a5a;
  top: 94px;
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
.input-nick-span:focus ~ .nick-span,
.input-nick-span:valid ~ .nick-span {
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

.input-nickName:focus ~ .nickName,
.input-nickName:valid ~ .nickName {
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

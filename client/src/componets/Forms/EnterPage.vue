<script>
export default {
  data() {
    return {
      disabled: false,
      code: "",
      error: "",
    };
  },
  methods: {
    input($event) {
      this.disabled = true;
      if ($event) {
        if (this.code.length == 0) {
          this.error = "Поле не должно быть пустым!";
        } else if (this.code.length > 0) {
          this.error = "";
          this.disabled = false;
        } else if (this.code.length < 5) {
          this.error = "Минимум 5 символов!";
        } else if (this.code.length == 5) {
          this.error = "";
          this.disabled = true;
        }
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
            class="input"
            autofocus
            required
            v-model="code"
            @input="input($event)"
            maxlength="5"
          />
          <span сlass="nick">Код</span>
          <button class="btn" :disabled="disabled">Отправить</button>
        </form>
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
.head {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  position: absolute;
  top: 230px;
  color: #000000;
}
.error {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 17px;
  color: red;
  position: absolute;
  top: 155px;
  z-index: 10000;
  left: 5px;
}
.btn {
  position: absolute;
  top: 77px;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  text-align: center;
  color: #ffffff;
  background: #ff812c;
  cursor: pointer;
  border-radius: 15px;
  width: 430px;
  height: 60px;
  border: none;
  cursor: pointer;
  z-index: 7000;
}
.btn:disabled {
  position: absolute;
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
.btn:hover {
  background: #ef7c30;
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
  margin-bottom: 40px;
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
  margin-bottom: 40px;
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

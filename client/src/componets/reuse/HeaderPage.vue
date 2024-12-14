<script>
export default {
  data() {
    return {
      isOpen: true,
      isLogged: false,
      burg: true,
    };
  },

  methods: {
    burgmenu() {
      this.burg = !this.burg;
    },
  },
};
</script>

<template>
  <div class="header" :class="{ open: this.isOpen }">
    <div class="div-ob logo-title cursor-pointer" @click="this.$router.push('/')">
      <img width="50" src="../../assets/icons/logoMarket.svg" alt="" />
      <h1>
        Строительство <br />
        и <br />
        Ремонт
      </h1>
    </div>
    <div class="navigate">
      <div class="links">
        <button class="link-btn" @click="this.$router.push('/')">Главная</button>
        <button class="link-btn" @click="this.$router.push('/Catalog')">Каталог</button>
        <button class="link-btn" @click="this.$router.push('/aboutus')">О нас</button>
      </div>
      <div class="div-ob fav-acc">
        <a href="/Favorites">
          <svg
            class="favorite"
            width="35px"
            height="35px"
            viewBox="0 0 24 24"
            fill="white"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z"
              stroke="#000000"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </a>

        <a href="/basket">
          <svg
            width="35px"
            height="35px"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M21 10L15 4M21 10H3M21 10L19.6431 16.7845C19.2692 18.6542 17.6275 20 15.7208 20H8.27922C6.37249 20 4.73083 18.6542 4.35689 16.7845L3 10M3 10L9 4"
              stroke="#000000"
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </a>

        <button v-if="isLogged" @click="burgmenu" class="burgmenu">
          <svg
            width="35px"
            height="35px"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M4 6H20M4 12H20M4 18H20"
              stroke="#000000"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </button>
        <button v-if="!isLogged" class="acc" @click="this.$router.push('/Login')">
          Войти
        </button>
      </div>
    </div>

    <div class="contact">
      <p>
        Для связи: <br />
        8 495 255 87 65
        <a class="shortTg" href="#!"><img src="../../assets/icons/tgicon.svg"  alt="" /></a>
      </p>
      <a class="tg" href="#!"><img src="../../assets/icons/tgicon.svg" alt="" /></a>
    </div>
  </div>
  <div class="btn-top">
    <button >
      <img @click="this.isOpen = !this.isOpen" src="../../assets/menu.svg" alt="" />
    </button>
  </div>
  <div class="two-blocks" :class="{ close: this.isOpen }">
    <div class="bl block-link">
      <button class="link-btn" @click="this.$router.push('/')">Главная</button>
      <button class="link-btn" @click="this.$router.push('/catalog')">Каталог</button>
      <button class="link-btn" @click="this.$router.push('/aboutus')">О нас</button>
    </div>
    <div class="bl block-btns">
      <a href="/Favorites">
        <svg
          class="favorite"
          width="35px"
          height="35px"
          viewBox="0 0 24 24"
          fill="white"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z"
            stroke="#000000"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </a>

      <a href="/basket">
        <svg
          width="35px"
          height="35px"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M21 10L15 4M21 10H3M21 10L19.6431 16.7845C19.2692 18.6542 17.6275 20 15.7208 20H8.27922C6.37249 20 4.73083 18.6542 4.35689 16.7845L3 10M3 10L9 4"
            stroke="#000000"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </a>

      <button v-if="isLogged" @click="burgmenu" class="burgmenu">
        <svg
          width="35px"
          height="35px"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M4 6H20M4 12H20M4 18H20"
            stroke="#000000"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </button>
      <button v-if="!isLogged" class="acc" @click="this.$router.push('/Login')">
        Войти
      </button>
      <a class="shortTg" href="#!"><img src="../../assets/icons/tgicon.svg"  alt="" /></a>
    </div>
  </div>
</template>

<style scoped>
button {
  border: none;
}

.two-blocks {
  display: flex;
  flex-direction: column;
  align-items: end;
  gap: 10px;

  position: absolute;
  right: 20px;

  transition: all 100ms;

  z-index: 1000;
}

.shortTg {
  display: block;
  width: 20px;
  height: 20px;
}

.contact p {}

.bl {
  width: 180px;
  height: 50px;
  background-color: #fff;
  box-shadow: 2px 2px 7px #6f6f6f;
  border-radius: 50px;

  display: flex;
  justify-content: center;
  align-items: center;
}

.block-link {
  padding: 0 5px;
  width: 290px;
  gap: 10px;
}

.block-btns {
  width: 310px;
  gap: 20px;
}

.acc:hover {
  padding: 8px 34px !important;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;


  width: 100%;
  height: 80px;

  padding: 0 100px 0 100px;
  margin-top: 32px;

  transition: all 300ms;
}

.navigate {
  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 0 40px;

  width: 70%;
  height: 80px;

  border-radius: 50px;
  box-shadow: 2px 2px 7px #6f6f6f;

  position: relative;
}

.contact p {
  line-height: 20px;
  color: #ff812c;
}

.links {
  width: 60%;
  display: flex;
  justify-content: space-between;
}

.links button {
  font-weight: 600;
}

.link-btn {
  width: 140px;
  height: 50px;
  font-size: 18px;

  border-radius: 50px;

  transition: all 100ms;
}

.link-btn a {
  font-size: 22px;
  color: #2b2b2b;
}

.link-btn:hover {
  background-color: #2b2b2b;
  color: #fff;
}

.link-btn:active {
  background-color: #191919;
}

.btn-top {
  display: flex;
  justify-content: space-between;
  align-items: center;

  z-index: 1000;
}


.title {
  font-weight: 700;
  margin-left: 20px;
  font-size: 25px;
}

.logo {
  width: 40px;
  height: 40px;

  border: 2px solid #000;
  border-radius: 50px;
}

.acc {
  padding: 8px 34px;
  border-radius: 50px;

  background-color: #ff812c;
  color: #fff;

  font-size: 20px;
  font-weight: 600;

  transition: all 100ms;
}

.acc:hover {
  padding: 10px 40px !important;
}

.acc:active {
  background-color: #d95700;
  border-color: #d95700;
}

.fav-acc a {
  margin-right: 40px;
}

.fav-acc svg {
  transition: all 100ms;
}

.fav-acc svg:hover {
  fill: #ff812c;
}

.fav-acc svg:active {
  fill: #d95700;
}

.div-ob {
  display: flex;
  align-items: center;
  gap: 5px;

  h1 {
    font-weight: 500;
  }
}

.open {
}

.close {
  display: none;
}

@media (min-width: 1000px) {
  .btn-top img {
    display: none;
  }
}

@media (max-width: 1300px) {
  .navigate {
    padding: 0 20px;
  }

  .link-btn {
    font-size: 16px;
    width: 100px;
    height: 40px;
  }

  .links {
    margin-right: 20px;
    gap: 10px;
  }

  .header {
    padding: 0 40px;
  }
}

@media (min-width: 1175px) {
  .contact {
    .tg {
      display: none;
    }
  }
}

@media (max-width: 1175px) {
  .div-ob {
    h1 {
      display: none;
    }
  }

  .link-btn {
    font-size: 14px;
  }

  .acc {
    font-size: 14px;
  }

  .acc:hover {
    padding: 12px 45px;
  }

  .fav-acc {
    gap: 30px;
  }

  .fav-acc a {
    margin-right: 0 !important;
  }

  .contact {
    a {
      display: block;

      img {
        width: 30px;
      }
    }

    p {
      display: none;
    }
  }
}

@media (max-width: 1000px) {
  .btn-top button {
    background-color: #191919;
    padding: 5px;
    border-radius: 12px;
  }

  .header {
    margin-top: 10px;
  }

  .navigate,
  .contact {
    display: none;
  }

  .btn-top {
    position: absolute;
    top: 25px;
    right: 20px;
  }
}

@media (max-width: 500px) {
  .header {
    padding: 0 10px;
  }

  .btn-top {
    right: 10px;
  }
}
</style>

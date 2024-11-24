<script>
import CatalogMenu from "./CatalogMenu.vue";
import { Catalog } from "./catalog.js";
export default {
  data() {
    return {
      catalog: Catalog,
      data: "Электроинструменты",
      tmps: null,
    };
  },
  methods: {
    handleDataFromChild(data) {
      this.data = data;
      console.log(this.data);
      this.getData();
    },
    getData() {
      switch (this.data) {
        case "Электроинструменты":
          this.tmps = this.catalog[0].Электроинструменты;
          console.log(this.tmp);
          break;
        case "Садовая техника":
          this.tmps = this.catalog[1].Садоваятехника;
          console.log(this.tmp);
          break;
        case "Насосы и оборудование":
          this.tmps = this.catalog[2].Насосыиоборудование;
          console.log(this.tmp);

          break;
        case "Садовый инструмент":
          this.tmps = this.catalog[3].Садовыйинструмент;
          console.log(this.tmp);
          break;
        case "Садовая сантехника":
          this.tmps = this.catalog[4].Садоваясантехника;
          console.log(this.tmp);

          break;
        case "Расходные материалы":
          this.tmps = this.catalog[5].Расходныематериалы;
          console.log(this.tmp);

          break;
        case "Сварочные аппараты":
          this.tmps = this.catalog[6].Сварочныеаппараты;
          console.log(this.tmp);

          break;
        case "Аппараты плазменной резки":
          this.tmps = this.catalog[7].Аппаратыплазменнойрезки;
          console.log(this.tmp);

          break;
        case "Электроды, прутки, проволока":
          this.tmps = this.catalog[8].Электродыпруткипроволока;
          console.log(this.tmp);

          break;
        case "Принадлежности для сварки":
          this.tmps = this.catalog[9].Принадлежностидлясварки;
          console.log(this.tmp);
          break;
        default:
        // Код, если значение this.data не соответствует ни одному из case
      }
    },
  },
  components: {
    CatalogMenu,
  },
  mounted() {
    console.log(this.data);
    this.getData();
  },
};
</script>

<template>
  <div class="content">
    <CatalogMenu @data-from-child="handleDataFromChild" />
    <div class="content-links mt-4">
      <h1>{{ this.data }}</h1>
      <ul class="mt-5">
        <li v-for="item in tmps" :key="item.url" class="mr-3"><a href="">{{ item.title }}</a></li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-size: 45px;
  font-weight: 700;
  color: black;
}
.content {
  display: flex;
  gap: 30px;
}
.content-links {
  justify-content: start;

  ul {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 2 столбца равной ширины */
    list-style: none; /* Удаление маркеров списка */
    padding: 0;
    grid-column-gap: 20px;
    grid-row-gap: 11px; 
  }
  li{
    transition: all 0.3s;
    font-size: 18px;
    font-weight: 570;
    color: rgb(255, 174, 0);
    text-decoration: underline
  }
}

      @media (max-width: 1200px) {
        h1 {
          font-size: 35px;
        }
        .content-links {
          ul {
            grid-template-columns: repeat(2, 1fr);
          }
        }
      }

      @media (max-width: 990px) {
        .content-links {
          ul {
            grid-template-columns: repeat(1, 1fr);
          }

          overflow-y: hidden;
        }

        
      }

      @media (max-width: 850px) {
        .content-links {
          margin-left: 60px;
        }
      }

      @media (max-width: 520px) {
        h1 {
          font-size: 24px;
        }

        .content-links {
          ul {
            li {
              a {
                font-size: 16px;
              }
            }
          }  
        }
        
      }
</style>

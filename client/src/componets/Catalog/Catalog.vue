<script>
import CatalogMenu from "./CatalogMenu.vue";
import { Catalog } from "./catalog.js";

export default {
  data() {
    return {
      catalog: Catalog,
      data: "Электроинструменты", // Категория по умолчанию
      tmps: null,
    };
  },
  methods: {
    async handleDataFromChild() {
      this.data = await axios.get("/catalog");
      this.getData();
    },
    getData() {
      const normalizedData = this.data.toLowerCase().replace(/\s+/g, "");
      const foundCategory = this.catalog.find((category) => {
        const keys = Object.keys(category);
        return keys.some(
          (key) => key.toLowerCase().replace(/\s+/g, "") === normalizedData
        );
      });
      this.tmps = foundCategory
        ? foundCategory[
            Object.keys(foundCategory).find(
              (key) => key.toLowerCase().replace(/\s+/g, "") === normalizedData
            )
          ]
        : [];
      console.log(this.tmps);
    },
  },
  components: {
    CatalogMenu,
  },
  mounted() {
    this.handleDataFromChild();
  },
};
</script>

<template>
  <div class="content">
    <CatalogMenu @data-from-child="handleDataFromChild" />
    <div class="content-links mt-4">
      <h1>{{ this.data }}</h1>
      <ul class="mt-5" v-if="tmps">
        <li v-for="item in tmps" :key="item.url" class="mr-3">
          <a :href="item.url">{{ item.title }}</a>
        </li>
      </ul>
      <p v-else>Товары для этой категории не найдены.</p>
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
  li {
    transition: all 0.3s;
    font-size: 18px;
    font-weight: 570;
    color: rgb(255, 174, 0);
    text-decoration: underline;
  }

  li:hover {
    color: #d95700;
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

<script>
import axios from "axios";
import { Category } from "../admin/categories.js";
import { Catalog } from "../Catalog/catalog.js";

export default {
  data() {
    return {
      topics: Category,
      underTopics: [],
      error: ``,

      product: {},
      tmps: [],
      photos: [],
    };
  },

  watch: {
    "product.category"(newValue) {
      this.underTopics = [];
      for (let i = 0; i < Catalog.length; i++) {
        if (Object.keys(Catalog[i])[0] == this.product.category.category) {
          for (
            let j = 0;
            j < Catalog[i][Object.keys(Catalog[i])[0]].length;
            j++
          ) {
            this.underTopics.push(
              Catalog[i][Object.keys(Catalog[i])[0]][j].title
            );
          }
        }
      }
    },
  },

  mounted() {
    this.getProduct();
  },

  methods: {
    async getProduct() {
      try {
        let res = await axios.get("/items/one-item", {
          params: {
            id: this.$route.params.id,
          },
        });
        this.product = res.data.res;
        this.photos = res.data.res.photos;
      } catch (error) {
        console.log(error);
      }
    },

    async addProduct() {
      try {
        let res;
        if (!this.product.category.category) {
          // говнокод
          console.log(this.product.photos);
          res = await axios.put("/items/put-item/text", {
            id: this.$route.params.id,
            title: this.product.title,
            price: this.product.price,
            photos: this.photos,
            category: this.product.category,
            small_category: this.product.small_category,
            descriptions: this.product.descriptions,
            characteristics: this.product.characteristics,
          });
        } else {
          res = await axios.put("/items/put-item/text", {
            id: this.$route.params.id,
            title: this.product.title,
            price: this.product.price,
            photos: this.photos,
            category: this.product.category.category,
            small_category: this.product.small_category,
            descriptions: this.product.descriptions,
            characteristics: this.product.characteristics,
          });
        }

        if (res.data.res == "Error") {
          this.error = "Ошибка добавления товара";
          console.log("error");
        } else {
          //   this.$router.push("/");
        }
      } catch (error) {
        this.error = "Ошибка добавления товара";
        console.log(error);
      }

      try {
        let res = await axios.put("/items/put-item/image", this.formdata, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            this.percentCompleted = percentCompleted;
          },
        });
      } catch (error) {
        console.error("Ошибка при отправке данных:", error);
        return;
      }
    },

    async convertFile(event, name) {
      if (event && name) {
        const files = event.target.files;
        if (files && files.length > 0) {
          if (!this.formdata) {
            this.formdata = new FormData();
          }

          for (let i = 0; i < files.length; i++) {
            const file = files[i];
            this.formdata.append(name, file); // Добавляем файлы в FormData
            this.photos.push(file.name);
            console.log("Файл(ы) успешно добавлены в formdata");
          }
          const reader = new FileReader();
          reader.onload = (e) => {
            if (reader.result) {
              console.log("Файлы успешно прочитаны");
            }
          };
          if (files.length > 0) {
            reader.readAsDataURL(files[0]);
          }
        } else {
          console.log("Нет файлов для загрузки");
        }
      } else {
        console.log("Неверные аргументы для convertFile");
      }
    },
    deleteImage() {
    this.photos = []; // Очистить массив загруженных изображений
    if (this.product && this.product.photos) {
      this.product.photos = []; // Очистить массив фотографий продукта
    }
    console.log("Изображения успешно очищены");
  },
  },

};
</script>

<template>
  <form
    @submit.prevent="addProduct"
    class="post-container mx-0 flex flex-col mt-16"
  >
    <div class="up-info flex xl:gap-16 justify-between">
      <label for="filee" class="input-file">
        <div
          class="image-container border-black py-20 rounded-xl flex justify-center items-center select-none"
          role="button"
        >
          <input
            type="file"
            name="file[]"
            id="filee"
            multiple
            @change="convertFile($event, 'images')"
            accept="image/*"
          />
          <span>+</span>
        </div>
      </label>
      <div class="main-info-block flex flex-col">
        <div class="main-inputs-block flex flex-row xl:gap-12 xl:mt-0 mt-4">
          <div class="flex flex-col gap-2 text-2xl flex-1">
            <label for="title">Название:</label>
            <input
              type="text"
              id="title"
              v-model="product.title"
              class="mb-5"
            />
          </div>
          <div class="select-block">
            <select
              class="sell text-2xl px-10 pe-16 mt-3"
              v-model="product.category"
            >
              <option selected :value="product.category">
                {{ product.category }}
              </option>
              <option :value="topic" v-for="topic in topics">
                {{ topic.category }}
              </option>
            </select>
            <select
              class="sell text-2xl px-10 pe-16 mt-3"
              v-model="product.small_category"
              v-if="this.product.category"
            >
              <option selected :value="product.small_category">
                {{ product.small_category }}
              </option>
              <option :value="title" v-for="title in underTopics">
                {{ title }}
              </option>
            </select>
          </div>
        </div>
        <div class="text-2xl">
          <label for="desc_short mt-1">Краткое описание:</label>
          <textarea
            class="short-desc border border-black mt-3"
            rows="2"
            type="text"
            id="desc_short"
            v-model="product.descriptions"
          ></textarea>
        </div>
      </div>
    </div>

    <!-- <div id="imageContainer">
      <div class="one-image" v-for="(image, index) in product.photos">
        <img class="image-one" :src="image" alt="Изображение" />
        <img
          @click="deleteImage(index)"
          class="close-btn"
          src="../../assets/close-img.png"
        />
      </div>
    </div> -->

    <div class="m-c flex flex-col">
      <label for="fullDescription" class="text-2xl mt-8"
        >Подробное описание:</label
      >
      <textarea
        id="fullDescription"
        rows="10"
        v-model="product.characteristics"
        class="border-2 border-black mt-3 p-1 rounded"
      ></textarea>
    </div>
    <div
      class="price-block m-c flex xl:justify-between xl:flex-row flex-col gap-10"
    >

    <!-- во кнопка -->
        <div><button class="ml-7 mt-7" @click="deleteImage">Очистить картинки</button></div>



      <label for="price" class="text-2xl mt-8">Цена товара:</label>
      <div class="flex gap-3">
        <input
          id="price"
          v-model="product.price"
          class="price border-2 border-black mt-3 p-1"
        />
      </div>

      <button type="submit" class="acc mt-8">Изменить</button>
    </div>
    <h2 class="text-red-500 text-xl text-semibold mt-10" v-if="this.error">
      {{ error }}
    </h2>
  </form>

  <div class="mt-7 ml-5 d-flex">
    <ul>
      <li v-for="(photo, index) in this.product.photos">
        <a :href="photo" target="blank"
          >Ссылка на изображение №{{ index + 1 }}</a
        >
      </li>
    </ul>
  </div>
</template>

<style scoped>
.acc {
  padding: 8px 34px;
  border-radius: 50px;

  background-color: #ff812c;
  color: #fff;

  font-size: 20px;
  font-weight: 600;

  transition: all 200ms;
}

.acc:hover {
  background-color: #d95700;
}

.select-block {
  position: relative;
}

.arrow-down {
  position: absolute;
  bottom: 40px;
  right: 35px;
  z-index: 10;
}

.one-image {
  position: relative;
}

.close-btn {
  position: absolute;
  top: -15px;
  right: -15px;
  padding: 8px;
  background-color: #1e1e1e;
  z-index: 52;
  border-radius: 100%;
  cursor: pointer;
}

#imageContainer {
  display: flex;
  gap: 62.8px;
  flex-wrap: wrap;
  /* justify-content: space-between; */
  margin-top: 30px !important;
}

.image-one {
  width: 120px;
  height: 120px;
  border-radius: 15px;
  object-fit: cover;
  border: 3px solid #1e1e1e;
}

.input-file {
  position: relative;
  display: flex;
}

.input-file span {
  font-size: 185px;
  font-weight: 100;
  transition: color 0.3s;
}

.input-file input[type="file"] {
  position: absolute;
  z-index: -1;
  opacity: 0;
  display: block;
  width: 0;
  height: 0;
}

.input-file:hover span {
  color: #ff812c;
}

select {
  margin-top: 38px;
  height: 52px;
  background-color: #ff812c;
  color: #fff;
  border-radius: 15px;
  appearance: none;
  position: relative;
  background-image: url("../../assets/arrowDown.png");
  background-size: 24px 12px;
  background-position: 85% 54%;
  background-repeat: no-repeat;
}

@media (max-width: 1124px) {
  select {
    background-position: 96% 54%;
  }
}

input,
textarea {
  width: 100%;
  padding: 8px;

  font-size: 20px;

  border: 3px solid #000;

  border-radius: 10px;
}

input {
  height: 52px;
}

textarea {
  height: 120px;
}

.short-desc {
  width: 100%;
}

.image-container {
  height: 280px;
  width: 280px;
  font-size: 185px;
  font-weight: 100 !important;
  border: 3px solid #1e1e1e;
}

@media (min-width: 1400px) {
  .post-container {
    margin-left: 260px;
    margin-right: 260px;
  }

  .up-info,
  .text-red-500 {
    margin: 0 185px;
  }

  .main-info-block {
    flex-grow: 1;
  }

  .m-c {
    margin: 0 185px;
  }

  #imageContainer {
    margin: 0 185px;
  }
}

@media (max-width: 1400px) {
  .m-c,
  .up-info,
  .text-red-500 {
    margin: 0 30px;
  }
}

@media (max-width: 1284px) {
  .image-container {
    width: 100%;
  }

  .up-info,
  .main-inputs-block {
    flex-direction: column !important;
  }

  select {
    margin-top: 0;
    margin-bottom: 15px;
    width: 100%;
  }

  #imageContainer {
    margin: 10px 30px !important;
    gap: 15px;
    justify-content: center;
  }

  .image-one {
    width: 75px;
    height: 75px;
    border-radius: 13px;
    object-fit: cover;
    border: 3px solid #1e1e1e;
  }

  .close-btn {
    padding: 4px;
  }

  .text-xl {
    font-size: 20px !important;
  }

  select {
    padding-left: 10px;
  }

  .arrow-down {
    bottom: 32px;
  }

  .price-block {
    flex-direction: column;
    gap: 0;
  }

  .price {
    margin-top: 0 !important;
  }
}

.price {
  width: 500px;
  height: 50px;
  border: none;
  border-bottom: 3px solid #1e1e1e;
  border-radius: 0 !important;
  margin-top: 24px;

  &:focus {
    outline: none;
  }
}

.price-block div span {
  font-size: 45px;
}
</style>

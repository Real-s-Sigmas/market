<script>
export default {
    data() {
        return {
            categories: [
                {
                    name: 'Электроинструменты',
                    subItems: [
                        { name: 'Дрели', subSubItems: ['Аккумуляторные дрели', 'Сетевые дрели'] },
                        { name: 'Перфораторы', subSubItems: ['SDS+', 'SDS Max'] },
                        { name: 'Шуруповерты', subSubItems: ['Сетевые шуруповерты', 'Аккумуляторные шуруповерты'] },
                    ],
                },
                {
                    name: 'Ручные инструменты',
                    subItems: [
                        { name: 'Молотки', subSubItems: ['Кувалды', 'Столярные молотки'] },
                        { name: 'Отвертки', subSubItems: ['Крестовые', 'Плоские'] },
                        { name: 'Клещи', subSubItems: ['Комбинированные клещи', 'Длинногубцы'] },
                    ],
                }
            ],
            activeIndex: null,
            activeSubIndex: null,
            mousePosition: { x: 0, y: 0 }
        };
    },

    methods: {
        showSubMenu(index) {
            this.activeIndex = index;
            this.activeSubIndex = null;
            console.log("show");
        },
        
        showSubSubMenu(subIndex) {
            this.activeSubIndex = subIndex;
            console.log("show-show");
        },

        hideAllMenus() {
            this.activeIndex = null;
            this.activeSubIndex = null;
            console.log("hide");
        },

        updateMousePosition(event) {
            this.mousePosition = { x: event.clientX, y: event.clientY };
        },

        onSubItemMouseLeave(event, index) {
            if (this.isOutsideElement(event, index)) {
                this.activeSubIndex = null;
            }
        },

        isOutsideElement(event, index) {
            const subMenuRect = this.$refs[`subMenu-${index}`]?.getBoundingClientRect();
            if (!subMenuRect) return false;
            return (
                event.clientX < subMenuRect.left ||
                event.clientX > subMenuRect.right ||
                event.clientY < subMenuRect.top ||
                event.clientY > subMenuRect.bottom
            );
        }
    }
};
</script>

<template>
    <div class="category" @mouseleave="hideAllMenus" @mousemove="updateMousePosition">
        <ul>
            <li v-for="(item, index) in categories"
                :key="index"
                class="categ-item"
                @mouseenter="showSubMenu(index)">
                {{ item.name }}
                <div class="submenu" v-if="activeIndex === index" ref="subMenu">
                    <ul>
                        <li v-for="(subItem, subIndex) in item.subItems"
                            :key="subIndex"
                            @mouseenter="showSubSubMenu(subIndex)"
                            @mouseleave="onSubItemMouseLeave($event, index)">
                            {{ subItem.name }}
                            <div class="subsubmenu" v-if="activeSubIndex === subIndex">
                                <ul>
                                    <li v-for="(subSubItem, subSubIndex) in subItem.subSubItems" :key="subSubIndex" @click="selectItem(subSubItem)">
                                        <a href="http://localhost:5174/edit">{{ subSubItem }}</a>
                                    </li>
                                </ul>
                            </div>
                        </li>
                    </ul>
                </div>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.category {
    position: relative;
    height: 500px;
    width: 600px;
}

.categ-item {
    position: relative;
    padding: 10px;
    width: 200px;
    cursor: pointer;
}

.submenu {
    position: absolute;
    width: 140px;
    height: 150px;
    left: 200px;
    top: 0;
    background-color: #a9a9a9;
    border: 1px solid #000;
    padding: 10px;
    display: block;
    white-space: nowrap;
}

.submenu ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.submenu li {
    padding: 5px 0;
}

.subsubmenu {
  position: absolute;
  width: 200px;
  height: 100px;
  left: 150px;
  top: 0;
  background-color: #e9e9e9;
  border: 1px solid #bbb;
  padding: 10px;
  white-space: nowrap;
}

.subsubmenu ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.subsubmenu li {
  padding: 5px 0;
}

</style>

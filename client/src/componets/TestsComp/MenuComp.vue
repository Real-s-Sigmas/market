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
        };
    },

    methods: {
        showSubMenu(index) {
            this.activeIndex = index;
            this.activeSubIndex = null;
        },
        
        showSubSubMenu(subIndex) {
            this.activeSubIndex = subIndex;
        },

        hideAllMenus() {
            this.activeIndex = null;
            this.activeSubIndex = null;
        }
    }
};
</script>

<template>
    <div class="category" @mouseleave="hideAllMenus">
        <ul>
            <li v-for="(item, index) in categories"
                :key="index"
                class="categ-item"
                @mouseenter="showSubMenu(index)">
                {{ item.name }}
                <div class="submenu" v-show="activeIndex === index">
                    <ul>
                        <li v-for="(subItem, subIndex) in item.subItems"
                            :key="subIndex"
                            @mouseenter="showSubSubMenu(subIndex)">
                            {{ subItem.name }}
                            <div class="subsubmenu" v-show="activeSubIndex === subIndex">
                                <ul>
                                    <li v-for="(subSubItem, subSubIndex) in subItem.subSubItems" :key="subSubIndex">
                                        <a href="http://localhost:5173">{{ subSubItem }}</a>
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
    width: 200px;
    left: 200px;
    top: 0;
    background-color: #a9a9a9;
    border: 1px solid #000;
    padding: 10px;
    display: block;
    white-space: nowrap;
    z-index: 10000;
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
    left: 200px;
    top: 0;
    background-color: #e9e9e9;
    border: 1px solid #bbb;
    padding: 10px;
    white-space: nowrap;
    z-index: 20000;
}

.subsubmenu ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.subsubmenu li {
    padding: 5px 0;
}

a {
    text-decoration: none;
    color: black;
}

a:hover {
    text-decoration: underline;
}
</style>
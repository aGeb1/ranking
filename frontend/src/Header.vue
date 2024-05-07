<template>
  <header>
    <h1>ranking</h1>
    <div class="toggle-button" @click="toggleSortType">
      <span :class="{ active: sortType === 'popularity' }">Popularity</span>
      <span>/</span>
      <span :class="{ active: sortType === 'quality' }">Quality</span>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  props: {
    sortBy: Function,
  },
  data() {
    return {
      sortType: 'popularity',
    };
  },
  methods: {
    toggleSortType() {
      this.sortType = this.sortType === 'popularity' ? 'quality' : 'popularity';
      this.sortBy(this.sortType);
    },
  },
};
</script>

<style scoped>
header {
  background-color: #333;
  color: white;
  padding: 20px;
  position: sticky;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 1000;
  display: flex;
  justify-content: space-between;
  align-items: center; /* Vertically center items */
}

.toggle-button {
  display: flex;
  cursor: pointer;
  align-items: center; /* Vertically center items */
}

.toggle-button span {
  margin-right: 10px;
}

.toggle-button .active {
  font-weight: bold;
}
</style>

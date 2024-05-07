<template>
  <div id="app">
    <Header :sortBy="setSortType"/>
    <div class="main-content">
      <RankedList :sortBy="sortBy" />
    </div>
  </div>
</template>

<script>
import Header from './Header.vue';
import RankedList from './RankedList.vue';

export default {
  name: 'App',
  components: {
    Header,
    RankedList,
  },
  data() {
    return {
      sortBy: 'popularity',
    };
  },
  methods: {
    setSortType(sortType) {
      this.sortBy = sortType;
    },
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  margin: 80px;
  height: 100%;
}
</style>

<template>
  <div id="app">
    <Header />
    <div class="main-content">
      <RankedList />
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
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  margin: 80px;
  height: 100%;
}
</style>

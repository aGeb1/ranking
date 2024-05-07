<template>
  <div class="item">
    <div class="item-content">
      <h3>{{ name }}</h3>
      <p>{{ description }}</p>
      <p>Current Rating: {{ ratingValue.toFixed(2) }}</p>
      <p>{{ ratingCount }} Ratings</p>
    </div>
    <button @click="removeItem">Remove</button>
  </div>
</template>

<script>
export default {
  name: 'RankedItem',
  props: {
    name: String,
    description: String,
    ratingValue: Number,
    ratingCount: Number,
    index: Number,
    remove: Function,
  },
  methods: {
    removeItem() {
      this.remove(this.index);
    },
  },
};
</script>

<style scoped>
.item {
  display: flex;
  align-items: center;
  margin: 10px 0;
}

.item-content {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 8px;
  flex-grow: 1;
}

button {
  margin-left: 10px;
  padding: 8px 16px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #c82333;
}
</style>

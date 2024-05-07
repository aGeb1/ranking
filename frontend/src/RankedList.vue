<template>
  <div>
    <div v-for="(item, index) in items" :key="index">
      <RankedItem :name="item.name" :description="item.description" :ratingValue="item.ratingValue" :ratingCount="item.ratingCount" :index="index" :remove="removeItem" />
    </div>
    <div class="add-item">
      <button @click="showAddItemDialog">Add Item</button>
      <div v-if="showDialog" class="dialog">
        <h3>Add New Item</h3>
        <input type="text" v-model="newItemName" placeholder="Name" />
        <textarea v-model="newItemDescription" placeholder="Description"></textarea>
        <button @click="addItem">Add</button>
        <button @click="hideAddItemDialog">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
import RankedItem from './RankedItem.vue';

export default {
  name: 'RankedList',
  components: {
    RankedItem,
  },
  data() {
    return {
      items: [
        {name: 'Item 1', description: 'what', ratingValue: 0, ratingCount: 0},
        {name: 'Item 2', description: 'wait', ratingValue: 0, ratingCount: 0},
        {name: 'Item 3', description: 'huh', ratingValue: 0, ratingCount: 0}
      ],
      showDialog: false,
      newItemName: '',
      newItemDescription: ''
    };
  },
  methods: {
    showAddItemDialog() {
      this.showDialog = true;
    },
    hideAddItemDialog() {
      this.showDialog = false;
      this.newItemName = '';
      this.newItemDescription = '';
    },
    addItem() {
      if (this.newItemName.trim() && this.newItemDescription.trim()) {
        this.items.push({
          name: this.newItemName,
          description: this.newItemDescription,
          ratingValue: 0,
          ratingCount: 0
        });
        this.hideAddItemDialog();
      } else {
        alert('Please enter a name and description for the new item.');
      }
    },
    removeItem(index) {
      this.items.splice(index, 1);
    },
  },
};
</script>

<style scoped>
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

.add-item {
  display: flex;
  padding: 10px;
  align-items: center;
  justify-content: center;
}

.dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.dialog input,
.dialog textarea {
  display: block;
  margin-bottom: 10px;
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.dialog button {
  margin-top: 10px;
}
</style>
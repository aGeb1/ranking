<template>
  <div>
    <div>
      <RankedItem
        v-for="(item, index) in items"
        :key="index"
        :name="item.name"
        :description="item.description"
        :ratingValue="item.ratingValue"
        :ratingCount="item.ratingCount"
        :index="index"
        :remove="removeItem"
        :rate="updateRating"
      />
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
import axios from 'axios';
import RankedItem from './RankedItem.vue';

export default {
  name: 'RankedList',
  components: {
    RankedItem,
  },
  data() {
    return {
      items: [],
      showDialog: false,
      newItemName: '',
      newItemDescription: ''
    };
  },
  created() {
    this.fetchRankingData();
  },
  methods: {
    fetchRankingData() {
      axios.get('http://localhost:5000/ranking/popularity')
        .then(response => {
          this.items = response.data.items.map((item) => {
            return {
              id: item.id,
              name: item.name,
              description: item.description,
              ratingValue: item.rating_value,
              ratingCount: item.rating_count
            };
          });
        })
        .catch(error => {
          console.error('Error fetching ranking data:', error);
        });
    },
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
        const newItem = {
          name: this.newItemName,
          description: this.newItemDescription,
          ratingValue: 0, // works on page, not with database
          ratingCount: 0, // works on page, not with database
        };
        
        axios.post('http://localhost:5000/upload_item', newItem)
          .then(response => {
            this.items.push({ ...newItem, id: response.data.id });
            this.hideAddItemDialog();
          })
          .catch(error => {
            console.error('Error uploading item:', error);
            alert('Failed to add item. Please try again later.');
          });
      } else {
        alert('Please enter a name and description for the new item.');
      }
    },
    removeItem(index) {
      axios.post('http://localhost:5000/delete_item', { id: this.items[index].id })
        .then(_response => {
          // Remove the item from the list if it was successfully deleted
          this.items.splice(index, 1);
        })
        .catch(error => {
          console.error('Error deleting item:', error);
          alert('Failed to delete item. Please try again later.');
        });
    },
    updateRating(index, newRatingValue, newRatingCount) {
      this.items[index].ratingValue = newRatingValue;
      this.items[index].ratingCount = newRatingCount;
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

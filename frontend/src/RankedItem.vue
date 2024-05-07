<template>
  <div class="item">
    <div class="item-content">
      <div>
        <h3>{{ name }}</h3>
        <p>{{ description }}</p>
      </div>
      <div class="rating-section">
        <div class="rating-text">
          <p>Current Rating: {{ ratingValue.toFixed(2) }}</p>
          <p>{{ ratingCount }} Ratings</p>
        </div>
        <div class="rating-input">
          <form @submit.prevent="submitRating">
            <div>
              <input type="number" v-model.number="newRating" min="1" max="10" step="1" placeholder="Enter your rating (1-10)" required>
            </div>
            <div>
              <button type="submit">Submit Rating</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <button @click="removeItem" class="remove-button">Remove</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RankedItem',
  props: {
    name: String,
    description: String,
    ratingValue: Number,
    ratingCount: Number,
    index: Number,
    id: Number,
    remove: Function,
    rate: Function,
  },
  data() {
    return {
      newRating: 5,
    };
  },
  methods: {
    removeItem() {
      this.remove(this.index);
    },
    submitRating() {
      axios.post('http://localhost:5000/submit_rating',
        {
          rating: this.newRating,
          id: this.id,
        })
        .then(_response => {
          const newRatingValue = (this.ratingValue * this.ratingCount + this.newRating) / (this.ratingCount + 1);
          const newRatingCount = this.ratingCount + 1;
          this.rate(this.index, newRatingValue, newRatingCount);
          this.newRating = 5;
        })
        .catch(error => {
          console.error('Error submitting rating:', error);
          alert('Failed to add rating. Please try again later.');
        });
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
  display: flex;
  justify-content: space-between; /* Align children at each end of the container */
}

.rating-section {
  display: flex;
  flex-direction: column; /* Stack children vertically */
}

.rating-text {
  margin-bottom: 10px; /* Add some spacing between the rating text and input */
}

.rating-input {
  display: flex;
  flex-direction: column; /* Stack children vertically */
}

.remove-button {
  margin-left: 10px;
}

button {
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

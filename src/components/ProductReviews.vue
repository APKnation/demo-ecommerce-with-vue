<template>
  <div class="product-reviews">
    <div class="reviews-header">
      <h3 class="reviews-title">Customer Reviews</h3>
      <div class="reviews-summary">
        <div class="rating-summary">
          <div class="rating-number">{{ averageRating }}</div>
          <div class="rating-stars">
            <span v-for="i in 5" :key="i" class="star" :class="{ 'filled': i <= averageRating }">★</span>
          </div>
          <div class="rating-count">{{ reviews.length }} reviews</div>
        </div>
        <button @click="showReviewForm = true" class="write-review-btn">
          Write a Review
        </button>
      </div>
    </div>
    
    <!-- Review Form Modal -->
    <div v-if="showReviewForm" class="review-modal">
      <div class="modal-content">
        <div class="modal-header">
          <h4>Write Your Review</h4>
          <button @click="showReviewForm = false" class="close-btn">×</button>
        </div>
        <div class="modal-body">
          <div class="form-group">
            <label>Rating</label>
            <div class="rating-input">
              <span 
                v-for="i in 5" 
                :key="i"
                @click="newReview.rating = i"
                class="star-input"
                :class="{ 'filled': i <= newReview.rating }"
              >
                ★
              </span>
            </div>
          </div>
          <div class="form-group">
            <label>Your Name</label>
            <input v-model="newReview.name" type="text" class="form-input" placeholder="Enter your name">
          </div>
          <div class="form-group">
            <label>Review Title</label>
            <input v-model="newReview.title" type="text" class="form-input" placeholder="Summarize your experience">
          </div>
          <div class="form-group">
            <label>Your Review</label>
            <textarea v-model="newReview.content" class="form-textarea" rows="4" placeholder="Share your experience with this product"></textarea>
          </div>
        </div>
        <div class="modal-footer">
          <button @click="submitReview" class="submit-btn">Submit Review</button>
        </div>
      </div>
    </div>
    
    <!-- Reviews List -->
    <div class="reviews-list">
      <div v-if="reviews.length === 0" class="no-reviews">
        <p>No reviews yet. Be the first to review this product!</p>
      </div>
      
      <div v-else class="reviews-grid">
        <div v-for="review in displayedReviews" :key="review.id" class="review-card">
          <div class="review-header">
            <div class="reviewer-info">
              <div class="reviewer-name">{{ review.name }}</div>
              <div class="review-date">{{ formatDate(review.date) }}</div>
            </div>
            <div class="review-rating">
              <span v-for="i in 5" :key="i" class="star" :class="{ 'filled': i <= review.rating }">★</span>
            </div>
          </div>
          <div class="review-content">
            <h5 class="review-title">{{ review.title }}</h5>
            <p class="review-text">{{ review.content }}</p>
          </div>
          <div class="review-actions">
            <button class="helpful-btn" @click="markHelpful(review.id)">
              Helpful ({{ review.helpful || 0 }})
            </button>
          </div>
        </div>
      </div>
      
      <!-- Load More Button -->
      <div v-if="hasMoreReviews" class="load-more">
        <button @click="loadMoreReviews" class="load-more-btn">
          Load More Reviews
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'

export default {
  name: 'ProductReviews',
  props: {
    productId: {
      type: String,
      required: true
    },
    reviews: {
      type: Array,
      default: () => []
    }
  },
  setup(props) {
    const showReviewForm = ref(false)
    const newReview = ref({
      rating: 5,
      name: '',
      title: '',
      content: ''
    })
    const displayedReviews = ref([])
    const reviewsPerPage = 5
    const currentPage = ref(1)
    
    // Sample reviews if none provided
    const sampleReviews = [
      {
        id: 1,
        name: 'John Doe',
        rating: 5,
        title: 'Excellent Product!',
        content: 'This product exceeded my expectations. Great quality and fast delivery.',
        date: new Date('2024-01-15'),
        helpful: 12
      },
      {
        id: 2,
        name: 'Jane Smith',
        rating: 4,
        title: 'Good Value',
        content: 'Very happy with my purchase. The product works as described.',
        date: new Date('2024-01-10'),
        helpful: 8
      },
      {
        id: 3,
        name: 'Mike Johnson',
        rating: 5,
        title: 'Highly Recommended',
        content: 'Amazing quality and customer service. Would definitely buy again.',
        date: new Date('2024-01-05'),
        helpful: 15
      }
    ]
    
    const allReviews = computed(() => {
      return props.reviews.length > 0 ? props.reviews : sampleReviews
    })
    
    const averageRating = computed(() => {
      if (allReviews.value.length === 0) return 0
      const total = allReviews.value.reduce((sum, review) => sum + review.rating, 0)
      return (total / allReviews.value.length).toFixed(1)
    })
    
    const hasMoreReviews = computed(() => {
      return displayedReviews.value.length < allReviews.value.length
    })
    
    const loadInitialReviews = () => {
      displayedReviews.value = allReviews.value.slice(0, reviewsPerPage)
      currentPage.value = 1
    }
    
    const loadMoreReviews = () => {
      const nextPage = currentPage.value + 1
      const startIndex = (nextPage - 1) * reviewsPerPage
      const endIndex = startIndex + reviewsPerPage
      
      displayedReviews.value = [
        ...displayedReviews.value,
        ...allReviews.value.slice(startIndex, endIndex)
      ]
      currentPage.value = nextPage
    }
    
    const submitReview = () => {
      if (!newReview.value.name || !newReview.value.title || !newReview.value.content) {
        alert('Please fill in all fields')
        return
      }
      
      const review = {
        id: Date.now(),
        ...newReview.value,
        date: new Date(),
        helpful: 0
      }
      
      allReviews.value.unshift(review)
      loadInitialReviews()
      
      // Reset form
      newReview.value = {
        rating: 5,
        name: '',
        title: '',
        content: ''
      }
      showReviewForm.value = false
    }
    
    const markHelpful = (reviewId) => {
      const review = allReviews.value.find(r => r.id === reviewId)
      if (review) {
        review.helpful = (review.helpful || 0) + 1
      }
    }
    
    const formatDate = (date) => {
      return new Date(date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
    
    onMounted(() => {
      loadInitialReviews()
    })
    
    return {
      showReviewForm,
      newReview,
      displayedReviews,
      averageRating,
      hasMoreReviews,
      loadMoreReviews,
      submitReview,
      markHelpful,
      formatDate
    }
  }
}
</script>

<style scoped>
.product-reviews {
  @apply space-y-6;
}

.reviews-header {
  @apply flex justify-between items-start mb-8;
}

.reviews-title {
  @apply text-2xl font-bold text-gray-900;
}

.reviews-summary {
  @apply flex items-center gap-6;
}

.rating-summary {
  @apply text-center;
}

.rating-number {
  @apply text-3xl font-bold text-gray-900;
}

.rating-stars {
  @apply flex justify-center my-1;
}

.star {
  @apply text-2xl text-gray-300;
}

.star.filled {
  @apply text-yellow-400;
}

.rating-count {
  @apply text-sm text-gray-600;
}

.write-review-btn {
  @apply px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors;
}

.review-modal {
  @apply fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50;
}

.modal-content {
  @apply bg-white rounded-lg p-6 max-w-md w-full mx-4;
}

.modal-header {
  @apply flex justify-between items-center mb-4;
}

.modal-header h4 {
  @apply text-lg font-semibold text-gray-900;
}

.close-btn {
  @apply text-gray-400 hover:text-gray-600 text-2xl font-bold;
}

.modal-body {
  @apply space-y-4;
}

.form-group {
  @apply space-y-2;
}

.form-group label {
  @apply block text-sm font-medium text-gray-700;
}

.form-input, .form-textarea {
  @apply w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent;
}

.rating-input {
  @apply flex gap-2;
}

.star-input {
  @apply text-2xl text-gray-300 cursor-pointer hover:text-yellow-400 transition-colors;
}

.star-input.filled {
  @apply text-yellow-400;
}

.modal-footer {
  @apply mt-6;
}

.submit-btn {
  @apply w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors;
}

.reviews-list {
  @apply space-y-6;
}

.no-reviews {
  @apply text-center py-8 text-gray-500;
}

.reviews-grid {
  @apply space-y-4;
}

.review-card {
  @apply bg-gray-50 rounded-lg p-6;
}

.review-header {
  @apply flex justify-between items-start mb-4;
}

.reviewer-info {
  @apply space-y-1;
}

.reviewer-name {
  @apply font-semibold text-gray-900;
}

.review-date {
  @apply text-sm text-gray-600;
}

.review-content {
  @apply space-y-2;
}

.review-title {
  @apply font-medium text-gray-900;
}

.review-text {
  @apply text-gray-700;
}

.review-actions {
  @apply mt-4;
}

.helpful-btn {
  @apply text-sm text-blue-600 hover:text-blue-700;
}

.load-more {
  @apply text-center;
}

.load-more-btn {
  @apply px-6 py-2 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition-colors;
}
</style>

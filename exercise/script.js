// Get elements
const nameInput = document.getElementById('name');
const feedbackInput = document.getElementById('feedback');
const charCountDisplay = document.getElementById('charCount');
const reviewForm = document.getElementById('reviewForm');
const thankYouMsg = document.getElementById('thankYou');
const reviewDetails = document.getElementById('reviewDetails');
const starsContainer = document.getElementById('stars');

let selectedRating = 0;

// Dynamically generate 5 stars
for (let i = 1; i <= 5; i++) {
  const star = document.createElement('span');
  star.innerHTML = '☆';
  star.setAttribute('data-rating', i);
  star.classList.add('star');
  starsContainer.appendChild(star);
}

// Highlight stars on click
starsContainer.addEventListener('click', (e) => {
  if (e.target.classList.contains('star')) {
    selectedRating = parseInt(e.target.getAttribute('data-rating'));
    updateStarDisplay();
  }
});

function updateStarDisplay() {
  document.querySelectorAll('.star').forEach(star => {
    const rating = parseInt(star.getAttribute('data-rating'));
    star.innerHTML = rating <= selectedRating ? '★' : '☆';
    star.style.color = rating <= selectedRating ? '#fbbf24' : '#6b7280';
  });
}

// Live character count
feedbackInput.addEventListener('keyup', () => {
  charCountDisplay.textContent = feedbackInput.value.length;
});

// Form submission
reviewForm.addEventListener('submit', (e) => {
  e.preventDefault();

  if (!nameInput.value.trim() || !feedbackInput.value.trim() || selectedRating === 0) {
    alert('Please fill all required fields and select a rating!');
    return;
  }

  const reviewData = {
    name: nameInput.value.trim(),
    feedback: feedbackInput.value.trim(),
    rating: selectedRating,
    timestamp: new Date().toLocaleString()
  };

  localStorage.setItem('lastReview', JSON.stringify(reviewData));

  showThankYou();
  displayLastReview();
  resetForm();
});

// Thank you message
function showThankYou() {
  thankYouMsg.classList.remove('hidden');
  setTimeout(() => thankYouMsg.classList.add('hidden'), 3000);
}

// Show last submitted review
function displayLastReview() {
  const savedReview = JSON.parse(localStorage.getItem('lastReview'));
  if (savedReview) {
    reviewDetails.innerHTML = `
      <p><strong>Name:</strong> ${savedReview.name}</p>
      <p><strong>Feedback:</strong> ${savedReview.feedback}</p>
      <p><strong>Rating:</strong> ${'★'.repeat(savedReview.rating)}${'☆'.repeat(5 - savedReview.rating)}</p>
      <p class="text-sm text-gray-500"><em>Submitted on ${savedReview.timestamp}</em></p>
    `;
  }
}

// Reset the form
function resetForm() {
  nameInput.value = '';
  feedbackInput.value = '';
  charCountDisplay.textContent = '0';
  selectedRating = 0;
  updateStarDisplay();
}

// Display last review on page load
window.addEventListener('DOMContentLoaded', displayLastReview);

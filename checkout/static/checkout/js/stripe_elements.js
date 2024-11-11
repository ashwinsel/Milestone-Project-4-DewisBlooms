// Get Stripe public key and client secret from the rendered template
const stripePublicKey = $("#stripePublicKey").text().slice(1, -1);
const clientSecret = $("#clientSecret").text().slice(1, -1);

// Initialize Stripe and Elements
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// Define styling for Stripe Elements
const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create a card element and mount it to the DOM
const card = elements.create('card', { style: style });
card.mount('#card-element');

// Display card error messages
card.on('change', (event) => {
    const errorDisplay = document.getElementById('card-errors');
    if (event.error) {
        errorDisplay.textContent = event.error.message;
    } else {
        errorDisplay.textContent = '';
    }
});
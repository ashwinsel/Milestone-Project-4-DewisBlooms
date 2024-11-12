// Retrieve the public key and client secret, stripping out extra quotes if needed.
const stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
const clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

// Initialize Stripe and Elements using the public key and client secret.
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements({
    clientSecret: clientSecret,  // Ensure clientSecret format as `${id}_secret_${secret}`
    appearance: { theme: 'night' }
});

// Define card style and create a card element
const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': { color: '#aab7c4' }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

const card = elements.create('card', { style });
card.mount('#card-element');

// Handle changes and errors on card element
card.on('change', (event) => {
    const errorDisplay = document.getElementById('card-errors');
    if (event.error) {
        errorDisplay.textContent = event.error.message;
    } else {
        errorDisplay.textContent = '';
    }
});
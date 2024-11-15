document.addEventListener('DOMContentLoaded', function () {
    const stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
    const clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

    const stripe = Stripe(stripePublicKey);
    const elements = stripe.elements();

    const style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': { color: '#aab7c4' }
        },
        invalid: { color: '#dc3545', iconColor: '#dc3545' }
    };

    const card = elements.create('card', { style: style });
    card.mount('#card-element');

    card.on('change', (event) => {
        const errorDisplay = document.getElementById('card-errors');
        errorDisplay.textContent = event.error ? event.error.message : '';
    });

    const form = document.getElementById('payment-form');
    form.addEventListener('submit', function (ev) {
        ev.preventDefault();
        card.update({ 'disabled': true });
        $('#submit-button').attr('disabled', true);

        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        const saveInfo = Boolean($('#id-save-info').attr('checked'));

        $.post('/checkout/cache_checkout_data/', {
            csrfmiddlewaretoken: csrfToken,
            client_secret: clientSecret,
            save_info: saveInfo,
        }).done(function () {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        email: $.trim(form.email.value),
                        address: {
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            state: $.trim(form.county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        postal_code: $.trim(form.postcode.value),
                        state: $.trim(form.county.value),
                    }
                }
            }).then((result) => {
                if (result.error) {
                    $('#card-errors').text(result.error.message);
                    card.update({ 'disabled': false });
                    $('#submit-button').attr('disabled', false);
                } else if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            });
        }).fail(() => location.reload());
    });
});
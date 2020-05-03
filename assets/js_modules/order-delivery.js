window.addEventListener('DOMContentLoaded', () => {
    if (document.getElementsByClassName('order-delivery__vehisles-list')[0]) {
        let vehisles = document.getElementsByClassName('order-delivery__vehisle'),
            priceMultiplier = parseFloat(document.getElementById('order-delivery__price-multiplier').textContent);

        for (let i = 0; i < vehisles.length; i++) {
            let vehisle = vehisles[i];

            let pricePerKm = parseInt(vehisle.getElementsByClassName('order-delivery__price-per-km')[0].textContent),
                pricePerUse = parseInt(vehisle.getElementsByClassName('order-delivery__price-per-use')[0].textContent),
                pathLength = parseInt(document.getElementById('order-delivery__path-length').textContent);

            let cost = priceMultiplier * ((pathLength * pricePerKm) + pricePerUse);

            vehisle.getElementsByClassName('order-delivery__delivery-cost')[0].textContent = cost + '$';
        }
    }
});
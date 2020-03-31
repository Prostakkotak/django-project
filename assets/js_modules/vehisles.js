var filtersOpenButton = document.getElementById('filters__open-button'),
    filtersForm = document.getElementById('filters__form');

filtersOpenButton.addEventListener('click', function() {
    filtersOpenButton.classList.toggle('open')
    filtersForm.classList.toggle('open')
})
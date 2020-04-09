export default function connectFiltersButton(obj) {
    obj.filtersOpenButton.addEventListener('click', function () {
        obj.filtersOpenButton.classList.toggle('open');
        obj.filtersForm.classList.toggle('open');
    });
}
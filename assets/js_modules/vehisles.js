import connectFiltersButton from './filters';

let vehislesFilters = {
    filtersOpenButton: document.getElementById('filters__button_open'),
    filtersForm: document.getElementById('filters__form')
};

connectFiltersButton(vehislesFilters);
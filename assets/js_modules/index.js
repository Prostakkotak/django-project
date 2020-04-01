import createAnimatedSlider from './animated-slider'
import createSlider from './slider'

let fleetGallery = {
    container: document.getElementById('fleet-gallery'),
    list: document.getElementById('fleet-gallery__slider-list'),
    items: document.getElementsByClassName('fleet-gallery__slider-item'),
    leftButton: document.getElementById('fleet-gallery__slider-button_left'),
    rightButton: document.getElementById('fleet-gallery__slider-button_right')
}

var headerSlider = {
    container: document.getElementById('slider'),
    list: document.getElementById('slider__list'),
    items: document.getElementsByClassName('slider__item'),
    rightButton: document.getElementById('slider__button')
}

createAnimatedSlider(headerSlider)
createSlider(fleetGallery)
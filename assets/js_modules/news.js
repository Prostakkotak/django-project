import createSlider from './slider'

let importantNews = {
    container: document.getElementById('important-news'),
    list: document.getElementById('important-news__list'),
    items: document.getElementsByClassName('important-news__item'),
    rightButton: document.getElementById('important-news__button_right')
}

createSlider(importantNews)
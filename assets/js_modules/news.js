import createSlider from './slider';
import connectTagsButton from './tags'

let importantNews = {
    container: document.getElementById('important-news'),
    list: document.getElementById('important-news__list'),
    items: document.getElementsByClassName('important-news__item'),
    rightButton: document.getElementById('important-news__button_right')
};

let tags = {
    tagsOpenButton: document.getElementById('tags__open-button'),
    tagsList: document.getElementById('tags__list')
};

connectTagsButton(tags);
createSlider(importantNews);
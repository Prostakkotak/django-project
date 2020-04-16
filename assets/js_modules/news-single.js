import deleteConfirmationPopUp from './delete-confirmation';

deleteConfirmationPopUp(document.getElementById('delete-pop-up__link_news'), 'news');

let comments = document.getElementsByClassName('news-comments__item-delete');

for (let i = 0; i < comments.length; i++) {
    deleteConfirmationPopUp(comments[i], 'comment');
}
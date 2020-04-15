import deleteConfirmationPopUp from './delete-confirmation';

let newsDelete = {
    container: document.getElementById('delete-pop-up_news'),
    link: document.getElementById('delete-pop-up__link_news'),
    cancelButton: document.getElementById('delete-pop-up__cancel_news')
};

deleteConfirmationPopUp(newsDelete);
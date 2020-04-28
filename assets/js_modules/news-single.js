import deleteConfirmationPopUp from './delete-confirmation';

deleteConfirmationPopUp(document.getElementById('delete-pop-up__link_news'), 'news');


let commentsList = document.getElementsByClassName('news-comments__item'),
    answersList = document.getElementsByClassName('news-comments__item_answer');

for (let i = 0; i < answersList.length; i++) {
    answersList[i].classList.remove('hidden');
    let tempAnswer = answersList[i].cloneNode(true);

    for (let k = 0; k < commentsList.length; k++) {
        if (
            commentsList[k].getElementsByClassName('news-comments__comment-id')[0].textContent ==
            answersList[i].getElementsByClassName('news-comments__answer-id')[0].textContent
        ) {
            answersList[i].remove();
            commentsList[k].getElementsByClassName('news-comments__answers-list')[0].appendChild(tempAnswer);
            commentsList = document.getElementsByClassName('news-comments__item');
            break;
        }
    }
}

let commentsDeleteLinks = document.getElementsByClassName('news-comments__link_delete');

for (let i = 0; i < commentsDeleteLinks.length; i++) {
    deleteConfirmationPopUp(commentsDeleteLinks[i], 'comment');
}

let commentCreationForm = document.getElementById('comment-create-form'),
    messageInputHeader = document
        .getElementsByClassName('news-comments__input-block_message')[0]
        .getElementsByClassName('news-comments__input-name')[0];

document.getElementsByClassName('news-comments__list')[0].addEventListener('click', (e) => {
    let target = e.target;

    while (target != this) {
        if (target.classList.contains('news-comments__link_answer')) {
            let userID = target.getElementsByClassName('news-comments__user-id')[0].textContent;

            let answerInput = document.createElement('input');
            answerInput.classList.add('news-comments__answer-input');
            answerInput.hidden = true;
            answerInput.name = 'answer';
            answerInput.value = userID;

            let answerTitle = 'Message to ' + target.getElementsByClassName('news-comments__answer-target')[0].textContent;

            if (commentCreationForm.getElementsByClassName('news-comments__answer-input')[0]) {
                commentCreationForm.getElementsByClassName('news-comments__answer-input')[0].remove();
            }

            commentCreationForm.appendChild(answerInput);

            messageInputHeader.textContent = answerTitle;
            messageInputHeader.classList.add('news-comments__input-name_cancel');
            messageInputHeader.title = 'Cancel?';

            messageInputHeader.addEventListener('click', () => {
                messageInputHeader.classList.remove('news-comments__input-name_cancel');
                messageInputHeader.textContent = 'Message';
                messageInputHeader.title = '';

                commentCreationForm.getElementsByClassName('news-comments__answer-input')[0].remove();
            });
        }

        target = target.parentNode;
    }

})
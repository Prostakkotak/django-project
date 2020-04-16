export default function deleteConfirmationPopUp(link, deleteObjName) {
    document.addEventListener('DOMContentLoaded', () => {

        if (!document.getElementById('body-shadow')) {
            let bodyShadow = document.createElement('div');

            bodyShadow.classList.add('body-shadow');
            bodyShadow.id = 'body-shadow';

            wrapper.appendChild(bodyShadow);
        }

        link.addEventListener('click', (e) => {
            let evt = e ? e : window.event;

            (evt.preventDefault) ? evt.preventDefault() : evt.returnValue = false;

            let popUp = document.createElement('div'),
                confirmButton = document.createElement('a'),
                cancelButton = document.createElement('div'),
                deleteWarning = document.createElement('div');

            popUp.id = 'delete-pop-up';
            popUp.classList.add('delete-pop-up');

            confirmButton.classList.add('delete-pop-up__confirmation');
            confirmButton.href = link.href;
            confirmButton.textContent = 'Yes';

            cancelButton.id = 'delete-cancel';
            cancelButton.classList.add('delete-pop-up__cancel');
            cancelButton.textContent = 'Cancel';

            deleteWarning.classList.add('delete-pop-up__warning');
            deleteWarning.textContent = `Are you sure you want to delete ${deleteObjName}?`;

            popUp.append(deleteWarning, confirmButton, cancelButton);
            document.getElementsByClassName('wrapper')[0].append(popUp);

            document.getElementById('body-shadow').classList.add('active');

            cancelButton.addEventListener('click', () => {
                popUp.remove();
                document.getElementById('body-shadow').classList.remove('active');
            });
        });
    });
}
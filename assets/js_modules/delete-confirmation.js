export default function deleteConfirmationPopUp(obj) {
    document.addEventListener('DOMContentLoaded', () => {
        obj.link.addEventListener('click', (e) => {
            obj.container.classList.remove('hidden');

            if (!document.getElementById('body-shadow')) {
                let bodyShadow = document.createElement('div');

                bodyShadow.classList.add('body-shadow');
                bodyShadow.id = 'body-shadow';

                wrapper.appendChild(bodyShadow);
                bodyShadow = document.getElementById('body-shadow');

                bodyShadow.classList.toggle('active');
            } else {
                document.getElementById('body-shadow').classList.toggle('active');
            }
        });

        obj.cancelButton.addEventListener('click', (e) => {
            obj.container.classList.add('hidden');
            document.getElementById('body-shadow').classList.remove('active');
        });
    })
}
export default function connectTagsButton(obj) {
    obj.tagsOpenButton.addEventListener('click', () => {
        obj.tagsOpenButton.classList.toggle('open');
        obj.tagsList.classList.toggle('open');
    });
}
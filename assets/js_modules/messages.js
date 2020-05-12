// Удаляем появившиеся сообения после заполнения формы и т.д.
if (document.getElementById('messages')) {
    setTimeout(function () {
        document.getElementById('messages').remove();
    }, 5000);
}
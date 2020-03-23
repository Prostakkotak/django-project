let trigram = document.getElementById('trigram');

let bodyShadow = document.createElement('div');
bodyShadow.classList.add('body-shadow');
bodyShadow.id = 'body-shadow';

document.getElementsByClassName('wrapper')[0].appendChild(bodyShadow);

bodyShadow = document.getElementById('body-shadow');

document.getElementById('header').onclick = function(e) {

    target = e.target

    while (target != this) {

        if (target == trigram) {
            trigram.classList.toggle('open')
            document.getElementsByClassName('nav')[0].classList.toggle('open');
            document.getElementsByClassName('header__options')[0].classList.toggle('open');
            bodyShadow.classList.toggle('active');
        }

        target = target.parentNode;
    }
}

addEventListener('resize', function () {
    if (document.body.offsetWidth >= 750) {
        if (bodyShadow.classList.contains('active')) {
            bodyShadow.classList.remove('active');
        }
    } else {
        if (trigram.classList.contains('open')) {
            bodyShadow.classList.add('active');
        }
    }
})
let trigram = document.getElementById('trigram'),
    header = document.getElementById('header'),
    bodyShadow = document.createElement('div');

let wrapper = document.getElementsByClassName('wrapper')[0];

if (document.body.offsetWidth <= 750) {
    wrapper.style.marginTop = header.offsetHeight + 'px';
}

bodyShadow.classList.add('body-shadow');
bodyShadow.id = 'body-shadow';

wrapper.appendChild(bodyShadow);

bodyShadow = document.getElementById('body-shadow');

trigram.addEventListener('click', () => {
    trigram.classList.toggle('open');
    document.getElementsByClassName('nav')[0].classList.toggle('open');
    document.getElementsByClassName('header__options')[0].classList.toggle('open');
    bodyShadow.classList.toggle('active');
});

addEventListener('resize', () => {
    if (document.body.offsetWidth >= 750) {

        wrapper.style.marginTop = '';

        if (bodyShadow.classList.contains('active')) {
            bodyShadow.classList.remove('active');
        }
    } else {

        wrapper.style.marginTop = header.offsetHeight + 'px';

        if (trigram.classList.contains('open')) {
            bodyShadow.classList.add('active');
        }
    }
});
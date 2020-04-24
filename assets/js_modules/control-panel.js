let controlMenu = document.getElementById('control-panel__menu');

let blockList = document.getElementsByClassName('control-panel__block'),
    controlMenuItems = controlMenu.getElementsByClassName('control-panel__item');

controlMenuItems[0].classList.add('current');

// Отображаем самый первый элемент из меню при загрузке страницы
for (let i = 0; i < blockList.length; i++) {
    if (blockList[i].getAttribute('data-model-name') == controlMenuItems[0].getAttribute('data-model-name')) {
        blockList[i].classList.add('current');
    } else {
        blockList[i].classList.remove('current');
    }
}

/*
 * Берем стили блоков управления и рассчитываем
 * минимальную высоту(минимальная высота=высота менюшки) учитывая внутренние отступы
 */
let blockListStyles = window.getComputedStyle(blockList[0]),
    minBlockHeight = (
        controlMenu.offsetHeight - parseInt(blockListStyles.paddingBottom) - parseInt(blockListStyles.paddingTop)
    );

controlMenu.addEventListener('click', (e) => {
    let target = e.target;

    while (target != this) {

        if (target.classList.contains('control-panel__item')) {
            if (!target.classList.contains('current')) {

                /*
                 * Удаление current со всех элементов и добавление 
                 * current к указанному пункту меню и соответствующему блоку управления
                 */
                for (let i = 0; i < controlMenuItems.length; i++) {
                    controlMenuItems[i].classList.remove('current');

                    if (blockList[i].getAttribute('data-model-name') == target.getAttribute('data-model-name')) {
                        blockList[i].classList.add('current');
                    } else {
                        blockList[i].classList.remove('current');
                    }
                }

                target.classList.add('current');
            }
        }

        target = target.parentNode;
    }
})


// Вешаем обработчики для раскрывающихся списков с моделями
for (let i = 0; i < blockList.length; i++) {

    blockList[i].style.minHeight = minBlockHeight + 'px';

    let modelsList = blockList[i].getElementsByClassName('models-list')[0],
        modelsListButton = blockList[i].getElementsByClassName('models-list__button')[0];

    modelsListButton.addEventListener('click', () => {
        blockList[i].getElementsByClassName('models-list__header')[0].classList.toggle('open');
        modelsList.classList.toggle('open');
    });
}
export default function createAnimatedSlider(obj) {
    if (obj.items.length != 1) {

        for (let i = 0; i <= obj.items.length - 1; i++) {
            if (i != 0) {
                obj.items[i].getElementsByClassName('slider__text')[0].classList.add('shadowed');
            }
        }

        let itemWidth = obj.items[0].offsetWidth;

        let betweenElemsDistance = Math.abs(obj.items[0].offsetLeft + obj.items[0].offsetWidth - obj.items[1].offsetLeft);

        let maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance),
            currentScrollWidth = 0;

        obj.container.onclick = (e) => {
            let target = e.target;

            while (target != this && !obj.list.classList.contains('on-scroll')) {
                if (target == obj.rightButton) {
                    if (currentScrollWidth > maxScrollWidth) {

                        let currentItem = Math.floor(-currentScrollWidth / itemWidth); // Вычисления номера слайда отображаемого на экране

                        obj.items[currentItem].getElementsByClassName('slider__text')[0].classList.add('shadowed');
                        obj.rightButton.classList.add('shadowed');

                        obj.list.classList.add('on-scroll');

                        setTimeout(() => {
                            currentScrollWidth =
                                currentScrollWidth - obj.items[0].offsetWidth - betweenElemsDistance;
                            obj.list.style.marginLeft = currentScrollWidth + "px";

                            setTimeout(() => {
                                obj.items[currentItem + 1].getElementsByClassName('slider__text')[0].classList.remove('shadowed');
                                obj.rightButton.classList.remove('shadowed');
                                obj.list.classList.remove('on-scroll');
                            }, 700);
                        }, 700);
                    } else {
                        obj.items[obj.items.length - 1].getElementsByClassName('slider__text')[0].classList.add('shadowed');
                        obj.rightButton.classList.add('shadowed');
                        obj.list.classList.add('on-scroll');

                        setTimeout(() => {
                            currentScrollWidth = 0;
                            obj.list.style.marginLeft = currentScrollWidth + 'px';

                            setTimeout(() => {
                                obj.items[0].getElementsByClassName('slider__text')[0].classList.remove('shadowed');
                                obj.rightButton.classList.remove('shadowed');
                                obj.list.classList.remove('on-scroll');
                            }, 700);
                        }, 700);
                    }
                }

                target = target.parentNode; // Чтобы функция не повесила всю страницу
            }
        };

        addEventListener("resize", () => {
            let currentItem = Math.floor(-currentScrollWidth / itemWidth); // Вычисления номера слайда отображаемого на экране

            if (currentItem > 0) {
                /* Если это не самый первый слайд, то идет перерасчет ширины прокрути для новой ширины окна браузера */
                currentScrollWidth = -((obj.items[0].offsetWidth + betweenElemsDistance) * currentItem);
            } else { currentScrollWidth = 0; }

            obj.list.style.marginLeft = currentScrollWidth + "px"; // Возврат к стартовой точке
            maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance); // Перерасчет максимальной ширины прокрутки
            itemWidth = obj.items[0].offsetWidth; // Запоминаем новую текущую ширину одного слайда
        });
    }
}
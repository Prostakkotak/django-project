export default function createSlider(obj) {
    if (obj.items.length != 1) {
        let itemWidth = obj.items[0].offsetWidth;

        let betweenElemsDistance = Math.abs(obj.items[0].offsetLeft + obj.items[0].offsetWidth - obj.items[1].offsetLeft);

        let maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance),
            currentScrollWidth = 0;

        let sliderTouchStart = 0,
            sliderTouchEnd = 0;

        obj.list.addEventListener('touchstart', function (e) {
            sliderTouchStart = e.changedTouches[0].screenX;
        });

        obj.list.addEventListener('touchend', function (e) {
            sliderTouchEnd = e.changedTouches[0].screenX;

            if (Math.abs(sliderTouchStart - sliderTouchEnd) >= 20) { // Чтобы нажатие на ссылки и т.д. в слайде не засчитывались как свайпы
                if (sliderTouchEnd > sliderTouchStart) scrollLeft();
                else if (sliderTouchEnd < sliderTouchStart) scrollRight();
            }
        });

        obj.container.addEventListener('click', function (e) {
            let target = e.target;

            while (target != this) {
                if (target == obj.rightButton) { scrollRight(); }
                else if (target == obj.leftButton) { scrollLeft(); }

                target = target.parentNode;
            }
        });

        addEventListener("resize", function () {
            let currentItem = Math.floor(-currentScrollWidth / itemWidth); // Вычисления номера слайда отображаемого на экране

            if (currentItem > 0) {
                /* Если это не самый первый слайд, то идет перерасчет ширины прокрутки для новой ширины окна браузера */
                currentScrollWidth = -((obj.items[0].offsetWidth + betweenElemsDistance) * currentItem);
            } else { currentScrollWidth = 0; }

            obj.list.style.marginLeft = currentScrollWidth + "px"; // Перемещение на новую точку после перерасчета
            maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance); // Перерасчет максимальной ширины прокрутки
            itemWidth = obj.items[0].offsetWidth; // Запоминаем новую текущую ширину одного слайда
        });

        let scrollLeft = function() {
            if (currentScrollWidth < 0) {
                let currentItem = Math.floor(-currentScrollWidth / itemWidth);

                currentScrollWidth =
                    currentScrollWidth + itemWidth + betweenElemsDistance;
                obj.list.style.marginLeft = currentScrollWidth + 'px';
            } else {
                currentScrollWidth = maxScrollWidth;
                obj.list.style.marginLeft = currentScrollWidth + 'px';
            }
        };

        let scrollRight = function() {
            if (currentScrollWidth > maxScrollWidth) {
                let currentItem = Math.floor(-currentScrollWidth / itemWidth);

                currentScrollWidth =
                    currentScrollWidth - itemWidth - betweenElemsDistance;
                obj.list.style.marginLeft = currentScrollWidth + "px";
            } else {
                currentScrollWidth = 0;
                obj.list.style.marginLeft = currentScrollWidth + 'px';
            }
        };
    }
}
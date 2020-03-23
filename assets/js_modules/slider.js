export default function createSlider(obj) {
    if (obj.items.length != 1) {

        if (!obj.leftButton) obj.leftButton = '';
        if (!obj.rightButton) obj.rightButton = '';

        let itemWidth = obj.items[0].offsetWidth

        let betweenElemsDistance = Math.abs(obj.items[0].offsetLeft + obj.items[0].offsetWidth - obj.items[1].offsetLeft);

        let maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance);
        let currentScrollWidth = 0;

        obj.container.onclick = function (e) {
            let target = e.target;

            while (target != this) {
                if (target == obj.rightButton) {
                    if (currentScrollWidth > maxScrollWidth) {
                        let currentItem = Math.floor(-currentScrollWidth / itemWidth);

                        currentScrollWidth =
                            currentScrollWidth - itemWidth - betweenElemsDistance;
                        obj.list.style.marginLeft = currentScrollWidth + "px";
                    } else {
                        currentScrollWidth = 0;
                        obj.list.style.marginLeft = currentScrollWidth + 'px';
                    }
                } else if (target == obj.leftButton) {
                    if (currentScrollWidth < 0) {
                        let currentItem = Math.floor(-currentScrollWidth / itemWidth);

                        currentScrollWidth =
                            currentScrollWidth + itemWidth + betweenElemsDistance;
                        obj.list.style.marginLeft = currentScrollWidth + 'px';
                    } else {
                        currentScrollWidth = maxScrollWidth;
                        obj.list.style.marginLeft = currentScrollWidth + 'px';
                    }
                }

                target = target.parentNode;
            }
        }

        addEventListener("resize", function () {
            let currentItem = Math.floor(-currentScrollWidth / itemWidth); // Вычисления номера слайда отображаемого на экране

            if (currentItem > 0) {
                // Если это не самый первый слайд, то идет перерасчет ширины прокрутки для новой ширины окна браузера
                currentScrollWidth = -((obj.items[0].offsetWidth + betweenElemsDistance) * currentItem);
            } else {
                currentScrollWidth = 0;
            }

            obj.list.style.marginLeft = currentScrollWidth + "px"; // Перемещение на новую точку после перерасчета
            maxScrollWidth = (obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance;
            maxScrollWidth = -maxScrollWidth; // Перерасчет максимальной ширины прокрутки
            itemWidth = obj.items[0].offsetWidth; // Запоминаем новую текущую ширину одного слайда
        });
    }
}
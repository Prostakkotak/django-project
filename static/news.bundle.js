/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 1);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./js_modules/header.js":
/*!******************************!*\
  !*** ./js_modules/header.js ***!
  \******************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("let trigram = document.getElementById('trigram'),\r\n    header = document.getElementById('header'),\r\n    bodyShadow = document.createElement('div');\r\n\r\nlet wrapper = document.getElementsByClassName('wrapper')[0];\r\n\r\nif (document.body.offsetWidth <= 750) {\r\n    wrapper.style.marginTop = header.offsetHeight + 'px';\r\n}\r\n\r\nbodyShadow.classList.add('body-shadow');\r\nbodyShadow.id = 'body-shadow';\r\n\r\nwrapper.appendChild(bodyShadow);\r\n\r\nbodyShadow = document.getElementById('body-shadow');\r\n\r\ntrigram.addEventListener('click', () => {\r\n    trigram.classList.toggle('open');\r\n    document.getElementsByClassName('nav')[0].classList.toggle('open');\r\n    document.getElementsByClassName('header__options')[0].classList.toggle('open');\r\n    bodyShadow.classList.toggle('active');\r\n});\r\n\r\naddEventListener('resize', () => {\r\n    if (document.body.offsetWidth >= 750) {\r\n\r\n        wrapper.style.marginTop = '';\r\n\r\n        if (bodyShadow.classList.contains('active')) {\r\n            bodyShadow.classList.remove('active');\r\n        }\r\n    } else {\r\n\r\n        wrapper.style.marginTop = header.offsetHeight + 'px';\r\n\r\n        if (trigram.classList.contains('open')) {\r\n            bodyShadow.classList.add('active');\r\n        }\r\n    }\r\n});\n\n//# sourceURL=webpack:///./js_modules/header.js?");

/***/ }),

/***/ "./js_modules/news.js":
/*!****************************!*\
  !*** ./js_modules/news.js ***!
  \****************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _slider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./slider */ \"./js_modules/slider.js\");\n/* harmony import */ var _tags__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./tags */ \"./js_modules/tags.js\");\n\r\n\r\n\r\nlet tags = {\r\n    tagsOpenButton: document.getElementById('tags__open-button'),\r\n    tagsList: document.getElementById('tags__list')\r\n};\r\n\r\nObject(_tags__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(tags);\r\n\r\nif (document.getElementById('important-news')) {\r\n    let importantNews = {\r\n        container: document.getElementById('important-news'),\r\n        list: document.getElementById('important-news__list'),\r\n        items: document.getElementsByClassName('important-news__item'),\r\n        rightButton: document.getElementById('important-news__button_right')\r\n    };\r\n\r\n    Object(_slider__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(importantNews);\r\n}\n\n//# sourceURL=webpack:///./js_modules/news.js?");

/***/ }),

/***/ "./js_modules/slider.js":
/*!******************************!*\
  !*** ./js_modules/slider.js ***!
  \******************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return createSlider; });\nfunction createSlider(obj) {\r\n    if (obj.items.length != 1) {\r\n        let itemWidth = obj.items[0].offsetWidth;\r\n\r\n        let betweenElemsDistance = Math.abs(obj.items[0].offsetLeft + obj.items[0].offsetWidth - obj.items[1].offsetLeft);\r\n\r\n        let maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance),\r\n            currentScrollWidth = 0;\r\n\r\n        let sliderTouchStart = 0,\r\n            sliderTouchEnd = 0;\r\n\r\n        obj.list.addEventListener('touchstart', (e) => {\r\n            sliderTouchStart = e.changedTouches[0].screenX;\r\n        });\r\n\r\n        obj.list.addEventListener('touchend', (e) => {\r\n            sliderTouchEnd = e.changedTouches[0].screenX;\r\n            /* Чтобы нажатие на ссылки и т.д. в слайде не засчитывались как свайпы свайп должен быть не короче чем 20 пикселей */\r\n            if (Math.abs(sliderTouchStart - sliderTouchEnd) >= 20) {\r\n                if (sliderTouchEnd > sliderTouchStart) scrollLeft();\r\n                else if (sliderTouchEnd < sliderTouchStart) scrollRight();\r\n            }\r\n        });\r\n\r\n        obj.container.addEventListener('click', (e) => {\r\n            let target = e.target;\r\n\r\n            while (target != this) {\r\n                if (target == obj.rightButton) { scrollRight(); }\r\n                else if (target == obj.leftButton) { scrollLeft(); }\r\n\r\n                target = target.parentNode;\r\n            }\r\n        });\r\n\r\n        addEventListener(\"resize\", () => {\r\n            let currentItem = Math.floor(-currentScrollWidth / itemWidth); // Вычисления номера слайда отображаемого на экране\r\n\r\n            if (currentItem > 0) {\r\n                /* Если это не самый первый слайд, то идет перерасчет ширины прокрутки для новой ширины окна браузера */\r\n                currentScrollWidth = -((obj.items[0].offsetWidth + betweenElemsDistance) * currentItem);\r\n            } else { currentScrollWidth = 0; }\r\n\r\n            obj.list.style.marginLeft = currentScrollWidth + \"px\"; // Перемещение на новую точку после перерасчета\r\n            maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance); // Перерасчет максимальной ширины прокрутки\r\n            itemWidth = obj.items[0].offsetWidth; // Запоминаем новую текущую ширину одного слайда\r\n        });\r\n\r\n        let scrollLeft = () => {\r\n            if (currentScrollWidth < 0) {\r\n                let currentItem = Math.floor(-currentScrollWidth / itemWidth);\r\n\r\n                currentScrollWidth =\r\n                    currentScrollWidth + itemWidth + betweenElemsDistance;\r\n                obj.list.style.marginLeft = currentScrollWidth + 'px';\r\n            } else {\r\n                currentScrollWidth = maxScrollWidth;\r\n                obj.list.style.marginLeft = currentScrollWidth + 'px';\r\n            }\r\n        };\r\n\r\n        let scrollRight = () => {\r\n            if (currentScrollWidth > maxScrollWidth) {\r\n                let currentItem = Math.floor(-currentScrollWidth / itemWidth);\r\n\r\n                currentScrollWidth =\r\n                    currentScrollWidth - itemWidth - betweenElemsDistance;\r\n                obj.list.style.marginLeft = currentScrollWidth + \"px\";\r\n            } else {\r\n                currentScrollWidth = 0;\r\n                obj.list.style.marginLeft = currentScrollWidth + 'px';\r\n            }\r\n        };\r\n    }\r\n}\n\n//# sourceURL=webpack:///./js_modules/slider.js?");

/***/ }),

/***/ "./js_modules/tags.js":
/*!****************************!*\
  !*** ./js_modules/tags.js ***!
  \****************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return connectTagsButton; });\nfunction connectTagsButton(obj) {\r\n    obj.tagsOpenButton.addEventListener('click', () => {\r\n        obj.tagsOpenButton.classList.toggle('open');\r\n        obj.tagsList.classList.toggle('open');\r\n    });\r\n}\n\n//# sourceURL=webpack:///./js_modules/tags.js?");

/***/ }),

/***/ 1:
/*!*******************************************************!*\
  !*** multi @js_modules/news.js @js_modules/header.js ***!
  \*******************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("__webpack_require__(/*! @js_modules/news.js */\"./js_modules/news.js\");\nmodule.exports = __webpack_require__(/*! @js_modules/header.js */\"./js_modules/header.js\");\n\n\n//# sourceURL=webpack:///multi_@js_modules/news.js_@js_modules/header.js?");

/***/ })

/******/ });
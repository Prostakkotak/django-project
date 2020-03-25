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
/******/ 	return __webpack_require__(__webpack_require__.s = "./js_modules/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./js_modules/animated-slider.js":
/*!***************************************!*\
  !*** ./js_modules/animated-slider.js ***!
  \***************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return createAnimatedSlider; });\nfunction createAnimatedSlider(obj) {\r\n    if (obj.items.length != 1) {\r\n\r\n        for (let i = 0; i <= obj.items.length - 1; i++) {\r\n            if (i != 0) {\r\n                obj.items[i].getElementsByClassName('slider__text')[0].classList.add('shadowed');\r\n            }\r\n        }\r\n\r\n\r\n        if (!obj.leftButton) obj.leftButton = '';\r\n        if (!obj.rightButton) obj.rightButton = '';\r\n\r\n        let itemWidth = obj.items[0].offsetWidth\r\n\r\n        let betweenElemsDistance = Math.abs(obj.items[0].offsetLeft + obj.items[0].offsetWidth - obj.items[1].offsetLeft);\r\n\r\n        let maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance);\r\n        let currentScrollWidth = 0;\r\n\r\n        obj.container.onclick = function (e) {\r\n            let target = e.target;\r\n\r\n            while (target != this && !obj.list.classList.contains('on-scroll')) {\r\n                if (target == obj.rightButton) {\r\n                    if (currentScrollWidth > maxScrollWidth) {\r\n\r\n                        let currentItem = Math.floor(-currentScrollWidth / itemWidth); // Вычисления номера слайда отображаемого на экране\r\n\r\n                        obj.items[currentItem].getElementsByClassName('slider__text')[0].classList.add('shadowed');\r\n                        obj.rightButton.classList.add('shadowed')\r\n\r\n                        obj.list.classList.add('on-scroll')\r\n\r\n                        setTimeout(function () {\r\n                            currentScrollWidth =\r\n                                currentScrollWidth - obj.items[0].offsetWidth - betweenElemsDistance;\r\n                            obj.list.style.marginLeft = currentScrollWidth + \"px\";\r\n\r\n                            setTimeout(function () {\r\n                                obj.items[currentItem + 1].getElementsByClassName('slider__text')[0].classList.remove('shadowed');\r\n                                obj.rightButton.classList.remove('shadowed')\r\n                                obj.list.classList.remove('on-scroll')\r\n                            }, 700)\r\n                        }, 700)\r\n                    } else {\r\n                        obj.items[obj.items.length - 1].getElementsByClassName('slider__text')[0].classList.add('shadowed')\r\n                        obj.rightButton.classList.add('shadowed')\r\n                        obj.list.classList.add('on-scroll')\r\n\r\n                        setTimeout(function () {\r\n                            currentScrollWidth = 0;\r\n                            obj.list.style.marginLeft = currentScrollWidth + 'px';\r\n\r\n                            setTimeout(function () {\r\n                                obj.items[0].getElementsByClassName('slider__text')[0].classList.remove('shadowed')\r\n                                obj.rightButton.classList.remove('shadowed')\r\n                                obj.list.classList.remove('on-scroll')\r\n                            }, 700)\r\n                        }, 700)\r\n                    }\r\n                }\r\n\r\n                target = target.parentNode; // Чтобы функция не повесила всю страницу\r\n            }\r\n        };\r\n\r\n        addEventListener(\"resize\", function () {\r\n            let currentItem = Math.floor(-currentScrollWidth / itemWidth); // Вычисления номера слайда отображаемого на экране\r\n\r\n            if (currentItem > 0) {\r\n                // Если это не самый первый слайд, то идет перерасчет ширины прокрути для новой ширины окна браузера\r\n                currentScrollWidth = (obj.items[0].offsetWidth + betweenElemsDistance) * currentItem;\r\n                currentScrollWidth = -currentScrollWidth;\r\n            } else {\r\n                currentScrollWidth = 0;\r\n            }\r\n\r\n            obj.list.style.marginLeft = currentScrollWidth + \"px\"; // Возврат к стартовой точке\r\n            maxScrollWidth = (obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance;\r\n            maxScrollWidth = -maxScrollWidth; // Перерасчет максимальной ширины прокрутки\r\n            itemWidth = obj.items[0].offsetWidth; // Запоминаем новую текущую ширину одного слайда\r\n        });\r\n    }\r\n}\n\n//# sourceURL=webpack:///./js_modules/animated-slider.js?");

/***/ }),

/***/ "./js_modules/index.js":
/*!*****************************!*\
  !*** ./js_modules/index.js ***!
  \*****************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _animated_slider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./animated-slider */ \"./js_modules/animated-slider.js\");\n/* harmony import */ var _slider__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./slider */ \"./js_modules/slider.js\");\n\r\n\r\n\r\nlet fleetGallery = {\r\n    container: document.getElementById('fleet-gallery'),\r\n    list: document.getElementById('fleet-gallery__slider-list'),\r\n    items: document.getElementsByClassName('fleet-gallery__slider-item'),\r\n    leftButton: document.getElementById('fleet-gallery__slider-button_left'),\r\n    rightButton: document.getElementById('fleet-gallery__slider-button_right')\r\n}\r\n\r\nlet headerSlider = {\r\n    container: document.getElementById('slider'),\r\n    list: document.getElementById('slider__list'),\r\n    items: document.getElementsByClassName('slider__item'),\r\n    rightButton: document.getElementById('slider__button')\r\n}\r\n\r\nObject(_animated_slider__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(headerSlider)\r\nObject(_slider__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(fleetGallery)\n\n//# sourceURL=webpack:///./js_modules/index.js?");

/***/ }),

/***/ "./js_modules/slider.js":
/*!******************************!*\
  !*** ./js_modules/slider.js ***!
  \******************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return createSlider; });\nfunction createSlider(obj) {\r\n    if (obj.items.length != 1) {\r\n\r\n        if (!obj.leftButton) obj.leftButton = '';\r\n        if (!obj.rightButton) obj.rightButton = '';\r\n\r\n        let itemWidth = obj.items[0].offsetWidth\r\n\r\n        let betweenElemsDistance = Math.abs(obj.items[0].offsetLeft + obj.items[0].offsetWidth - obj.items[1].offsetLeft);\r\n\r\n        let maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance);\r\n        let currentScrollWidth = 0;\r\n\r\n        obj.container.onclick = function (e) {\r\n            let target = e.target;\r\n\r\n            while (target != this) {\r\n                if (target == obj.rightButton) {\r\n                    if (currentScrollWidth > maxScrollWidth) {\r\n                        let currentItem = Math.floor(-currentScrollWidth / itemWidth);\r\n\r\n                        currentScrollWidth =\r\n                            currentScrollWidth - itemWidth - betweenElemsDistance;\r\n                        obj.list.style.marginLeft = currentScrollWidth + \"px\";\r\n                    } else {\r\n                        currentScrollWidth = 0;\r\n                        obj.list.style.marginLeft = currentScrollWidth + 'px';\r\n                    }\r\n                } else if (target == obj.leftButton) {\r\n                    if (currentScrollWidth < 0) {\r\n                        let currentItem = Math.floor(-currentScrollWidth / itemWidth);\r\n\r\n                        currentScrollWidth =\r\n                            currentScrollWidth + itemWidth + betweenElemsDistance;\r\n                        obj.list.style.marginLeft = currentScrollWidth + 'px';\r\n                    } else {\r\n                        currentScrollWidth = maxScrollWidth;\r\n                        obj.list.style.marginLeft = currentScrollWidth + 'px';\r\n                    }\r\n                }\r\n\r\n                target = target.parentNode;\r\n            }\r\n        }\r\n\r\n        addEventListener(\"resize\", function () {\r\n            let currentItem = Math.floor(-currentScrollWidth / itemWidth); // Вычисления номера слайда отображаемого на экране\r\n\r\n            if (currentItem > 0) {\r\n                // Если это не самый первый слайд, то идет перерасчет ширины прокрутки для новой ширины окна браузера\r\n                currentScrollWidth = -((obj.items[0].offsetWidth + betweenElemsDistance) * currentItem);\r\n            } else {\r\n                currentScrollWidth = 0;\r\n            }\r\n\r\n            obj.list.style.marginLeft = currentScrollWidth + \"px\"; // Перемещение на новую точку после перерасчета\r\n            maxScrollWidth = (obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance;\r\n            maxScrollWidth = -maxScrollWidth; // Перерасчет максимальной ширины прокрутки\r\n            itemWidth = obj.items[0].offsetWidth; // Запоминаем новую текущую ширину одного слайда\r\n        });\r\n    }\r\n}\n\n//# sourceURL=webpack:///./js_modules/slider.js?");

/***/ })

/******/ });
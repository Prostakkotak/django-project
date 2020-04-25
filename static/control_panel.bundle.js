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
/******/ 	return __webpack_require__(__webpack_require__.s = 4);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./js_modules/control-panel.js":
/*!*************************************!*\
  !*** ./js_modules/control-panel.js ***!
  \*************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("let controlMenu = document.getElementById('control-panel__menu');\r\n\r\nlet blockList = document.getElementsByClassName('control-panel__block'),\r\n    controlMenuItems = controlMenu.getElementsByClassName('control-panel__item');\r\n\r\nlet currentMenuItem = controlMenuItems[0],\r\n    currentBlock;\r\n\r\ncontrolMenuItems[0].classList.add('current');\r\ncurrentMenuItem = controlMenuItems[0];\r\n\r\n// Отображаем самый первый элемент из меню при загрузке страницы\r\nfor (let i = 0; i < blockList.length; i++) {\r\n    if (blockList[i].getAttribute('data-model-name') == controlMenuItems[0].getAttribute('data-model-name')) {\r\n        blockList[i].classList.add('current');\r\n        setTimeout(async ()=> {\r\n            blockList[i].classList.add('opening');\r\n        }, 1);\r\n        currentBlock = blockList[i];\r\n    } else {\r\n        blockList[i].classList.remove('current');\r\n    }\r\n}\r\n\r\n/*\r\n * Берем стили блоков управления и рассчитываем\r\n * минимальную высоту(минимальная высота=высота менюшки) учитывая внутренние отступы\r\n */\r\nlet blockListStyles = window.getComputedStyle(blockList[0]),\r\n    minBlockHeight = (\r\n        controlMenu.offsetHeight - parseInt(blockListStyles.paddingBottom) - parseInt(blockListStyles.paddingTop)\r\n    );\r\n\r\ncontrolMenu.addEventListener('click', (e) => {\r\n    let target = e.target;\r\n\r\n    while (target != this) {\r\n\r\n        if (target.classList.contains('control-panel__item')) {\r\n            if (!target.classList.contains('current')) {\r\n                /*\r\n                 * Удаление current со всех элементов и добавление \r\n                 * current к указанному пункту меню и соответствующему блоку управления\r\n                 */\r\n                for (let i = 0; i < controlMenuItems.length; i++) {\r\n                    controlMenuItems[i].classList.remove('current');\r\n\r\n                    if (blockList[i].getAttribute('data-model-name') == target.getAttribute('data-model-name')) {\r\n                        currentBlock.classList.remove('opening'); // Убираем класс открытия с прошлого блока\r\n\r\n                        blockList[i].classList.add('current'); // Добавляем классы к открываемому блоку\r\n                        setTimeout(async () => {\r\n                            blockList[i].classList.add('opening');\r\n                        }, 1);\r\n\r\n                        currentBlock = blockList[i]; // Переопределение текущего блока\r\n                    } else {\r\n                        blockList[i].classList.remove('current');\r\n                    }\r\n                }\r\n\r\n                target.classList.add('current');\r\n            }\r\n        }\r\n\r\n        target = target.parentNode;\r\n    }\r\n});\r\n\r\n\r\n// Вешаем обработчики для раскрывающихся списков с моделями\r\nfor (let i = 0; i < blockList.length; i++) {\r\n\r\n    blockList[i].style.minHeight = minBlockHeight + 'px';\r\n\r\n    let modelsList = blockList[i].getElementsByClassName('models-list')[0],\r\n        modelsListButton = blockList[i].getElementsByClassName('models-list__button')[0];\r\n\r\n    modelsListButton.addEventListener('click', () => {\r\n        blockList[i].getElementsByClassName('models-list__header')[0].classList.toggle('open');\r\n        modelsList.classList.toggle('open');\r\n    });\r\n}\n\n//# sourceURL=webpack:///./js_modules/control-panel.js?");

/***/ }),

/***/ "./js_modules/header.js":
/*!******************************!*\
  !*** ./js_modules/header.js ***!
  \******************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("let trigram = document.getElementById('trigram'),\r\n    header = document.getElementById('header'),\r\n    bodyShadow = document.createElement('div');\r\n\r\nlet wrapper = document.getElementsByClassName('wrapper')[0];\r\n\r\nif (document.body.offsetWidth <= 750) {\r\n    wrapper.style.marginTop = header.offsetHeight + 'px';\r\n}\r\n\r\nbodyShadow.classList.add('body-shadow');\r\nbodyShadow.id = 'body-shadow';\r\n\r\nwrapper.appendChild(bodyShadow);\r\n\r\nbodyShadow = document.getElementById('body-shadow');\r\n\r\ntrigram.addEventListener('click', () => {\r\n    trigram.classList.toggle('open');\r\n    document.getElementsByClassName('nav')[0].classList.toggle('open');\r\n    document.getElementsByClassName('header__options')[0].classList.toggle('open');\r\n    bodyShadow.classList.toggle('active');\r\n});\r\n\r\naddEventListener('resize', () => {\r\n    if (document.body.offsetWidth >= 750) {\r\n\r\n        wrapper.style.marginTop = '';\r\n\r\n        if (bodyShadow.classList.contains('active')) {\r\n            bodyShadow.classList.remove('active');\r\n        }\r\n    } else {\r\n\r\n        wrapper.style.marginTop = header.offsetHeight + 'px';\r\n\r\n        if (trigram.classList.contains('open')) {\r\n            bodyShadow.classList.add('active');\r\n        }\r\n    }\r\n});\n\n//# sourceURL=webpack:///./js_modules/header.js?");

/***/ }),

/***/ 4:
/*!****************************************************************!*\
  !*** multi @js_modules/header.js @js_modules/control-panel.js ***!
  \****************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("__webpack_require__(/*! @js_modules/header.js */\"./js_modules/header.js\");\nmodule.exports = __webpack_require__(/*! @js_modules/control-panel.js */\"./js_modules/control-panel.js\");\n\n\n//# sourceURL=webpack:///multi_@js_modules/header.js_@js_modules/control-panel.js?");

/***/ })

/******/ });
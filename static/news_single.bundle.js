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
/******/ 	return __webpack_require__(__webpack_require__.s = 2);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./js_modules/delete-confirmation.js":
/*!*******************************************!*\
  !*** ./js_modules/delete-confirmation.js ***!
  \*******************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return deleteConfirmationPopUp; });\nfunction deleteConfirmationPopUp(link, deleteObjName) {\r\n    document.addEventListener('DOMContentLoaded', () => {\r\n\r\n        if (!document.getElementById('body-shadow')) {\r\n            let bodyShadow = document.createElement('div');\r\n\r\n            bodyShadow.classList.add('body-shadow');\r\n            bodyShadow.id = 'body-shadow';\r\n\r\n            wrapper.appendChild(bodyShadow);\r\n        }\r\n\r\n        link.addEventListener('click', (e) => {\r\n            let evt = e ? e : window.event;\r\n\r\n            (evt.preventDefault) ? evt.preventDefault() : evt.returnValue = false;\r\n\r\n            let popUp = document.createElement('div'),\r\n                confirmButton = document.createElement('a'),\r\n                cancelButton = document.createElement('div'),\r\n                deleteWarning = document.createElement('div');\r\n\r\n            popUp.id = 'delete-pop-up';\r\n            popUp.classList.add('delete-pop-up');\r\n\r\n            confirmButton.classList.add('delete-pop-up__confirmation');\r\n            confirmButton.href = link.href;\r\n            confirmButton.textContent = 'Yes';\r\n\r\n            cancelButton.id = 'delete-cancel';\r\n            cancelButton.classList.add('delete-pop-up__cancel');\r\n            cancelButton.textContent = 'Cancel';\r\n\r\n            deleteWarning.classList.add('delete-pop-up__warning');\r\n            deleteWarning.textContent = `Are you sure you want to delete ${deleteObjName}?`;\r\n\r\n            popUp.append(deleteWarning, confirmButton, cancelButton);\r\n            document.getElementsByClassName('wrapper')[0].append(popUp);\r\n\r\n            document.getElementById('body-shadow').classList.add('active');\r\n\r\n            cancelButton.addEventListener('click', () => {\r\n                popUp.remove();\r\n                document.getElementById('body-shadow').classList.remove('active');\r\n            });\r\n        });\r\n    });\r\n}\n\n//# sourceURL=webpack:///./js_modules/delete-confirmation.js?");

/***/ }),

/***/ "./js_modules/header.js":
/*!******************************!*\
  !*** ./js_modules/header.js ***!
  \******************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("let trigram = document.getElementById('trigram'),\r\n    header = document.getElementById('header'),\r\n    bodyShadow = document.createElement('div');\r\n\r\nlet wrapper = document.getElementsByClassName('wrapper')[0];\r\n\r\nif (document.body.offsetWidth <= 750) {\r\n    wrapper.style.marginTop = header.offsetHeight + 'px';\r\n}\r\n\r\nbodyShadow.classList.add('body-shadow');\r\nbodyShadow.id = 'body-shadow';\r\n\r\nwrapper.appendChild(bodyShadow);\r\n\r\nbodyShadow = document.getElementById('body-shadow');\r\n\r\ntrigram.addEventListener('click', () => {\r\n    trigram.classList.toggle('open');\r\n    document.getElementsByClassName('nav')[0].classList.toggle('open');\r\n    document.getElementsByClassName('header__options')[0].classList.toggle('open');\r\n    bodyShadow.classList.toggle('active');\r\n});\r\n\r\naddEventListener('resize', () => {\r\n    if (document.body.offsetWidth >= 750) {\r\n\r\n        wrapper.style.marginTop = '';\r\n\r\n        if (bodyShadow.classList.contains('active')) {\r\n            bodyShadow.classList.remove('active');\r\n        }\r\n    } else {\r\n\r\n        wrapper.style.marginTop = header.offsetHeight + 'px';\r\n\r\n        if (trigram.classList.contains('open')) {\r\n            bodyShadow.classList.add('active');\r\n        }\r\n    }\r\n});\n\n//# sourceURL=webpack:///./js_modules/header.js?");

/***/ }),

/***/ "./js_modules/news-single.js":
/*!***********************************!*\
  !*** ./js_modules/news-single.js ***!
  \***********************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _delete_confirmation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./delete-confirmation */ \"./js_modules/delete-confirmation.js\");\n\r\n\r\nObject(_delete_confirmation__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(document.getElementById('delete-pop-up__link_news'), 'news');\r\n\r\nlet comments = document.getElementsByClassName('news-comments__item-delete');\r\n\r\nfor (let i = 0; i < comments.length; i++) {\r\n    Object(_delete_confirmation__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(comments[i], 'comment');\r\n}\n\n//# sourceURL=webpack:///./js_modules/news-single.js?");

/***/ }),

/***/ 2:
/*!**************************************************************!*\
  !*** multi @js_modules/header.js @js_modules/news-single.js ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("__webpack_require__(/*! @js_modules/header.js */\"./js_modules/header.js\");\nmodule.exports = __webpack_require__(/*! @js_modules/news-single.js */\"./js_modules/news-single.js\");\n\n\n//# sourceURL=webpack:///multi_@js_modules/header.js_@js_modules/news-single.js?");

/***/ })

/******/ });
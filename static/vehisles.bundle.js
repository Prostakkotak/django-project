!function(e){var t={};function n(o){if(t[o])return t[o].exports;var s=t[o]={i:o,l:!1,exports:{}};return e[o].call(s.exports,s,s.exports,n),s.l=!0,s.exports}n.m=e,n.c=t,n.d=function(e,t,o){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(n.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var s in e)n.d(o,s,function(t){return e[t]}.bind(null,s));return o},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=5)}({0:function(e,t){let n=document.getElementById("trigram"),o=document.getElementById("header"),s=document.createElement("div"),r=document.getElementsByClassName("wrapper")[0];document.body.offsetWidth<=750&&(r.style.marginTop=o.offsetHeight+"px"),s.classList.add("body-shadow"),s.id="body-shadow",r.appendChild(s),s=document.getElementById("body-shadow"),n.addEventListener("click",()=>{n.classList.toggle("open"),document.getElementsByClassName("nav")[0].classList.toggle("open"),document.getElementsByClassName("header__options")[0].classList.toggle("open"),s.classList.toggle("active")}),addEventListener("resize",()=>{document.body.offsetWidth>=750?(r.style.marginTop="",s.classList.contains("active")&&s.classList.remove("active")):(r.style.marginTop=o.offsetHeight+"px",n.classList.contains("open")&&s.classList.add("active"))})},12:function(e,t,n){"use strict";n.r(t);let o={filtersOpenButton:document.getElementById("filters__button_open"),filtersForm:document.getElementById("filters__form")};var s;(s=o).filtersOpenButton.addEventListener("click",()=>{s.filtersOpenButton.classList.toggle("open"),s.filtersForm.classList.toggle("open")})},5:function(e,t,n){n(12),e.exports=n(0)}});
!function(t){var e={};function n(s){if(e[s])return e[s].exports;var o=e[s]={i:s,l:!1,exports:{}};return t[s].call(o.exports,o,o.exports,n),o.l=!0,o.exports}n.m=t,n.c=e,n.d=function(t,e,s){n.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:s})},n.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},n.t=function(t,e){if(1&e&&(t=n(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var s=Object.create(null);if(n.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var o in t)n.d(s,o,function(e){return t[e]}.bind(null,o));return s},n.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return n.d(e,"a",e),e},n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},n.p="",n(n.s=3)}([function(t,e){let n=document.getElementById("trigram"),s=document.getElementById("header"),o=document.createElement("div"),i=document.getElementsByClassName("wrapper")[0];document.body.offsetWidth<=750&&(i.style.marginTop=s.offsetHeight+"px"),o.classList.add("body-shadow"),o.id="body-shadow",i.appendChild(o),o=document.getElementById("body-shadow"),s.addEventListener("click",(function(t){for(target=t.target;target!=this;)target==n&&(n.classList.toggle("open"),document.getElementsByClassName("nav")[0].classList.toggle("open"),document.getElementsByClassName("header__options")[0].classList.toggle("open"),o.classList.toggle("active")),target=target.parentNode})),addEventListener("resize",(function(){document.body.offsetWidth>=750?(i.style.marginTop="",o.classList.contains("active")&&o.classList.remove("active")):(i.style.marginTop=s.offsetHeight+"px",n.classList.contains("open")&&o.classList.add("active"))}))},function(t,e,n){"use strict";function s(t){if(1!=t.items.length){let e=t.items[0].offsetWidth,n=Math.abs(t.items[0].offsetLeft+t.items[0].offsetWidth-t.items[1].offsetLeft),s=-((t.items.length-1)*t.items[0].offsetWidth+n),o=0,i=0,r=0;t.list.addEventListener("touchstart",t=>{i=t.changedTouches[0].screenX}),t.list.addEventListener("touchend",t=>{r=t.changedTouches[0].screenX,Math.abs(i-r)>=20&&(r>i?a():r<i&&l())}),t.container.addEventListener("click",e=>{let n=e.target;for(;n!=this;)n==t.rightButton?l():n==t.leftButton&&a(),n=n.parentNode}),addEventListener("resize",()=>{let i=Math.floor(-o/e);o=i>0?-(t.items[0].offsetWidth+n)*i:0,t.list.style.marginLeft=o+"px",s=-((t.items.length-1)*t.items[0].offsetWidth+n),e=t.items[0].offsetWidth});let a=()=>{if(o<0){Math.floor(-o/e);o=o+e+n,t.list.style.marginLeft=o+"px"}else o=s,t.list.style.marginLeft=o+"px"},l=()=>{if(o>s){Math.floor(-o/e);o=o-e-n,t.list.style.marginLeft=o+"px"}else o=0,t.list.style.marginLeft=o+"px"}}}n.d(e,"a",(function(){return s}))},,function(t,e,n){n(10),t.exports=n(0)},,,,,,,function(t,e,n){"use strict";n.r(e);var s=n(1);let o={container:document.getElementById("important-news"),list:document.getElementById("important-news__list"),items:document.getElementsByClassName("important-news__item"),rightButton:document.getElementById("important-news__button_right")},i={tagsOpenButton:document.getElementById("tags__open-button"),tagsList:document.getElementById("tags__list")};var r;(r=i).tagsOpenButton.addEventListener("click",()=>{r.tagsOpenButton.classList.toggle("open"),r.tagsList.classList.toggle("open")}),Object(s.a)(o)}]);
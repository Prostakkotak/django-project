!function(e){var t={};function n(s){if(t[s])return t[s].exports;var a=t[s]={i:s,l:!1,exports:{}};return e[s].call(a.exports,a,a.exports,n),a.l=!0,a.exports}n.m=e,n.c=t,n.d=function(e,t,s){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:s})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var s=Object.create(null);if(n.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)n.d(s,a,function(t){return e[t]}.bind(null,a));return s},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=10)}([function(e,t){let n=document.getElementById("trigram"),s=document.getElementById("header"),a=document.createElement("div"),o=document.getElementsByClassName("wrapper")[0];document.body.offsetWidth<=750&&(o.style.marginTop=s.offsetHeight+"px"),a.classList.add("body-shadow"),a.id="body-shadow",o.appendChild(a),a=document.getElementById("body-shadow"),n.addEventListener("click",()=>{n.classList.toggle("open"),document.getElementsByClassName("nav")[0].classList.toggle("open"),document.getElementsByClassName("header__options")[0].classList.toggle("open"),a.classList.toggle("active")}),addEventListener("resize",()=>{document.body.offsetWidth>=750?(o.style.marginTop="",a.classList.contains("active")&&a.classList.remove("active")):(o.style.marginTop=s.offsetHeight+"px",n.classList.contains("open")&&a.classList.add("active"))})},function(e,t,n){"use strict";function s(e,t){document.addEventListener("DOMContentLoaded",()=>{if(!document.getElementById("body-shadow")){let e=document.createElement("div");e.classList.add("body-shadow"),e.id="body-shadow",wrapper.appendChild(e)}e.addEventListener("click",n=>{let s=n||window.event;s.preventDefault?s.preventDefault():s.returnValue=!1;let a=document.createElement("div"),o=document.createElement("a"),l=document.createElement("div"),d=document.createElement("div");a.id="delete-pop-up",a.classList.add("delete-pop-up"),o.classList.add("delete-pop-up__confirmation"),o.href=e.href,o.textContent="Yes",l.id="delete-cancel",l.classList.add("delete-pop-up__cancel"),l.textContent="Cancel",d.classList.add("delete-pop-up__warning"),d.textContent=`Are you sure you want to delete ${t}?`,a.append(d,o,l),document.getElementsByClassName("wrapper")[0].append(a),document.getElementById("body-shadow").classList.add("active"),l.addEventListener("click",()=>{a.remove(),document.getElementById("body-shadow").classList.remove("active")})})})}n.d(t,"a",(function(){return s}))},,,,,,,,,function(e,t,n){n(0),e.exports=n(11)},function(e,t,n){"use strict";n.r(t);var s=n(1);let a=document.getElementsByClassName("models-list__link_delete");for(let e=0;e<a.length;e++)Object(s.a)(a[e],"model");let o,l=document.getElementById("control-panel__menu"),d=document.getElementsByClassName("control-panel__block"),r=l.getElementsByClassName("control-panel__item"),i=r[0];r[0].classList.add("current"),i=r[0];for(let e=0;e<d.length;e++)d[e].getAttribute("data-model-name")==r[0].getAttribute("data-model-name")?(d[e].classList.add("current"),setTimeout(async()=>{d[e].classList.add("opening")},1),o=d[e]):d[e].classList.remove("current");let c=window.getComputedStyle(d[0]),m=l.offsetHeight-parseInt(c.paddingBottom)-parseInt(c.paddingTop);l.addEventListener("click",e=>{let t=e.target;for(;null!=t;){if(t.classList.contains("control-panel__item")&&!t.classList.contains("current")){for(let e=0;e<r.length;e++)r[e].classList.remove("current"),d[e].getAttribute("data-model-name")==t.getAttribute("data-model-name")?(o.classList.remove("opening"),d[e].classList.add("current"),setTimeout(async()=>{d[e].classList.add("opening")},1),o=d[e]):d[e].classList.remove("current");t.classList.add("current")}t=t.parentNode}});for(let e=0;e<d.length;e++){d[e].style.minHeight=m+"px";let t=d[e].getElementsByClassName("models-list")[0];d[e].getElementsByClassName("models-list__header")[0].addEventListener("click",()=>{d[e].getElementsByClassName("models-list__header")[0].classList.toggle("open"),t.classList.toggle("open")})}}]);
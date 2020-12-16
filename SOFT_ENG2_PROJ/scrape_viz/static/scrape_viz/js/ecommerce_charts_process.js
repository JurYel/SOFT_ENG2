$(document).ready(function(){
    new ScrollBooster({
        viewport: document.querySelector('.slick-list'),
        content: document.querySelector('.slick-track'),
        scrollMode: 'transform',
        direction: 'horizontal',
        emulateScroll: true,
     });
});
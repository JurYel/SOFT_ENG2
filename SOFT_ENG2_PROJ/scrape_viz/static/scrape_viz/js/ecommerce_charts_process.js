$(document).ready(function(){
    new ScrollBooster({
        viewport: document.querySelector('.slick-list'),
        content: document.querySelector('.slick-track'),
        scrollMode: 'transform',
        direction: 'horizontal',
        emulateScroll: true,
     });

     window.onload = function(e){
        //  toggle();
     }

     function toggle(){
        var blur = document.getElementById('blur');
        blur.classList.toggle('active');

        var buffer = document.getElementById('buffer');
        buffer.classList.toggle('active');
    }
});
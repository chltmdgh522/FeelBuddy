
document.addEventListener("DOMContentLoaded", function() {
   const rightButton = document.querySelector("#game-and-watch-leftbutton-right a");
   const leftButton = document.querySelector("#game-and-watch-leftbutton-left a");
   const topButton = document.querySelector("#game-and-watch-leftbutton-top a");
   const bottomButton = document.querySelector("#game-and-watch-leftbutton-bottom a");
   const mainImage = document.getElementById("main-image");
   const nintendoLogo = document.getElementById("game-and-watch-nintendo-logo");

   const imageFiles = ["media/fear.png", "media/sad.png", "media/anger.png", "media/anxiety.png", "media/joy.png"];
   const logoTexts = ["fear", "sad", "anger", "anxiety", "joy"];

   let currentImageIndex = 0;
   let currentTopPosition = 0;

   function updateImageAndLogo() {
       mainImage.src = `/${imageFiles[currentImageIndex]}`;
       nintendoLogo.textContent = logoTexts[currentImageIndex];
   }

   rightButton.addEventListener("click", function(event) {
       event.preventDefault();  // Prevent the default anchor behavior
       currentImageIndex = (currentImageIndex + 1) % imageFiles.length;
       updateImageAndLogo();
   });

   leftButton.addEventListener("click", function(event) {
       event.preventDefault();  // Prevent the default anchor behavior
       currentImageIndex = (currentImageIndex - 1 + imageFiles.length) % imageFiles.length;
       updateImageAndLogo();
   });

   topButton.addEventListener("click", function(event) {
       event.preventDefault();  // Prevent the default anchor behavior
       currentTopPosition -= 10;
       mainImage.style.transform = `translateY(${currentTopPosition}px)`;
   });

   bottomButton.addEventListener("click", function(event) {
       event.preventDefault();  // Prevent the default anchor behavior
       currentTopPosition += 10;
       mainImage.style.transform = `translateY(${currentTopPosition}px)`;
   });
});
function animateThis() {
    // 캐릭터 5개 //
    let box = document.getElementById('box');
    let wrapper1 = document.querySelector('.newcreate-img-wrapper1');
    let wrapper2 = document.querySelector('.newcreate-img-wrapper2');
    let wrapper3 = document.querySelector('.newcreate-img-wrapper3');
    let wrapper4 = document.querySelector('.newcreate-img-wrapper4');
    let wrapper5 = document.querySelector('.newcreate-img-wrapper5');

    let boxchar = document.getElementById('box-char');
    let top = document.getElementById('top');
    let bottom = document.getElementById('bottom');
    let left = document.getElementById('left');
    let right = document.getElementById('right');
    let back = document.getElementById('back');
    let front = document.getElementById('front');

    wrapper1.style.width = '160px';
    wrapper1.style.fontSize = '1rem';
    wrapper1.style.top = '-4rem';
    wrapper1.style.left = '0';

    wrapper2.style.width = '200px';
    wrapper2.style.height = '200px';
    wrapper2.style.fontSize = '1rem';
    wrapper2.style.top = '-4rem';
    wrapper2.style.left = '0';

    wrapper3.style.width = '240px';
    wrapper3.style.height = '240px';
    wrapper3.style.fontSize = '1rem';
    wrapper3.style.top = '-4rem';
    wrapper3.style.left = '0';

    wrapper4.style.width = '200px';
    wrapper4.style.height = '200px';
    wrapper4.style.fontSize = '1rem';
    wrapper4.style.top = '-4rem';
    wrapper4.style.left = '0';

    wrapper5.style.width = '160px';
    wrapper5.style.fontSize = '1rem';
    wrapper5.style.top = '-4rem';
    wrapper5.style.left = '0';

    top.style.display = 'none';
    front.style.transform = 'translateZ(10em) translateY(50%) rotateX(-90deg)';
    left.style.transform = 'rotateY(90deg) translateZ(10em) translateY(50%) rotateX(-90deg)';
    right.style.transform = 'rotateY(270deg) translateZ(10em) translateY(50%) rotateX(-90deg)';
    back.style.transform = 'rotateY(180deg) translateZ(10em) translateY(50%) rotateX(-90deg)';

    // 캐릭터들을 좌우로 퍼지게 함
    setTimeout(() => {
        wrapper1.style.transform = 'translateX(-16em)';
        wrapper2.style.transform = 'translateX(-10em)';
        wrapper3.style.transform = 'translateX(-2rem)';
        wrapper4.style.transform = 'translateX(8.5em)';
        wrapper5.style.transform = 'translateX(17em)';
    }, 500);

    wrapper3.style.zIndex = '10';
    wrapper4.style.zIndex = '5';
    wrapper5.style.zIndex = '1';
}
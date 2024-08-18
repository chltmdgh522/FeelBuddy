
document.addEventListener("DOMContentLoaded", function() {
    const rightButton = document.querySelector("#game-and-watch-leftbutton-right a");
    const leftButton = document.querySelector("#game-and-watch-leftbutton-left a");
    const topButton = document.querySelector("#game-and-watch-leftbutton-top a");
    const bottomButton = document.querySelector("#game-and-watch-leftbutton-bottom a");
    const mainImage = document.getElementById("main-image");
    const nintendoLogo = document.getElementById("game-and-watch-nintendo-logo");
    const miniNintendoLogo = document.getElementById("mini-classic-logo");
    

    const imageFiles = ["media/fear.png", "media/sad.png", "media/anger.png", "media/anxiety.png", "media/joy.png"];
    const logoTexts = ["fear", "sad", "anger", "anxiety", "joy"];

    let currentImageIndex = 0;
    let currentTopPosition = 0;

    function updateImageAndLogo() {
        mainImage.src = `/${imageFiles[currentImageIndex]}`;
        nintendoLogo.textContent = logoTexts[currentImageIndex];
        miniNintendoLogo.textContent = logoTexts[currentImageIndex];
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
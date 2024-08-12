document.addEventListener('DOMContentLoaded', function() {
    const playPauseButton = document.getElementById('playPauseButton');
    const audioPlayer = document.getElementById('audioPlayer');
    
    playPauseButton.addEventListener('click', function() {
        if (audioPlayer.paused) {
            audioPlayer.play();
            // playPauseButton.style.backgroundColor = '#0f0'; 
        } else {
            audioPlayer.pause();
            // playPauseButton.style.backgroundColor = '#f00'; 
        }
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const flipCard = document.getElementById('flipCard');
    const submitCard = document.getElementById('submitCard');
    const envelope = document.querySelector('.envelope');

    function toggleAnimation() {
        if (envelope.classList.contains('active')) {
            flipCard.textContent = 'Animate';
        } else {
            flipCard.textContent = '';
        }
        envelope.classList.toggle('active');
    }

    flipCard.addEventListener('click', toggleAnimation);

    submitCard.addEventListener('click', toggleAnimation);
  });
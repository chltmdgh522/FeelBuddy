function setupResponsiveChat() {
    const contacts = document.querySelectorAll('.contact');
    const contactsContainer = document.querySelector('.contacts');
    const chatContainer = document.querySelector('.chat');
    const backButton = document.querySelector('.header-left'); // 추가된 코드: 뒤로가기 버튼 선택


    function showContacts() {
        chatContainer.style.display = 'none';
        contactsContainer.style.display = 'block';
        sessionStorage.setItem('currentView', 'contacts');
    }

    function showChat() {
        contactsContainer.style.display = 'none';
        chatContainer.style.display = 'flex';
        sessionStorage.setItem('currentView', 'chat');
    }

    if (window.matchMedia("(max-width: 768px)").matches) {
        // Determine initial view based on session storage
        const currentView = sessionStorage.getItem('currentView') || 'contacts';

        if (currentView === 'chat') {
            showChat();
        } else {
            showContacts();
        }

        contacts.forEach(contact => {
            contact.addEventListener('click', showChat);
        });

        // 추가된 코드: 뒤로가기 버튼을 눌렀을 때 연락처를 보여줌
        backButton.addEventListener('click', showContacts);
    } else {
        chatContainer.style.display = 'flex';
        contactsContainer.style.display = 'block';
    }
}

// Run the function on page load
setupResponsiveChat();

// Re-check on window resize
window.addEventListener('resize', setupResponsiveChat);



// 햄버거 버튼 눌렀을 때 추가 아이콘 나오도록
(function($) {

    var header = $('#header-bg');
    var menuButton = $('#menu-icon');
    var menuButtonX = $('#menu-icon-x');
    var menuIcon = $('.header-el');
    var menuIconPhoto = $('#header-photo');
    var menuIconPeople = $('#header-people');
    var menuIconMex = $('#header-mex');
    var menuIconHeart = $('#header-heart');

    var homeElement = $('.el-home-anima');
    var tlhome = new TimelineMax();

    // Initial State: Show the hamburger menu and hide the close icon
    menuButton.addClass('menu-icon-in');
    menuButtonX.addClass('menu-icon-out');
    header.addClass('header-bg');
    tlhome
        .staggerFrom(homeElement, 0.6, { y: 20, autoAlpha: 0, ease:Bounce.easeOut}, 0.2);

    // Button menu click event
    menuButton.on('click', function(){
        menuButton.removeClass('menu-icon-in');
        menuButton.addClass('menu-icon-out');
        menuButtonX.removeClass('menu-icon-out');
        menuButtonX.addClass('menu-icon-in');

        // Show the icons by adding the 'header-el-anima' class
        menuIconPhoto.addClass('header-el-anima');
        menuIconPeople.addClass('header-el-anima');
        menuIconMex.addClass('header-el-anima');
        menuIconHeart.addClass('header-el-anima');
    });

    // Close menu icon event
    menuButtonX.on('click', function(){
        header.addClass('header-bg');
        header.removeClass('header-bg-photo header-bg-people header-bg-mex header-bg-heart');

        menuButton.addClass('menu-icon-in');
        menuButton.removeClass('menu-icon-out');
        menuButtonX.addClass('menu-icon-out');
        menuButtonX.removeClass('menu-icon-in');

        // Hide the icons by removing the 'header-el-anima' class
        menuIconPhoto.removeClass('header-el-anima');
        menuIconPeople.removeClass('header-el-anima');
        menuIconMex.removeClass('header-el-anima');
        menuIconHeart.removeClass('header-el-anima');
        tlhome.restart();
    });

    // Individual icon click event handling
    menuIconPhoto.on('click', function(){
        header.addClass('header-bg-photo');
        header.removeClass('header-bg-people header-bg-mex header-bg-heart');
        tlhome.restart();
    });

    menuIconPeople.on('click', function(){
        header.addClass('header-bg-people');
        header.removeClass('header-bg-photo header-bg-mex header-bg-heart');
        tlhome.restart();
    });

    menuIconMex.on('click', function(){
        header.addClass('header-bg-mex');
        header.removeClass('header-bg-photo header-bg-people header-bg-heart');
        tlhome.restart();
    });

    menuIconHeart.on('click', function(){
        header.addClass('header-bg-heart');
        header.removeClass('header-bg-photo header-bg-people header-bg-mex');
        tlhome.restart();
    });

  })(jQuery);

  (function($) {

    var header = $('#header-bg');
    var menuButton = $('#menu-icon');
    var menuButtonX = $('#menu-icon-x');
    var menuIcons = $('.header-el');

    // Start with the hamburger icon visible and the close icon hidden
    menuButton.addClass('menu-icon-in');
    menuButtonX.addClass('menu-icon-out hidden');

    // Handle the hamburger menu click
    menuButton.on('click', function(){
        menuButton.addClass('hidden');
        menuButtonX.removeClass('hidden');

        // Show the icons by removing the 'hidden' class
        menuIcons.removeClass('hidden').addClass('header-el-anima');
    });

    // Handle the close icon click
    menuButtonX.on('click', function(){
        menuButton.removeClass('hidden');
        menuButtonX.addClass('hidden');

        // Hide the icons by adding the 'hidden' class
        menuIcons.addClass('hidden').removeClass('header-el-anima');
    });

  })(jQuery);



document.querySelector('.character-animation-btn').addEventListener('click', function() {
    animateThis();
});
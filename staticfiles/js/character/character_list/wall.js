document.addEventListener("DOMContentLoaded", function() {
    var roomWalls = document.querySelector('.room-walls');
    
    // Clone the content and append it to ::before
    var beforeContent = roomWalls.querySelector('.walls-content').cloneNode(true);
    var beforeWrapper = document.createElement('div');
    beforeWrapper.style.position = 'absolute';
    beforeWrapper.style.top = '0';
    beforeWrapper.style.left = '0';
    beforeWrapper.style.width = '100%';
    beforeWrapper.style.height = '100%';
    beforeWrapper.style.transform = 'rotateY(90deg)';
    beforeWrapper.style.transformOrigin = 'left center';
    beforeWrapper.appendChild(beforeContent);
    roomWalls.appendChild(beforeWrapper);
    
    // Clone the content and append it to ::after
    var afterContent = roomWalls.querySelector('.walls-content').cloneNode(true);
    var afterWrapper = document.createElement('div');
    afterWrapper.style.position = 'absolute';
    afterWrapper.style.top = '0';
    afterWrapper.style.left = '0';
    afterWrapper.style.width = '100%';
    afterWrapper.style.height = '100%';
    afterWrapper.style.transform = 'rotateY(-90deg)';
    afterWrapper.style.transformOrigin = 'right center';
    afterWrapper.appendChild(afterContent);
    roomWalls.appendChild(afterWrapper);
});
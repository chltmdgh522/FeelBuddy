var chat = document.getElementById('chat');
   chat.scrollTop = chat.scrollHeight - chat.clientHeight;

// // 드래그 기능 구현
// var dragItem = document.querySelector("#drag");
// var container = document.querySelector("#chat-container");

// var active = false;
// var currentX;
// var initialX;
// var xOffset = 0;

// dragItem.addEventListener("mousedown", dragStart, false);
// document.addEventListener("mouseup", dragEnd, false);
// document.addEventListener("mousemove", drag, false);

// function dragStart(e) {
//     initialX = e.clientX - xOffset;

//     if (e.target === dragItem) {
//         active = true;
//     }
// }

// function dragEnd() {
//     initialX = currentX;
//     active = false;
// }

// function drag(e) {
//     if (active) {
//         e.preventDefault();
//         currentX = e.clientX - initialX;
//         xOffset = currentX;
//         setWidth(currentX + container.clientWidth);
//     }
// }

// function setWidth(width) {
//     container.style.width = width + "px";
// }


$('#size').hover( function () {
   $('#drag').fadeOut(500);
 });

$('#size').mousemove( function () {
   $('.chat-center').css('width', $(this).val());
 });

$('#size').change(function () {
   $('.chat-center').css('width', $(this).val());
 });

 document.querySelector('.chat .input textarea').addEventListener('input', function() {
   this.style.height = 'auto';
   this.style.height = (this.scrollHeight) + 'px';
});
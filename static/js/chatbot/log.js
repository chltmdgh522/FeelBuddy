const showButton = document.querySelector("article > button");
const hideButton = document.querySelector("article > button:last-child");
const dayList = document.querySelector("article > ul");

showButton.removeAttribute("hidden");
showButton.addEventListener("click", function () {
  this.parentNode.classList.add("active");
  hideButton.removeAttribute("tabindex");
  this.parentNode.querySelector("li").focus();
});

hideButton.removeAttribute("hidden");
hideButton.addEventListener("click", function () {
  this.parentNode.classList.remove("active");
  this.setAttribute("tabindex", "-1");
  showButton.focus();
});

dayList.addEventListener("keydown", function (e) {
  const key = e.code.toLowerCase();
  if (key === "arrowright" || key === "right") {
    const next = e.target.nextSibling.nextSibling
      ? e.target.nextSibling.nextSibling
      : e.target.parentNode.firstChild.nextSibling;
    if (next) {
      next.focus();
    }
  } else if (key === "arrowleft" || key === "left") {
    const previous = e.target.previousSibling.previousSibling
      ? e.target.previousSibling.previousSibling
      : e.target.parentNode.lastChild.previousSibling;
    if (previous) {
      previous.focus();
    }
  }
});

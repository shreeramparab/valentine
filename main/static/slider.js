let currentSlide = 0;
const slides = document.querySelectorAll(".slide");
const caption = document.getElementById("caption");

function showSlide(index) {
  slides.forEach(slide => slide.classList.remove("active"));
  slides[index].classList.add("active");

  if (caption) {
    caption.innerText = slides[index].dataset.caption || "";
  }
}

function changeSlide(direction) {
  currentSlide += direction;

  if (currentSlide < 0) currentSlide = slides.length - 1;
  if (currentSlide >= slides.length) currentSlide = 0;

  showSlide(currentSlide);
}

if (slides.length > 0) {
  showSlide(0);
}

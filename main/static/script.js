const popup = document.getElementById("popup");
const popupText = document.getElementById("popup-text");

const messages = [
  "Not yet, my love 💕 Come back tomorrow.",
  "Patience, beautiful 🫶 The magic is almost ready.",
  "I see your curiosity 😏 but wait just a little more."
];

document.querySelectorAll(".card").forEach(card => {
  card.addEventListener("click", () => {
    if (card.dataset.unlocked === "true") {
      window.location.href = card.dataset.link;
    } else {
      popupText.innerText =
        messages[Math.floor(Math.random() * messages.length)];
      popup.style.display = "block";
    }
  });
});

function closePopup() {
  popup.style.display = "none";
}

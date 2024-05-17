var modal = document.getElementById("modal");
var btn = document.getElementById("openModalBtn");
var span = document.getElementsByClassName("close")[0];


btn.onclick = function() {
  modal.style.display = "block";
  document.body.classList.add("modal-open");
}

span.onclick = function() {
  modal.style.display = "none";
  document.body.classList.remove("modal-open");
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    document.body.classList.remove("modal-open");
  }
}
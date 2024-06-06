document.addEventListener('DOMContentLoaded', function() {
  var modal = document.querySelector("#modal");
  var btn = document.querySelector("#openSalonModal");
  var span = document.querySelector(".close");
  var salonForm = document.querySelector('#salonForm');
  var selectedSalon = document.querySelector('#selectedSalon');

  btn.addEventListener('click', function() {
    modal.style.display = "block";
    document.body.classList.add("modal-open");
  });

  span.addEventListener('click', function() {
    modal.style.display = "none";
    document.body.classList.remove("modal-open");
    clearUrl();
  });

  window.addEventListener('click', function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
      document.body.classList.remove("modal-open");
      clearUrl();
    }
  });

  salonForm.addEventListener('change', function() {
    var selectedOption = salonForm.querySelector('option:checked');
    if (selectedOption) {
      selectedSalon.textContent = 'Выбранный салон: ' + selectedOption.textContent;
    }
  });
});
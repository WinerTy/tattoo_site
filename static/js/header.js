function toggleMenu() {
    var list = document.querySelector('.list');
    list.classList.toggle('active');
  }

function clearUrl() {
  // Удаляем фрагмент из URL без перезагрузки страницы
  history.pushState("", document.title, window.location.pathname + window.location.search);
}

function checkUrlForModal() {
  var currentUrl = window.location.href;

  if (currentUrl.includes("#UserModal")) {
    var modalButton = document.getElementById("openUserModal");
    
    if (modalButton) {
      modalButton.click();
    }
  }
  if (currentUrl.includes("#SalonModal")) {
    var modalButton = document.getElementById("openSalonModal");
    
    if (modalButton) {
      modalButton.click();
    }
  }
  if (currentUrl.includes("#AppointmentModal")) {
    var modalButton = document.getElementById("OpenAppointmentModal");
    
    if (modalButton) {
      modalButton.click();
    }
  }
}

window.onload = checkUrlForModal;

$(document).ready(function() {
  checkUrlForModal();
});
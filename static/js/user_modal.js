var modal = document.getElementById("UserModal");


var btn = document.getElementById("openUserModal");


var span = document.getElementById("close");

  
btn.onclick = function() {
    modal.style.display = "block";
    document.body.classList.add("modal-open");
}


span.onclick = function() {
    modal.style.display = "none";
    document.body.classList.remove("modal-open");
    clearUrl();
}


window.onclick = function(event) {
    if (event.target == modal) {
    modal.style.display = "none";
    clearUrl();
    }
}


function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}


document.getElementById("defaultOpen").click();
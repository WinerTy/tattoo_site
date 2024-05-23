
var urlParams = new URLSearchParams(window.location.search);
var currentPage = urlParams.get('page');

var paginationItems = document.querySelectorAll('.pagination li a');
paginationItems.forEach(function(item) {
    if (item.getAttribute('href').includes('page=' + currentPage)) {
        item.parentElement.classList.add('active');
    }

    item.addEventListener('click', function(event) {
        if (this.parentElement.classList.contains('active')) {
            event.preventDefault();
        }
    });
});
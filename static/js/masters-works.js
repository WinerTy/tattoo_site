document.addEventListener('DOMContentLoaded', function() {
    var workCards = document.querySelectorAll('.work-card');
    workCards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.querySelector('.work-info').style.opacity = '1';
        });
        card.addEventListener('mouseleave', function() {
            this.querySelector('.work-info').style.opacity = '0';
        });
    });
});
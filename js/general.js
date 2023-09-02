$('.abstract-extender').click(function() {
    var id = this.id.replace('abstract-','');
    if ($('#arrow-' + id).hasClass('fa-caret-right')) {
        $('#arrow-' + id).removeClass('fa-caret-right');
        $('#arrow-' + id).addClass('fa-caret-down');
        document.getElementById('abstract-text-' + id).style.display = 'block';
    }
    else {
        $('#arrow-' + id).removeClass('fa-caret-down');
        $('#arrow-' + id).addClass('fa-caret-right');
        document.getElementById('abstract-text-' + id).style.display = 'none';
    }

});
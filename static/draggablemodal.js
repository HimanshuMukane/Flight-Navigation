const timeout = 500;

// Show modal
$('.show-modal').click(function (e) {
    e.preventDefault();
    const modalId = $(this).data('modal');
    const modal = $('#' + modalId);
    modal.fadeToggle(timeout);
    modal.toggleClass('active');
});

// Close modal
$('.modal-close, .modal-action .close').click(function (e) {
    e.preventDefault();
    const modal = $(this).closest('.modal');
    modal.fadeToggle(timeout);
    modal.toggleClass('active');
});

// Make modal draggable
$('.modal').draggable({ handle: '.modal-content' });
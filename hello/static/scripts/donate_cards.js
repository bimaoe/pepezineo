if (typeof pepezineo === 'undefined') {
  pepezineo = {};
}

pepezineo.donate_cards = {};
pepezineo.donate_cards.donate = function() {
  var data = {};
  $('.donate-card-input').each(function() {
    var quantity = parseInt($(this).val(), 10);
    var card = $(this).data('card'); 
    if (quantity > 0) {
      data[card] = quantity;
    }
  });
  $.post('/donate-cards', data, 
      function() {
        $('.donate-card-input').each(function() {
          var quantity = parseInt($(this).val(), 10);
          var card = $(this).data('card');
          if (quantity) {
            var old_quantity = parseInt($('#'+card+'-quantity').html(), 10);
            $('#'+card+'-quantity').html(old_quantity - quantity);
            $(this).val('');
          }
        });
  }).fail(function() { 
    // TODO(bimaoe): Handle not enough cards error.
  });
}
$(window).on('load', function() {
  $('.donate-card-input').keyup(function(e) {
    if (e.keyCode == 13) {
      pepezineo.donate_cards.donate();
    }
  });
});
if (typeof pepezineo === 'undefined') {
  pepezineo = {};
}

pepezineo.buy_cards = {};
pepezineo.buy_cards.buy = function() {
  var cards = {};
  $('.buy-card-input').each(function() {
    var quantity = parseInt($(this).val(), 10);
    var card = $(this).data('card'); 
    if (quantity > 0) {
      cards[card] = quantity;
    }
  });
  var data = {};
  data['cards'] = cards;
  data['type'] = 'buy';
  $.post('/acquire-cards', JSON.stringify(data), 
      function() {
        $('.buy-card-input').each(function() {
          var quantity = parseInt($(this).val(), 10);
          var card = $(this).data('card');
          if (quantity) {
            var old_quantity = parseInt($('#'+card+'-quantity').html(), 10);
            $('#'+card+'-quantity').html(old_quantity + quantity);
            $(this).val('');
          }
        });
      });
}

$(window).on('load', function() {
  $('.buy-card-input').keyup(function(e) {
    if (e.keyCode == 13) {
      pepezineo.buy_cards.buy();
    }
  });
});
if (typeof pepezineo === "undefined") {
  pepezineo = {};
}
pepezineo.max_level = {1: 13, 2: 11, 3: 8, 4: 5};
pepezineo.update_card = {};
pepezineo.update_card.change_level_dropdown_list = function () {
  var value = this.value;
  var type = $(this).find(':selected').data('type');
  $('#level').empty();
  for (var i = 1; i <= pepezineo.max_level[type]; i++) {
    $('#level').append($('<option>', {
      value: i,
      text: '' + i
    }));
  }
}
$(window).on('load', function() {
  $('#name').on('change', pepezineo.update_card.change_level_dropdown_list);
});
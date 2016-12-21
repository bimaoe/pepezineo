if (typeof pepezineo === 'undefined') {
  pepezineo = {}
}
pepezineo.create_cards = {}
pepezineo.create_cards.new_card_input_cnt = 1;
pepezineo.create_cards.add_new_card_input = function() {
  curr_index = pepezineo.create_cards.new_card_input_cnt;
  pepezineo.create_cards.new_card_input_cnt++;
  var new_card_input = "<fieldset class=\"go-away\">" + 
    "<legend> Card " + pepezineo.create_cards.new_card_input_cnt + " </legend> " +
    "<div class=\"form-group\">" + 
      "<label for=\"name\"> Name: </label> " + 
      "<input type=\"text\" name=\"name" + curr_index + "\" class=\"form-control\">" +
    "</div> " +
    "<div class=\"form-group\">" +
      "<label for=\"type\"> Type: </label> " +
      "<input type=\"radio\" name=\"type" + curr_index + "\" value=\"common\" checked> Common " +
      "<input type=\"radio\" name=\"type" + curr_index + "\" value=\"rare\"> Rare " +
      "<input type=\"radio\" name=\"type" + curr_index + "\" value=\"epic\"> Epic " +
      "<input type=\"radio\" name=\"type" + curr_index + "\" value=\"legendary\"> Legendary" +
    "</div> " +
    "<div class=\"form-group\">" +
      "<label for=\"elixir\"> Elixir: </label> " +
      "<select name=\"elixir" + curr_index + "\" class=\"form-control\">" +
        "<option value=\"1\">1</option>" +
        "<option value=\"2\">2</option>" +
        "<option value=\"3\">3</option>" +
        "<option value=\"4\">4</option>" +
        "<option value=\"5\">5</option>" +
        "<option value=\"6\">6</option>" +
        "<option value=\"7\">7</option>" +
        "<option value=\"8\">8</option>" +
        "<option value=\"9\">9</option>" +
      "</select>" +
    "</div> " +
    "<div class=\"form-group\">" +
      "<label for=\"arena\"> Arena: </label> " +
      "<select name=\"arena" + curr_index + "\" class=\"form-control\">" +
        "<option value=\"0\">0</option>" +
        "<option value=\"1\">1</option>" +
        "<option value=\"2\">2</option>" +
        "<option value=\"3\">3</option>" +
        "<option value=\"4\">4</option>" +
        "<option value=\"5\">5</option>" +
        "<option value=\"6\">6</option>" +
        "<option value=\"7\">7</option>" +
        "<option value=\"8\">8</option>" +
        "<option value=\"9\">9</option>" +
        "<option value=\"10\">10</option>" +
      "</select>" +
    "</div> " +
  "</fieldset>";
  $("#new_card_inputs").append(new_card_input);
}
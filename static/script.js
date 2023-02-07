var children = $("#container").children();
$('#container').empty();
$('#container').append(children[0]);
$('#container').append(children[1]);
$('#container').append("<div style='clear:both;'></div>");
$('#container').append("<div id='panel1'></div>");
$('#container').append(children[4]);
$('#container').append("<div id='panel2'></div>");
$('#container').append("<div style='clear:both;'></div>");
$('#container').append(children[2]);
$('#container').append(children[3]);
var statistic = $('.statistic').children();
$('.statistic').remove();
$('#panel2').append(statistic);

function my_f(){
		var cards = $(".table").children();
		$('.table').empty();
		$('.table').append("<div class='play_cards'></div>");
		$('.play_cards').append(cards[0]);
		$('.play_cards').append(cards[1]);
		$('.play_cards').append("<div style='clear:both;'></div>");
		$('.play_cards').append(cards[2]);
		$('.play_cards').append(cards[3]);
	};
	
function tap_card(id) {
	var width = $('#'+id).width();
	if (width > 82) {
		$('#'+id).css('width','82px');
		$('#'+id).css('height','126px');
	};
	if (width == 82) {
		$('#'+id).css('width','100px');
		$('#'+id).css('height','150px');
	};
};

function check_player() {
	var id = $('#master_id').html();
	var path = '#id_'+(id-1);
	$(path).css('border-color','#c40000');
	$(path).css('box-shadow', '0 0 10px red');
}

setTimeout(() => {
		var main_form = $('#main_form').children();
		$('#main_form').empty();
		$('#panel1').append(main_form);
    }, 100);

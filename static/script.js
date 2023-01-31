$(document).ready(function(){
	var children = $("#container").children();
	$('#container').empty();
	$('#container').append(children[0]);
	$('#container').append(children[1]);
	$('#container').append(children[4]);
	$('#container').append(children[2]);
	$('#container').append(children[3]);
});
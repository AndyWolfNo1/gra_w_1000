var children = $("#container").children();
$('#container').empty();
$('#container').append(children[0]);
$('#container').append(children[1]);
$('#container').append("<div style='clear:both;'></div>");
$('#container').append("<div id='panel1' class='panel1'></div>");
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
	var mainForm = $('#main_form').children();
	var newFormDiv = document.createElement("div");
	newFormDiv.id = "form_div";
	//newFormDiv.style.position = "fixed";
	//newFormDiv.style.top = "-38%";
	//newFormDiv.style.left = "85%";
	newFormDiv.appendChild(mainForm[0]);
	newFormDiv.appendChild(mainForm[1]);
	$('#main_form').empty();
	$('#panel2').append(newFormDiv);
    }, 100);

function errorColors() {
	var div = document.getElementById("error");
	var colors = ["#ff6565", "#ff9999"];
	var i = 0;

	setInterval(function() {
	  div.style.background = colors[i];
	  i = (i + 1) % colors.length;
	}, 500);
};

function errorAlert() {
	$('body').css("background-image", "url('static/image/error_background_image.jpg')");
	var modal = document.createElement("div");
	modal.id = "error";
	modal.style.height = "130px";
	modal.style.width = "600px";
	modal.style.backgroundColor = "#b3b3b3";
	modal.style.borderRadius = "5px";
	modal.style.color = "black";
	modal.style.border = "1px solid red";
	modal.style.padding = "20px";
	modal.style.position = "fixed";
	modal.style.top = "50%";
	modal.style.left = "50%";
	modal.style.transform = "translate(-50%, -50%)";
	modal.style.zIndex = "1";
	var text = document.createElement("p");
	text.innerHTML = "Wystąpił nieoczekiwany zonk.<br>Nastąpi ponowne rozdanie kart.";
	text.style.fontWeight = "900";
	text.style.textShadow = "-1px -1px 1px red";
	text.style.fontSize = "24px";
	text.style.textAlign = "center";
	modal.appendChild(text);
	const button = document.createElement('button');
	button.id = "button";
	button.innerText = 'Ok';
	button.style.fontSize = "18px";
	button.style.position = "absolute";
	button.style.left = "50%";
	button.style.transform = "translateX(-50%)";
	button.addEventListener('click', () => {
		location.href="/game";
	})
	modal.appendChild(button);
	document.body.appendChild(modal);
	errorColors();
};

function chat() {
	var chatbox = document.getElementById("chatbox");
	var chatlog = document.getElementById("chatlog");
	var chatinput = document.getElementById("chatinput");
	var chatsend = document.getElementById("chatsend");

	chatsend.addEventListener("click", function() {
	  var message = chatinput.value;
	  chatlog.innerHTML += "<div class='chatmessage'>" + message + "</div>";
	  chatinput.value = "";
	});
};

function infoPanel() {
	var panel1 = document.getElementById("panel1");
	var terminal = document.createElement("div");
	var chatBox = document.createElement("div");
	var chatLog = document.createElement("div");
	var input = document.createElement("input");
	chatBox.id = "chatbox";
	chatLog.id = "chatlog";
	chatBox.style.position ="relative";
	chatBox.style.zIndex = "1";
	input.type = "text";
	input.id = "chatinput";
	input.style.position = "relative";
	input.style.zIndex = "1"; 
	chatBox.appendChild(input);
	const btt = document.createElement('button');
	btt.id = "chatsend";
	btt.innerText = 'wyślij';
	btt.style.position = "relative";
	btt.style.zIndex = "1"; 
	//chatBox.appendChild(btt);
	chatBox.appendChild(chatLog);
	terminal.id = "terminal";
	terminal.style.top = "20px";
	terminal.style.left = "10%";
	terminal.style.opacity = '.8';
	// terminal.appendChild(chatBox);
	panel1.appendChild(chatBox);
	panel1.appendChild(btt);
	panel1.appendChild(input);
	// panel1.appendChild(terminal);
	chat();
};

function writeTextInfo() {
  let i = 0;
  const div = document.getElementById("info");
  var text = document.getElementById("g_r");
  text = text.textContent;

  function type() {
    if (i < text.length) {
	  div.innerHTML += text.charAt(i);
	  if(text.charAt(i) == '.') {
		div.innerHTML += "<br>";
	  }
      i++;
      setTimeout(type, 50);
    }
  }

  type();
};

function cleanTable(number) {
	var num = parseInt(number);
	var playForm = document.getElementById("play_form");
	var newGameForm = document.getElementById("new_game");
	if (num == 6) {
		playForm.style.display = "none";
		setTimeout(function() {
			$(".table").empty();
		}, 2500);
		
		setTimeout(function() {
			newGameForm.style.display = "block";
		},3000);
		
		setTimeout(function() {
			var table = document.getElementById("tb");
			var info = document.createElement("div");
			info.id = "info";
			info.style.backgroundColor = "black";
			info.style.position = "relative";
			info.style.width = "55%";
			info.style.height = "55%";
			info.style.left = "20%";
			info.style.top = "20%";
			info.style.padding = "20px";
			info.style.opacity = ".7";
			table.appendChild(info);
			writeTextInfo();
		}, 3000);
	};
};


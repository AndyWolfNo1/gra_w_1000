var playerName = document.getElementById("un").innerHTML;
var clearDiv = document.createElement("div");
clearDiv.style.clear = "both";

var container = document.getElementById("container");
container.style.backgroundImage = "url('/static/image/start_panel/black_joker.jpg')";
var exitButton = document.createElement("button");
exitButton.innerHTML = "X";
exitButton.style.position = "relative";
exitButton.style.left = "97%";
exitButton.style.top = "-4%";
exitButton.style.width = "30px";
exitButton.style.height = "30px";

var deck = document.createElement("img");
deck.src = "/static/image/start_panel/deck.png"
deck.style.position = "relative";
deck.style.top = "20%";
deck.style.left = "40%";
deck.style.border = "0";
deck.style.width = "130px";
deck.style.transform =  "rotate(-16deg)";
var startButton = document.createElement("button");
startButton.style.position = "relative";
startButton.style.top = "7%";
//startButton.style.left = "5%";
startButton.style.fontSize = "20px";
startButton.innerHTML = "Zacznij grę";
startButton.onclick = function() {
	container.innerHTML = '';
	setTimeout(function() {
		container.style.removeProperty("background-image");
		},400);
	container.style.backgroundColor = "#5c5470";
};

function openGame(id, creator, startTime) {
	var tableImage = document.createElement("div");
	tableImage.appendChild(deck);
	tableImage.style.position = "relative";
	tableImage.style.top = "15%";
	tableImage.style.left = "30%";
	tableImage.style.backgroundImage ='url("/static/image/table.jpg")';
	tableImage.backgroundSize = "cover";
	tableImage.style.backgroundPosition = "50% 50%";
	tableImage.style.borderRadius = "5px";
	tableImage.style.width = "599px";
	tableImage.style.height = "299px";
	tableImage.style.boShadow = "0 0 10px #dbd8e3";

	var addGameButton = document.createElement("button");
	addGameButton.id = "add_game_button";
	addGameButton.style.position = "relative";
	addGameButton.style.top = "39%";
	addGameButton.style.left = "48%";
	addGameButton.style.fontSize = "25px";
	addGameButton.innerHTML = "Usiądź do gry";
	var startButton = document.createElement("button");
	startButton.style.position = "relative";
	startButton.style.top = "7%";
	startButton.style.fontSize = "20px";
	startButton.innerHTML = "Zacznij grę";
	startButton.onclick = function() {
		activateGame(id);
		showGame(id);
	};
	container.style.backgroundImage = "url('/static/image/start_panel/black_joker.jpg')";
	tableImage.appendChild(addGameButton);
	container.innerHTML = "";
	exitButton.onclick = function(){
		container.innerHTML = "";
		try {
			document.getElementById("start_div").innerHTML = '';
		} catch (e) {
		};
		
	};
	addGameButton.onclick = function() {
		addPlayer(playerName, id);
		var delButton =  document.getElementById("add_game_button");
		tableImage.removeChild(delButton);
	};
	addGameButton.addEventListener("click", function() {
		addGameButton.setAttribute("disabled", true);
		var startDiv = document.createElement("div");
		startDiv.id = "start_div";
		startDiv.style.borderRadius = "5px";
		startDiv.style.position = "relative";
		startDiv.style.top = "19%";
		startDiv.style.left = "0%";
		startDiv.style.color = "#dbd8e3";
		startDiv.style.height = "25%";
		startDiv.style.fontSize = "25px";
		startDiv.style.textAlign = "center";
		startDiv.style.backgroundColor = "#242222";
		startDiv.innerHTML = "Zaczekaj na innych graczy lub zacznij od razu.<br>";
		startDiv.appendChild(startButton);
		tableImage.appendChild(startDiv);
	});
	var subId = id.toString();
	subId = subId.substr(-4); 
	container.innerHTML = '<p> Gra id: '+subId+' utworzona przez '+creator+', czas utworzenia: '+ startTime+'</p>';	
	container.appendChild(exitButton);
	container.appendChild(tableImage);
	var table = document.createElement("table");
	table.style.position = "";
	table.style.width = "200px";
	var tr = document.createElement("tr");
	var trb = document.createElement("tr");
	var th = document.createElement("th");
	var thb = document.createElement("th");
	th.innerHTML = "Gracze przy tym stole:";
	tr.appendChild(th);
	table.appendChild(tr);
	thb.id = "th_players";
	trb.appendChild(thb);
	table.appendChild(trb);
	table.style.position = "relative";
	container.appendChild(table);
	checkPlayer(id);
};

function addPlayer(player, id) {
	var tablePlayers = document.getElementById("th_players");
	tablePlayers.innerHTML = '';
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/process", true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4 && xhr.status === 200) {
			var response = JSON.parse(xhr.response);
			liczbaElementow = 0;
			for (var klucz in response) {
				liczbaElementow++;
			};
			for(var i = 0; i < liczbaElementow; i++) {
				//document.getElementById("output").innerHTML += response[i];
				tablePlayers.innerHTML += "<p>"+response[i]+"</p>";
			};
		};
	};
	var data = JSON.stringify({"process": 0, "player": player, "id" : id});
	xhr.send(data);
};

function checkPlayer(id) {
	var tablePlayers = document.getElementById("th_players");
	tablePlayers.innerHTML = '';
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/process", true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4 && xhr.status === 200) {
			var response = JSON.parse(xhr.response);
			liczbaElementow = 0;
			for (var klucz in response) {
				liczbaElementow++;
			};
			for(var i = 0; i < liczbaElementow; i++) {
				tablePlayers.innerHTML += "<p>"+response[i]+"</p>";
			};
		};
	};
	var data = JSON.stringify({"process": 1, "id" : id});
	xhr.send(data);
};

function gameCreator(name) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/process", true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4 && xhr.status === 200) {
			var response = JSON.parse(xhr.response);
			openGame(response["id"], response["creator"], response["start_time"]);
		};
	};
	var data = JSON.stringify({"process": 2, "name" : name});
	xhr.send(data);
};

var createGameButton = document.createElement("button");
createGameButton.innerHTML = "Stwórz grę";
createGameButton.style.margin = "5px";
createGameButton.onclick = function(){
	gameCreator(playerName);
	printAllGames();
};

document.getElementById("tables").prepend(createGameButton);

function printAllGames() {
	var tableAllGame = document.createElement("table");
	tableAllGame.id = "table1";
	document.getElementById("tables").innerHTML = '';
	document.getElementById("tables").prepend(createGameButton);
	tableAllGame.innerHTML = "<tr><th>Id</th><th>Dodano</th><th>Graczy</th><th>Autor</th><th>Wejdż</th></tr>";
	
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/process", true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4 && xhr.status === 200) {
			var response = JSON.parse(xhr.response);
			liczbaElementow = 0;
			for (var klucz in response) {
				liczbaElementow++;
			};
			for(var i = 0; i < liczbaElementow; i++) {
				var subId = response[i]['id'].toString();
				subId = subId.substr(-4);
				var startButton = document.createElement("button");
				if (response[i]['activate'] == 0) {
					startButton.innerHTML = "Wejdź";
				};
				if (response[i]['activate'] == 1) {
					startButton.innerHTML = "Oglądaj";
				};
				var res_th_button = "th_button" + i.toString();
				var res_tr = "<tr><th>"+subId+"</th><th>"+response[i]['start_time']+"</th><th>"+response[i]['len_players']+"</th><th>"+response[i]['creator']+"</th><th id='"+res_th_button+"'></th></tr>";
				tableAllGame.innerHTML += res_tr;
				document.getElementById(res_th_button).appendChild(startButton);
				var parent = document.getElementById(res_th_button);
				parent.firstChild.id = subId;
				if (response[i]['activate'] == 0) {
					var openGameId = 'openGame('+response[i]['id']+',"'+response[i]['creator']+'","'+response[i]['start_time']+'")';
				};
				if (response[i]['activate'] == 1) {
					var openGameId = 'showGame('+response[i]['id']+')';
				};
				parent.firstChild.setAttribute('onclick', openGameId);
			};
		};
		document.getElementById("tables").appendChild(tableAllGame);
	};

	var data = JSON.stringify({"process": 3});
	xhr.send(data);
};
printAllGames();
setInterval(printAllGames, 5000);

function activateGame(id) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/process", true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4 && xhr.status === 200) {
			//document.getElementById("output").innerHTML = xhr.responseText;
		};
	};
	var data = JSON.stringify({"process": 5, "id" : id});
	xhr.send(data);
};

 function showGame(id) {
	var url = "http://localhost:5000/game/"+id;
	window.open(url, "_blank", "fullscreen=yes");
 };
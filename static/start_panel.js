function startPanel() {
	var container = document.getElementById("container");
	var greeting = document.getElementById("greeting");
	var logo_path = "/static/image/start_panel/logo.png";
	var logo = document.createElement("img");
	logo.src = logo_path;
	logo.style.top = "-5%";
	logo.style.left = "60%";
	logo.style.position = "absolute";
	logo.style.border = "0";
	greeting.appendChild(logo);
	//container.style.backgroundColor = "#dbd8e3";
};

function showPlay() {
	var play = document.createElement("div");
	var container = document.getElementById("container");
	play.id = "show_play";
	play.style.height = "620px";
	play.style.width = "400px";
	//play.style.backgroundColor = "#b3b3b3";
	play.style.backgroundImage = 'url("/static/image/start_panel/czacha.png")';
	play.style.backgroundSize = "cover";
	play.style.backgroundPosition = "50% 50%";
	play.style.borderRadius = "5px";
	play.style.color = "black";
	//play.style.border = "1px solid red";
	play.style.padding = "20px";
	play.style.position = "fixed";
	play.style.top = "600px";
	play.style.left = "50%";
	play.style.transform = "translate(-50%, -50%)";
	play.style.zIndex = "1";
	play.style.opacity = ".7";
	var button = document.createElement("button");
	button.id = "play_button";
	button.animation = "color-change 5s ease-in-out infinite";
	button.style.backgroundColor = "#dbd8e3";
	button.style.color = "#FF212F";
	button.style.fontFamily = "'Anton', sans-serif";
	button.style.borderRadius = "10px";
	button.style.fontSize = "38px";
	button.style.position = "absolute";
	button.style.top = "62%";
	button.style.left = "24%";
	button.innerHTML = 'Symulacja gry';
	button.onclick = function()
		{
		   dark_window();
		};
	button.onmouseover = function() 
	{
    this.style.backgroundColor = "#2a2438";
	};
	button.onmouseout = function() 
	{
    this.style.backgroundColor = "#dbd8e3";
	};
	play.appendChild(button);
	container.style.width = "80%";
	container.style.height = "900px";
	container.appendChild(play);
};

function addCrupier() {
	var container = document.getElementById("container");
	var img1 = document.createElement("img");
	var img2 = document.createElement("img");
	var div_crupier = document.createElement("div");
	div_crupier.id = "div_crupier";
	div_crupier.style.width = "300px";
	div_crupier.style.position = "fixed";
	div_crupier.style.top = "100px";
	img1.style.border = '0';
	img2.style.border = '0';
	img1.src = "/static/image/start_panel/krupier.png";
	img2.src = "/static/image/start_panel/japonka.png";
	img2.style.position = "fixed";
	img2.style.width = "550px";
	img2.style.top = "26%";
	img2.style.left = "64%";
	div_crupier.appendChild(img1);
	container.appendChild(div_crupier);
	container.appendChild(img2);
}

function eyes() {
	var div_crupier = document.getElementById("div_crupier");
	var eyes = document.createElement("img");
	eyes.id = "eyes";
	eyes.style.border = "0";
	eyes.style.position = "absolute";
	div_crupier.appendChild(eyes);
};

function switchEye1() {
	var eyes = document.getElementById("eyes");
	eyes.style.left = "56.6%";
	eyes.style.top = "10.5%"
	eyes.style.opacity = "1";
	eyes.src = "/static/image/start_panel/eyes_open.jpg";
};

function switchEye2() {
	var eyes = document.getElementById("eyes");
	eyes.style.left = "57%";
	eyes.style.top = "10.4%";
	eyes.src = "/static/image/start_panel/eyes_close.jpg";
};
function switchEye3() {
	var eyes = document.getElementById("eyes");
	eyes.style.opacity = "0";
};

function repeatFunction() {
	setTimeout(switchEye1, 4000);
	setTimeout(switchEye2, 4100);
	setTimeout(switchEye1, 4200);
	setTimeout(switchEye3, 4250);
	setTimeout(repeatFunction, 5000);
};

repeatFunction();

function openInfoWindow() {
  var WindowDoc = window.open('', '', "width=1000, height=500, top=150, left=320").document;
	WindowDoc.open();
};

function closeInfoWindow() {
  var WindowDoc = window.open('', '', "width=1000, height=500, top=150, left=320").document;
	WindowDoc.close();
};

function dark_window() {
	var div = document.createElement("div");
	var container = document.getElementById("container");
	div.style.position = "absolute";
	div.style.width = "100%";
	div.style.height = "120%";
	div.style.zIndex = "1";
	div.style.margin = "0";
	div.style.opacity = "0";
	div.style.backgroundColor = "black";
	div.style.top = "-2%";
	document.body.appendChild(div);
	document.body.style.backgroundColor = "black";
	var opacity = 0;
	var intervalId = setInterval(function () {
		opacity += 0.2;
		div.style.opacity = opacity;
		if (opacity >= 1) {
		  clearInterval(intervalId);
		}
	}, 200);
	
		setTimeout(function() {
			var opacity2 = 1;
			var intervalId2 = setInterval(function () {
				opacity2 -= 0.2;
				$('#show_play').css('opacity',opacity2);
				if (opacity2 <= 0) {
				  clearInterval(intervalId2);
				}
			}, 100);
		}, 2000);
		
		setTimeout(function() {
			window.location.replace("/game");
		}, 2000);
};

(function(){
	$(document).ready(function(){
		/** initializing variables **/
		var text = $("#typewriter").data("text").trim();
		var phrase = text.split(",");
		var phLength = phrase.length;
		var speed = $("#typewriter").data("speed") || 80;
		var delay = $("#typewriter").data("delay") || 5000;
		var action = "type";
		var textLength = text.length;
		var i = 0;
		var j = 0;
		/** method for typing text **/
		function typing(){
			var iText = $("#typewriter").html();
			if (action == "type"){
				if (i<textLength){
					$("#typewriter").append(text[i]);
					i++;
					setTimeout(typing,speed);
				}
				if (i == textLength){
					action = "erase";
					setTimeout(eraser,delay);
				}
			}
		}
		/** method for erasing text **/
		function eraser(){
			var iText = $("#typewriter").html();
			if (action == "erase"){
				if (i<=textLength){
					$("#typewriter").html(iText.substr(0,i));
					i = i-1;
					setTimeout(eraser,speed);
				}
				if (i == -1){
					i = 0;
					action = "type";
					setTimeout(typeWriter, delay/100);
				}
			}
		}
		// add caret
		$("#typewriter").wrap("<div style='font-size:inherit;min-height:inherit;'></div>");
		$("#typewriter").parent()[0].style.whiteSpace = "nowrap";
		$("#typewriter").after("<span class='color-white blink' style='-webkit-text-stroke:2px;font-size:inherit;font-weight:bold;word-spacing:-3px'>&nbsp;|</span>");

		/** method for simulating and alternating the typing text phrases **/
		function typeWriter(){
			text = phrase[j];
			textLength = text.length;
			typing();
			j++;
			if (j == phLength){
				j = 0;
			}
		}
		/** start type writer **/
		typeWriter();

	});
})(jQuery);
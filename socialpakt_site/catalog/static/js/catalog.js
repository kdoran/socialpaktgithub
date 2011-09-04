(function(globalscope, $){
	
	$(document).ready(function(){
		// Set up the countdown timer
		var expiresdate = $("#expiresdate").text();
		$('#expiresdate').countdown({ref_time: new Date(expiresdate), format: '%d Days %H:%M:%S'});

		// Set up the photobrowser
		$("div#shirt div.shirtimage").click(function(){
			var cur_sel = $("div#shirt div.shirtimage.big");
			var cur_sel_img = cur_sel.html();
			cur_sel.html($(this).html());
			$(this).html(cur_sel_img);
		});

		$("li.size").click(function(){
			$("#shirt_select").attr("value", $(this).attr("id"));
			$("li.size.selected").removeClass("selected");
			$(this).addClass("selected");
		});
	});

})(window, jQuery);
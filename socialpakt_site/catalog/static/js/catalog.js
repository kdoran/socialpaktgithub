(function(globalscope, $){
	
	$(document).ready(function(){
		// Set up the countdown timer
		var expiresdate = $("#expiresdate").text();
		$('#expiresdate').countdown({ref_time: new Date(expiresdate), format: '%d Days %H:%M:%S'});

		// Set up the photobrowser
		$("ul.photobrowser li.photo").click(function(){
			var cur_sel = $("ul.photobrowser li.photo.big");
			var cur_sel_img = cur_sel.html();
			cur_sel.html($(this).html());
			$(this).html(cur_sel_img);
		});
	});

})(window, jQuery);
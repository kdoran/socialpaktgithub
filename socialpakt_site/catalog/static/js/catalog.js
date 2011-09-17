(function(globalscope, $){
	var hovering = false;

	$(document).ready(function(){
		// Set up the countdown timer
		var expiresdate = $("#expiresdate").text();
		$('#expiresdate').countdown({ref_time: new Date(expiresdate), format: '%d Days %H:%M:%S'});

		// Set up the photobrowser
		$("div#shirt div.shirtimage.thumbnail").click(function(){
			var cur_sel = $("div#shirt div.shirtimage.big");
			var cur_sel_img = cur_sel.html();
			cur_sel.html($(this).html());
			$(this).html(cur_sel_img);
			$("div.shirtimage.thumbnail").animate({width:"10%"});
			$("div.shirtimage.big").animate({width:"81%"});
		});

		$("div.thumbnail").hover(
			function(){
				if ( hovering == false ) {
					$("div.shirtimage.thumbnail").animate({width:"50%"});
					$("div.shirtimage.big").animate({width:"41%"});
					hovering = true;
				}
			},
			function(){
				hovering = false;
				$("div.shirtimage.thumbnail").animate({width:"10%"});
				$("div.shirtimage.big").animate({width:"81%"});
			}
		);


		// Set up the size selector
		$("li.size").click(function(){
			$("#shirt_select").attr("value", $(this).attr("id"));
			$("li.size.selected").removeClass("selected");
			$(this).addClass("selected");
			$("#cartbutton").removeAttr("disabled").removeClass("disabled");

		});
	});

})(window, jQuery);
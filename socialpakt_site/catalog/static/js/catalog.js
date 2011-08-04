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

		$("#addtocartlink").click(function(){
			var add_to_cart_url = $("#variationselect").attr("value");
			var quantity = $("#quantityinput").attr("value");
			if (quantity.match(/\b\d+\b/)) {
				add_to_cart_url = add_to_cart_url.replace(/\/1\/$/, "/"+quantity+"/");
				window.location = add_to_cart_url;
			} else {
				window.alert("Quantity must be a number!");
			}
		});
	});

})(window, jQuery);
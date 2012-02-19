(function(globalscope, $){
	var hovering = false;

	var show_shirt_detail = function() {
		var detail_link = $("div#shirt div.shirtimage.big a.photodetail");
		if( detail_link.length > 0 ) {
			var detail_href = $(detail_link).attr("href");
			$.colorbox({href:detail_href});
		}
	}

	var show_shirt_detail_link = function() {
		if ( $("div#shirt div.shirtimage.big a.photodetail").length ) {
			$("a#photodetaillink").show();
		} else {
			$("a#photodetaillink").hide();
		}
	}

	$(document).ready(function(){
			// Set up the countdown timer
			var expiresdate = $("#expiresdate").text();
			
			var daysleft = expiresdate;
			if (daysleft == 1){
				$("#days").text("day");
			}

			$("#amountdonated").hoverIntent({
				over: makeTall, 
				timeout: 500, 
				out: makeShort
			});
			function makeTall(){$("#amountdonated_helper").fadeIn();}
			function makeShort(){$("#amountdonated_helper").fadeOut();}

			// Set up the photobrowser
			$("div#shirt div.shirtimage.thumbnail").click(function(){
				var cur_sel = $("div#shirt div.shirtimage.big");
				var cur_sel_img = cur_sel.html();
				cur_sel.html($(this).html());
				$(this).html(cur_sel_img);
				$("div.shirtimage.thumbnail").animate({width:"10%"});
				$("div.shirtimage.big").animate({width:"81%"});

				show_shirt_detail_link();
			});

		$("div#shirt div.shirtimage.big").click(function(){
			show_shirt_detail();
		});

		$("a#photodetaillink").click(function(){
			show_shirt_detail();
			return false;
		});

		// //thumbnail click swaps main photo
		// $('.photo_thumbnail').click(function(){
		// 	var this_class = "." + $(this).attr("class").split(" ")[0];
		// 	$(".photo_large").hide();
		// 	//class of thumbnail is class of large photo
		// 	$(this_class).show();
		// });

		$(".charity_logo").each(function(){
			var sub = $(this).text().split('/')[2];
			if (sub){
				var nakeddomain = sub.split("www.");
				if (nakeddomain.length > 1){
					$(this).text(nakeddomain[1]);
				}
				else {
					$(this).text(nakeddomain[0]);
				}
			}
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
		$("div.size").click(function(){
			$("#shirt_select").attr("value", $(this).attr("id"));
			$("div.size.selected").removeClass("selected");
			$(this).addClass("selected");
			$("#cartbutton").removeAttr("disabled").removeClass("disabled");

		});

		show_shirt_detail_link();
	});

})(window, jQuery);
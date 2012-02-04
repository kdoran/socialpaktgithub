$(document).ready(function() {
	// Shim placeholder text as necessary for input elements
	if(!Modernizr.input.placeholder){
		$("input").each(function(){
			if($(this).val()=="" && $(this).attr("placeholder")!=""){
				$(this).val($(this).attr("placeholder"));
				
				$(this).focus(function(){
					if($(this).val()==$(this).attr("placeholder")) $(this).val("");
				});
				
				$(this).blur(function(){
					if($(this).val()=="") $(this).val($(this).attr("placeholder"));
				});
			}
		});
	}
	// calculate percentage goal
	var goal = $("#donated_container").text() / $("#goal_container").text();
	$("#percentage_container").text(Math.round(goal*100));
	// truncate text (no ellipsis)
	$(".truncate_50").each(function(){
		$(this).text(($(this).text().trim().split(" ").slice(0,50).join(" ")));
	});
	$(".truncate_28").each(function(){
		$(this).text(($(this).text().trim().split(" ").slice(0,28).join(" ")));
	});

});
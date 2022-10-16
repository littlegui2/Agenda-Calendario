(function () {
	"use strict";

	var treeviewMenu = $('.app-menu');

	// Toggle Sidebar
	$('[data-toggle="sidebar"]').click(function(event) {
		event.preventDefault();
		$('.app').toggleClass('sidenav-toggled');
	});

	// Activate sidebar treeview toggle
	$("[data-toggle='treeview']").click(function(event) {
		event.preventDefault();
		if(!$(this).parent().hasClass('is-expanded')) {
			treeviewMenu.find("[data-toggle='treeview']").parent().removeClass('is-expanded');
		}
		$(this).parent().toggleClass('is-expanded');
	});

	// Set initial active toggle
	$("[data-toggle='treeview.'].is-expanded").parent().toggleClass('is-expanded');

	//Activate bootstrip tooltips
	$("[data-toggle='tooltip']").tooltip();

})();


$('.player-dropdown').on('change', function(e){
	e.preventDefault();
	selected_player_id = $('.player-dropdown').val();
	$.ajax({
		type : "POST",
		url: '/relatorio/' + selected_player_id + '/',
	dataType: 'json',
		success: function (data) {
			$('.details').empty();
			$.each(data, function (key, val) {
				$(".details").append("\
				<tr>\
				<td>"+val['first_name']+"</td>\
				<td>"+val['last_name']+"</td>\
				<td>"+val['age']+"</td>\
				</tr>\
				");
			});
		}
	});
  });
  
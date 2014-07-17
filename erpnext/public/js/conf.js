// Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.provide('erpnext');

// add toolbar icon
$(document).bind('toolbar_setup', function() {
	frappe.app.name = "ERPNext";

	$('.navbar-brand').html('<i class="icon-home"></i>')
	.attr("title", "Home")
	.addClass("navbar-icon-home")
	.css({
		"max-width": "200px",
		"text-overflow": "ellipsis",
		"white-space": "nowrap"
	});
});

frappe.provide('frappe.ui.misc');
frappe.ui.misc.about = function() {
	if(!frappe.ui.misc.about_dialog) {
		var d = new frappe.ui.Dialog({title: __('About')})

		$(d.body).html(repl("<div>\
		<h2>ERPNext</h2>  \
		<h4 class='text-muted'>"+__("Built on") + " Frappe Framework"+"</h4>  \
		<p>"+__("Open source ERP built for the web") + "</p>" +
		"<p>"+__("To report an issue, go to ")+"<a href='https://github.com/frappe/erpnext/issues'>GitHub Issues</a></p> \
		<p><a href='http://erpnext.org' target='_blank'>http://erpnext.org</a>.</p>\
		<p><a href='http://www.gnu.org/copyleft/gpl.html'>License: GNU General Public License Version 3</a></p>\
		<hr>\
		<p>&copy; 2014 Web Notes Technologies Pvt. Ltd and contributers </p> \
		</div>", frappe.app));

		frappe.ui.misc.about_dialog = d;
	}

	frappe.ui.misc.about_dialog.show();
}

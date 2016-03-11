# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "interventions_management"
app_title = "Interventions Management"
app_publisher = "Anybox"
app_description = "An app to manage interventions"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "smorele@anybox.fr"
app_version = "0.0.1"
app_license = "MIT"

role_home_page = {
    "technician": "intervention"
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/interventions_management/css/interventions_management.css"
# app_include_js = "/assets/interventions_management/js/interventions_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/interventions_management/css/interventions_management.css"
# web_include_js = "/assets/interventions_management/js/interventions_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "interventions_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "interventions_management.install.before_install"
# after_install = "interventions_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "interventions_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"interventions_management.tasks.all"
# 	],
# 	"daily": [
# 		"interventions_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"interventions_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"interventions_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"interventions_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "interventions_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "interventions_management.event.get_events"
# }


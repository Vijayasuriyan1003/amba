app_name = "amba"
app_title = "amba"
app_publisher = "vijay"
app_description = "amba"
app_email = "vijay@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# apps/amba/amba/hooks.py
# hooks.py
# hooks.py

# doc_events = {
#     "test_amba": {
#         "after_insert": "amba.amba.api.fetch_and_store_data",
#         # "on_update": "amba.amba.api..fetch_and_store_data"
#     }
# }


doc_events = {
    "test_amba": {
        "on_update": "amba.amba.api.sync_test_amba_with_vijay",
        "after_insert": "amba.amba.api.sync_test_amba_with_vijay",
        "on_trash": "amba.amba.api.sync_test_amba_with_vijay",
       
        
       
    }
}

scheduler_events = {
    "cron": {
        "17 17 * * *": [
            "amba.amba.api.sync_test_amba_with_vijay"
        ]
    }
}


# scheduler_events = {
#     "cron": {
#         "22 12 * * *": [
#             "amba.amba.api.fetch_and_store_data"
#         ]
#     }
# }









#
# doc_events = {
#     "vijay": {
#         "after_insert": "amba.amba.api.vijay_hooks.remove_previous_data",
#         "before_save": "amba.amba.api.vijay_hooks.fetch_and_store_data"
#     }
# }



# include js, css files in header of desk.html
# app_include_css = "/assets/amba/css/amba.css"
# app_include_js = "/assets/amba/js/amba.js"

# include js, css files in header of web template
# web_include_css = "/assets/amba/css/amba.css"
# web_include_js = "/assets/amba/js/amba.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "amba/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "amba/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "amba.utils.jinja_methods",
# 	"filters": "amba.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "amba.install.before_install"
# after_install = "amba.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "amba.uninstall.before_uninstall"
# after_uninstall = "amba.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "amba.utils.before_app_install"
# after_app_install = "amba.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "amba.utils.before_app_uninstall"
# after_app_uninstall = "amba.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "amba.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"amba.tasks.all"
# 	],
# 	"daily": [
# 		"amba.tasks.daily"
# 	],
# 	"hourly": [
# 		"amba.tasks.hourly"
# 	],
# 	"weekly": [
# 		"amba.tasks.weekly"
# 	],
# 	"monthly": [
# 		"amba.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "amba.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "amba.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "amba.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["amba.utils.before_request"]
# after_request = ["amba.utils.after_request"]

# Job Events
# ----------
# before_job = ["amba.utils.before_job"]
# after_job = ["amba.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"amba.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


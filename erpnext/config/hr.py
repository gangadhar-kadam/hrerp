from frappe import _

data = [
	{
		"label": _("Documents"),
		"icon": "icon-star",
		"items": [
			{
				"type": "doctype",
				"name": "Employee",
				"description": _("Employee records."),
			},
			{
				"type": "doctype",
				"name": "Salary Slip",
				"description": _("Monthly salary statement."),
			},
			{
				"type": "doctype",
				"name": "Leave Application",
				"description": _("Applications for leave."),
			},
			{
				"type": "doctype",
				"name": "Attendance",
				"description": _("Attendance record."),
			},
			{
				"type": "doctype",
				"name": "Self Appraisal Form",
				"description": _("Self Appraisal Form record."),
			},
			{
				"type": "doctype",
				"name": "Performance Appraisal Form",
				"description": _("Performance Appraisal Form record."),
			},
			{
				"type": "doctype",
				"name": "Appraisal Rate Score Card",
				"description": _("Appraisal Rate Score Card Information."),
			},
			{
				"type": "doctype",
				"name": "Expense Claim",
				"description": _("Claims for company expense."),
			},
			{
				"type": "doctype",
				"name": "Appraisal",
				"description": _("Performance appraisal."),
			},
			{
				"type": "doctype",
				"name": "Job Applicant",
				"description": _("Applicant for a Job."),
			},
			{
				"type": "doctype",
				"name": "Job Opening",
				"description": _("Opening for a Job."),
			},
		]
	},
	{
		"label": _("Tools"),
		"icon": "icon-wrench",
		"items": [
			{
				"type": "doctype",
				"name": "Salary Manager",
				"label": _("Process Payroll"),
				"description":_("Generate Salary Slips"),
				"hide_count": True
			},
			{
				"type": "doctype",
				"name": "Upload Attendance",
				"description":_("Upload attendance from a .csv file"),
				"hide_count": True
			},
			{
				"type": "doctype",
				"name": "Leave Control Panel",
				"label": _("Leave Allocation Tool"),
				"description":_("Allocate leaves for the year."),
				"hide_count": True
			},
		]
	},
	{
		"label": _("Setup"),
		"icon": "icon-cog",
		"items": [
			{
				"type": "doctype",
				"name": "HR Settings",
				"description": _("Settings for HR Module")
			},
			{
				"type": "doctype",
				"name": "Employee",
				"description": _("Employee master.")
			},
			{
				"type": "doctype",
				"name": "Employment Type",
				"description": _("Types of employment (permanent, contract, intern etc.).")
			},
			{
				"type": "doctype",
				"name": "Branch",
				"description": _("Organization branch master.")
			},
			{
				"type": "doctype",
				"name": "Department",
				"description": _("Organization unit (department) master.")
			},
			{
				"type": "doctype",
				"name": "Designation",
				"description": _("Employee designation (e.g. CEO, Director etc.).")
			},
			{
				"type": "doctype",
				"name": "Salary Structure",
				"description": _("Salary template master.")
			},
			{
				"type": "doctype",
				"name": "Earning Type",
				"description": _("Salary components.")
			},
			{
				"type": "doctype",
				"name": "Deduction Type",
				"description": _("Tax and other salary deductions.")
			},
			{
				"type": "doctype",
				"name": "Leave Allocation",
				"description": _("Allocate leaves for a period.")
			},
			{
				"type": "doctype",
				"name":"Leave Type",
				"description": _("Type of leaves like casual, sick etc."),
			},
			{
				"type": "doctype",
				"name": "Holiday List",
				"description": _("Holiday master.")
			},
			{
				"type": "doctype",
				"name": "Leave Block List",
				"description": _("Block leave applications by department.")
			},
			{
				"type": "doctype",
				"name": "Appraisal Template",
				"description": _("Template for performance appraisals.")
			},
			{
				"type": "doctype",
				"name": "Expense Claim Type",
				"description": _("Types of Expense Claim.")
			},
			{
				"type": "doctype",
				"name": "Jobs Email Settings",
				"description": _("Setup incoming server for jobs email id. (e.g. jobs@example.com)")
			},
		]
	},
	{
		"label": _("Standard Reports"),
		"icon": "icon-list",
		"items": [
			{
				"type": "report",
				"is_query_report": True,
				"name": "Employee Leave Balance",
				"doctype": "Leave Application"
			},
			{
				"type": "report",
				"is_query_report": True,
				"name": "Employee Birthday",
				"doctype": "Employee"
			},
			{
				"type": "report",
				"name": "Employee Information",
				"doctype": "Employee"
			},
			{
				"type": "report",
				"is_query_report": True,
				"name": "Monthly Salary Register",
				"doctype": "Salary Slip"
			},
			{
				"type": "report",
				"is_query_report": True,
				"name": "Monthly Attendance Sheet",
				"doctype": "Attendance"
			},
		]
	},
]

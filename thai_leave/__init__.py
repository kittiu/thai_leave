__version__ = "0.0.1"

import hrms.hr.doctype.leave_application.leave_application as leave
from thai_leave.custom.leave_application import get_number_of_leave_days
leave.get_number_of_leave_days = get_number_of_leave_days

import hrms.hr.doctype.leave_application.leave_application as leave
from thai_leave.custom.leave_application import get_leaves_for_period
leave.get_leaves_for_period = get_leaves_for_period

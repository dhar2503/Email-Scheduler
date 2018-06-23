application_title = "Email_Scheduler_App"
main_python_file = "C:\Python27\Email_Scheduler.py"


import sys

from cx_Freeze import setup, Executable

setup(
	name = application_title,
	version = "0.1",
	description = "Application useful for Scheduling Email",
	executables = [Executable(main_python_file)])
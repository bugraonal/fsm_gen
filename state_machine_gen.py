"""
This program is a state machine generator usign Graphviz tool. 
This program will read a Verilog module (possibly VHDL module in the future) 
and create a state machine based on the lines of codes from the module, starting
from the indicated line number. 
This program is intended to be used with Notepad++'s "Run" command.
Only state machines done using "case" statement are supported.
State transitions out of the "case" block are not supported.
"""

import os
import re

# These are the compiled Regular Expression modules 

# Will match a white-spaced line that only contains "begin" 
re_begin = re.compile("\s*begin\s*\r\n")
# Will match a ternary if conditions
re_ternary = re.compile("\s*\w+\s*=\s*\(\s*\w+\s*\)?\s*\w+\s*(:\s*\w+\s*)[0,1];")

def parse_line(line):
	"""
	This function will parse a line, determining it's purpose
	Examples of the possible kinds of lines are:
		|PATTERN|									|TYPE|					|MULTI-LINE|
		- case(state) 								-> "begin case"				
		- STATE_NUM: CODE 							-> "single line state" 		
		- STATE_NUM: begin 							-> "begin state"			
		- STATE_NUM:								-> "state label"			x
		- begin										-> "begin"					x
		- if (CONDITION)							-> "single line if"
		- if (CONDITION) begin						-> "if"
		- VARIABLE = (CONDITION)? VALUE : VALUE;	-> "ternary if"
		- CODE										-> "code"					
		- end										-> "end"					
		- endcase									-> "end case"				
	Multi-line section of the table refers to the fact that these conditions
	can be removed by combining multi-lines. These conditions will not be 
	taken into consideration
	"""
	global re_begin, re_ternary
	if ("case(" in line):
		# begin case
		# needed for begin-end stack
		# need to extract state varibale name
	elif (":" in line):
		if ("begin" in line):
			# begin state
			# need to extract state label
		else:
			# single line state
			# need to extract state label
			# also need to look for state transition
	elif ("endcase" in line):
		# end case
	elif ("end" in line):
		# end
	elif ("if" in line):
		if ("begin" in line):
			# if
		else:
			# single line if
	elif (re_ternary.match(line) not None):
		# ternary if
	else:
		# code
		
# File path to the RTL module
file_path = os.argv[1]
# The line number the state machine start at (.ex case(state))
line_num = int(os.argv[2])
# Stack for holding the if conditions
begin_end_stack = []
# Flag indicating that the code is within a case statement
is_case = False

with f as open(file_path, "w"):
	line = f.readline()
	ret = parse_line(code)
	if (): # is a case begin statement
		in_case = True

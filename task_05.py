#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A program that asks the user their blood pressure"""

#"""This program allows a user to input thier blood pressure
#and based on entry it will print out a message stating status"""

BP = int(raw_input('What is your blood pressure?  '))
"""This entry below sets the stage for the first entry, starting at zero
and accepts anything below or equal to 89."""
if BP <= 89:
    BP_STATUS = 'low'
elif BP >= 90 and BP <= 119:
    BP_STATUS = 'Ideal'
elif BP >= 120 and BP <= 139:
    BP_STATUS = 'Warning!'
elif BP >= 140 and BP <= 159:
    BP_STATUS = 'High!'
else:
    BP_STATUS = 'Emergency!'

print "Your status is currently: {}".format(BP_STATUS)

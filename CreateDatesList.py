from datetime import datetime
from datetime import timedelta

with open('DRAWING.txt','r') as f:
    file_lines = f.readlines()

Nlines = len(file_lines)
Ncolumns = len(file_lines[0])-1 # trailing white space character

if Ncolumns<>51:
    raise Exception("DRAWING.txt Error: number of columns should be 51, or script should be adjusted.")

if Nlines<>7:
    raise Exception("DRAWING.txt Error: number of lines should be 7, or script should be adjusted.")

# Output:
# List of dates corresponding to pixels in the drawing.

# Information about the drawing:
on = '%'
off = '.'

# Column 51, Row 1 corresponds to the following date:
start_date = datetime(2016,8,7,1,0,0)
seven_days = timedelta(days=7)
one_day    = timedelta(days=1)



master_list = []

for jcol in range(Ncolumns):
    # Column jcol corresponds to the week,
    # where jcol=51 corresponds to start_date
    # meaning we are 51 - jcol weeks out from start_date
    #
    # start_date - (7 days/week)*(51 - jcol weeks)
    #
    base_date = start_date - (51-jcol)*seven_days

    for irow in range(Nlines):
        # Row irow corresponds to which day of the week
        # 0 = Sunday, 1 = Monday, ..., 6 = Saturday
        #
        # base_date + (1 day)*(irow days)
        #
        this_date = base_date + one_day*irow

        c = file_lines[irow][jcol]
        if c is on:
            # add the date to the list
            master_list.append(this_date)

with open('DATES.txt','w') as f:
    for i in master_list:
        f.write(i.isoformat()+"\n")

# Loop structure:
# Horizontal movement = 7 days change
# Vertical movement = 1 day change







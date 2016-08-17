from datetime import datetime
from datetime import timedelta


def CreateDatesList( input_file='DRAWING.txt', 
                     output_file='DATES.txt',
                     Nc=51, Nr=7, 
                     start_date=datetime(2016,8,7,1,0,0) ):


    with open(input_file,'r') as f:
        file_lines = f.readlines()
    
    Nlines = len(file_lines)
    Ncolumns = len(file_lines[0])-1 # trailing white space character
    
    if Ncolumns<>Nc:
        raise Exception("DRAWING.txt Error: number of columns should be %d, or script should be adjusted."%(Nc))
    
    if Nlines<>Nr:
        raise Exception("DRAWING.txt Error: number of lines should be %d, or script should be adjusted."%(Nr))
    
    # Output:
    # List of dates corresponding to pixels in the drawing.
    
    # Information about the drawing:
    on = '%'
    off = '.'
    
    # Column 51, Row 1 corresponds to the following date:
    ###start_date = datetime(2016,8,7,1,0,0)
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
    
    with open(output_file,'w') as f:
        for i in master_list:
            f.write(i.isoformat()+"\n")

    


if __name__=="__main__":
    drawing_file = 'DRAWING.txt'
    dates_file = 'DATES.txt'
    CreateDatesList(drawing_file, dates_file, 
                    51,7,datetime(2016,8,7,1,0,0))
    print "Finished making dates file: ", output_file


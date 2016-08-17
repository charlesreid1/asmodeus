# Input: DRAWING.txt
#   Create dates list
# Output: DATES.txt
#
# Input: DATES.txt
#   Script generator
# Output: doit.sh

if __name__=="__main__":

    drawing_file = 'DRAWING.txt'
    dates_file = 'DATES.txt'

    # Create dates list
    from CreateDatesList import CreateDatesList
    CreateDatesList(drawing_file, dates_file,
                    51,7,datetime(2016,8,7,1,0,0))

    # Script generator
    # 
    # (assumes populated repo)
    github_repo = 'confused-cat'
    ScriptGenerator(github_repo,dates_file)


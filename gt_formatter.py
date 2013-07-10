import glob

# process all CSV files in 'input' folder, write modified CSV to 'output' folder  
for filename in glob.glob("input/*.csv"):  
    # flag to skip input lines  
    skip = 1  
    # open input file  
    with open(filename) as f:  
       # open output file for writing  
       with open(filename.replace("input","output"), "w") as o:  
           # get all lines  
           lines = f.readlines()  
           # process each line  
           for line in lines:  
              # check for start of Week report  
              if skip and line.startswith("Week,"):  
                  # stop skipping lines  
                  skip = 0  
                  # output modified CSV header  
                  o.write( line.replace("Week,", "date,") )  
              elif not skip:  
                  # match blank lines  
                  if line == '':  
                     # skip remainder of input file  
                     skip = 1  
                     break  
                  else:  
                     # remove start date (leaving end date in first column)  
                     data = line.split(" ") # split on space  
                     if len(data) == 3:  
                         fields = data[2].split(",") # split on comma  
                         # count number of fields  
                         if len(fields) == 2 and fields[1] <> '':  
                            # numeric value is present, write row to output  
                            o.write( data[2] )  
                         else:  
                            # numeric value missing after comma, report done  
                            skip = 1  
                            break  
                     else:  
                         # input line doesn't conform  
                         skip = 1  
                         break
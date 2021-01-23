
filenames = ['file1.txt', 'file2.txt'] 
  
# Open file3 in write mode 
with open('file3.txt', 'w') as outfile: 
  
    
    for names in filenames: 
  
        # Open each file in read mode 
        with open(names) as infile: 
  
          
            outfile.write(infile.read()) 
        # Add '\n' to enter data of file2 
        outfile.write("\n") 

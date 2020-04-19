import csv

output = []
with open("address - address.csv", 'r') as my_file:
    
    
    for line in my_file:
        x= line.split(',')
        #if 'Ontario\n' in x:
        if x[3].strip() == "Ontario": 
            print(x[0]+ " " + x[1]+ " " + x[2])
        

      




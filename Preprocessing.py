import csv

input_data = open('Data.csv', 'r')
output_data = open('Mining.csv', 'w')

Data = csv.reader(input_data, delimiter=',')

output_data.write("Brand, Processor, RAM, OS , Display, Touch, Price \n" )
arr = ["Brand", "Processor", "RAM", "OS" , "Display", "Touch", "Price"]

flag = 0
for row in Data:
    if flag == 0:
        flag = 1
        continue
    count = 0
    for column in row:
        if count == 0 or count == 2 :
            Brand = column.split(" ")[0]
            output_data.write(Brand + ",")
        elif count == 1 or count ==3 :
            Processer = column.split(" ")
            print Processer
            Processer = Processer[0] + Processer[1] + Processer[2]
            output_data.write(Processer + ",")            
        elif count == 4:
            Display = column.split(" ")[0]
            output_data.write(Display + ",")             
            if "Touchscreen" in column:
                output_data.write("1,")
            else:
                output_data.write("0,")
        else:
            output_data.write(column)
        count += 1
       
    output_data.write("\n")
        
input_data.close()
output_data.close()
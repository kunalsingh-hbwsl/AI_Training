import csv
# Part a
# with open('/home/kunalsingh/Downloads/export_catalog_product_20251006_105554.csv', 'r') as file:
#     reader = csv.reader(file)
#     headers_to_include = ["sku","name", "short_description", "description", "categories", "additional_attributes"]
#     indexes_of_headers=[]
#     for row in reader:
#         for i in range(0,len(row)):
#             if row[i] in headers_to_include:
#                 indexes_of_headers.append(i)
#         break
#     print(indexes_of_headers)

#     with open('output/data1.xlsx','w') as output:
#         writer=csv.writer(output)
#         writer.writerow(tuple(headers_to_include))
#         for row in reader:
#            writer.writerow((row[0],row[4],row[6],row[7],row[8],row[46]))

#Part B  
# with open('output/data1.xlsx','r') as excel_output:
#     reader =csv.reader(excel_output)
#     next(reader)
#     i=0
#     with open('output/is_enabled.xlsx','w') as output2:
#         writer=csv.writer(output2)
#         for row in reader:
#             try:
#                 is_enabled=row[5].split(',')[6]
#                 if "Yes" in is_enabled:
#                     writer.writerow((row[0],row[1],row[2],row[3],row[4],row[5]))
#             except:
#                 print("no is_enabled present at",i)
#             i+=1

#Part C



       
            
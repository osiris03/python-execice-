"""Write all content of a given file into a new file by skipping line number 5"""
with open('file_dict/text.txt','r') as fp: 
    lines = fp.readlines()
    print(lines)
    
with open('file_dict/new_text.txt','w') as fp:
    count = 0 
    for line in lines:
        if count==4:
            count+=1
            continue
        else:
            fp.write(line)
        count+=1
with open('file_dict/new_text.txt','r') as fp:
    print(fp.read())

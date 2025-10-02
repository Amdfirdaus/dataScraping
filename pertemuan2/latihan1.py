import os
print(os)

def ucapan (text):
    print(text)
    
ucapan ("hai asssalamualaikum")

def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        
create_directory("scraping")

def create_new_file (path):
    f=open(path,'w')
    f.write("")
    f.close()
    
create_new_file("scraping/test.txt")

def write_to_file(path,data):
    with open (path,'a')as file:
        file.write(data + '\n')

write_to_file("scraping/test.txt", "Ini baris pertama")
write_to_file("scraping/test.txt", "Anda adalah seorang programmer yang handal")


def clear_file(path):
    f=open(path,'w')
    f.close()
    
clear_file("scraping/test.txt")

def does_file_exist(path):
    return os.path.isfile(path)

print (does_file_exist("scraping/file.txt"))

def read_data(path):
    with open(path, 'rt') as file:
        for line in file:
            print(line)
            
def remove_file(path):
    if does_file_exist(path):
        os.remove(path)
    else:
        print("file tidak ada")
        
remove_file("scraping/file1.txt")
    
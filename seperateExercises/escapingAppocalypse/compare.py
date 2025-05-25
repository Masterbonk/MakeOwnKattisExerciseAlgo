def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read().strip()
        content2 = f2.read().strip()
        
        if content1 != content2:
            print("Not correct")
            return None
    print("Correct")
        

compare_files('output1.txt', 'outputReal.txt')
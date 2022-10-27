def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    for i in data.split("\n"):
        if i.isdigit():
            a.append(int(i))
    return a
    
# Read data from file
f=open("./txt_file/data05.txt")
data=f.read()
print(main(data))
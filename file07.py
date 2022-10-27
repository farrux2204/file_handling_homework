def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=0
    for i in data:
        if i.isdigit():
            a += int(i)
    return a
# Read data from file
f=open("./txt_file/data07.txt") 
data=f.read() 
print(main(data))
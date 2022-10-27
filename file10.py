def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x=data.split('\n')
    a=[]
    for i in x:
        a.append(len(str(i)))
    return max(a)

# Read data from file
f=open("./txt_file/data10.txt")
data=f.read()
print(main(data))
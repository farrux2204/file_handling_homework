def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=0
    for i in data:
        if i.isdigit():
            if a>int(i):
                a=int(i)
    return a

# Read data from file
# Read data from file
f=open("./txt_file/data09.txt")
data=f.read()
print(main(data))
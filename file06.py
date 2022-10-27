def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str   
    Returns:
        list: return answer
    """
    ls=data.split('\n')
    ans=[]
    for i in ls:
        ans.append(len(str(i)))
    return ans
# Read data from file
f=open("./txt_file/data06.txt")
data=f.read()
print(main(data))
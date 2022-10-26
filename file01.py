def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ls=data.split(',')
    ans=[]
    for i in ls:
        ans.append(int(i))
    return ans
f=open("./txt_file/data01.txt")
data=f.read()
print(main(data))
# Read data from file
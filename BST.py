class node:
    left=None
    data=None
    right=None
    
root=None

def insert():
    if(root==None):
        info=int(input("Enter the data "))
        n=node()
        global root
        root=n
        n.data=info
        n.left=None
        n.right=None
    else:
        info=int(input("Enter the data "))
        n=node()
        n.data=info
        n.left=None
        n.right=None
        
        x=root
        
        while(x!=None):
            y=x
            if(info<x.data):
                x=x.left
            else:
                x=x.right
        if(y.data>info):
            y.left=n
        else:
            y.right=n

def inorder(root):
        if(root==None):
            return
        else:
            inorder(root.left)
            print(root.data)
            inorder(root.right)

if __name__=="__main__":
    c=1
    while(c):
        insert()
        c=int(input("Want ot enter more Y/N"))
    z=root
    inorder(z)


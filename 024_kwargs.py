# **kwargs packs all arguments into a disctionary
def hello(**kwargs):
    for key, value in kwargs.items():
        print(value, end=" ")
    
hello(title="Mr.", first="peter", second="parker", third="jack")
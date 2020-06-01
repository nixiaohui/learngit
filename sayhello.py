from getName import get_name

def say_hello(name="NoBody"):
    print("Hi,", name)
    
if __name__ == "__main__":
    name = get_name()
    say_hello("hugo")
    say_hello(name)

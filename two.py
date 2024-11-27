#two.py
import one
def two():
    print('Hello, this is the  two.py pyhton file')
two()
one.one()
if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is imported")



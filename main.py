from atcoder import result as atcoder
from codeforces import result as codeforces
from codechef import result as codechef

def main():
    choice = input("Which file to process? (1/2/3): ")

    if choice == '1':
        output = atcoder()
    elif choice == '2':
        output = codeforces()
    elif choice == '3':
        output = codechef()
    print(output)

if __name__ == "__main__":
    main()
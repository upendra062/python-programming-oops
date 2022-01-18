#With for loop else gets executed if for loop normaly ended ie without break

khana=["Roti", "Chawal", "Dal"]

for item in khana:
    print(item)
    if item=="Dal" :
        break
#
#
else:
    print("This for loop is ended properly")




class mine:
    def recur(self, num):
        print(num, end="")
        if num > 1:
            print(" * ",end="")
            return num * self.recur(self, num-1)
        print(" =")
        return 1

def main():
    # a = mine()
    print(mine.recur(mine, 10))

main()
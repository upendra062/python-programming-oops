# lst=["soap", "vegetables", "tea", "coffee"]
#
# i=1
# for item in lst:
#     if i % 2 is not 0:
#         print(f"Buy this item: {item}")
#     i+=1

# for index, item in enumerate(lst):
#     print(f"{index} : {item}")
#     if index%2==0:
#         print(f"Buy this item: {item}")


lst=["soap", "vegetables", "tea", "coffee", "upendra", "singh", "bhadauria"]
for index, item in enumerate(lst):
    if index%3==0:
        print("The even number of :", index, " Item is: ",item)
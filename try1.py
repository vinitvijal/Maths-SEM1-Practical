# def main():
#     s1 = input('Enter the first string : ')
# #     s2 = input('Enter the second string : ')
# #     print('The indices of all the occurrences: ', end='') 
# #     l1 = []
# #     if s2 in s1:
# #         for i in range(len(s1)):
# #             if s1.startswith(s2, i):
# #                 l1.append(i)
# #         print(l1)
# #     else:
# #         print(-1)
# # # main()

# # # l1 = [1,2,3,4,5,6]
# # # print([i**3 for i in l1 if i % 2 == 0])

# # s = 'hello i am a string'
# # a = 5
# # b = 10

# # print(a ,'+', b, '=', a+b)

# # print(f'{a} + {b} = {a+b}')



# # # print(' '.join(s.split()[::-1]))

# # # 1
# # # 23
# # # 345
# # # # 4567
# # x = 1
# # for i in range (6):
# #     for j in range(i):
# #         print(x, end=' ')
# #         x+=1
# #     x=(i+1)
# #     print()

# x=1
# for i in range(6):
#     for j in range(i):
#         print(i, end=" ")
#     print()
    

# class Rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def area(self):
#         return self.l*self.b
    
#     def perimeter(self):
#         return 2*(self.l+self.b)
    
# a= Rectangle(10,20)
# print(a.area(), a.perimeter())

# class Circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return (22/7)*self.r*self.r
    
# b= Circle(7)
# print(b.area())








a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(list(x))


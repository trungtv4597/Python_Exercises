import turtle

def make_window(color, title):
    '''
        Thiết lập cửa với nền và tiêu đề cho trước.
        Return về cửa sổ mới.
    '''
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window

def make_turtle(color, size):
    '''
        Thiết lập một turtle với màu và độ lớn cho trước.
        Return về turtle mới.
    '''
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    return animal

def cau1(john, side_length):
    '''
        Câu 1: Việt mộ void function để vẽ 5 hình vuông theo điều kiện.
            Điều kiện: vẽ với một con trỏ duy nhât, cả 5 hình tách biệt nhau với cạnh là 20 đơn vị.
        Gợi ý: vị trí con trỏ không thuộc báp cứ hình vẽ nào. 
            Nói các khác con trỏ di chuyển tới một vị trí mới rồi mới vẽ hình tiếp theo.
    '''
    # thực hiện 5 lần
    for j in range(5):
        # vẽ một hình vuông.
        for i in range(4):
            john.forward(side_length*2*(j+1))
            john.left(90)
        john.penup()                            # dừng vẽ
        john.setpos((side_length*2*(j+1)),0)    # di truyển để tọa độ (x, y) tùy chon
        john.pendown()                          # vẽ tiếp

def cau2(john, side_length):
    '''
        Câu 2: Viết một chương trình để vẽ 5 hình vuông theo điều kiện.
            Điều kiện: tất cả hình đều tách biệt và lồng vào nhau, hình gốc có độ dài cạnh là 20 và hình càng ở ngoài thì càng lớn hơn 20 đơn vị.  
    '''
    # thực hiện 5 lần
    for j in range(5):
        # vẽ một hình vuông.
        for i in range(4):
            john.forward(side_length)
            john.left(90)
        vi_tri = john.pos()         # xác định tọa độ(x, y) của hình hiện thời
        x, y = vi_tri[0], vi_tri[1] # lưu tọa độ lấy được ở trên
        john.penup()                # dừng vẽ
        john.setpos(x-10, y-10)     # di truyển để tọa độ (x, y) tùy chon
        john.pendown()              # vẽ tiếp
        side_length += 20           # tăng chiều lên theo điều kiện

def draw_poly(john, n, side_length, angle):
    '''
        Câu 3: Viết một void-function một hình đa giác theo mẫu.
            Điều kiện: hình đa giác có 8 cạnh và dài 50 đơn vị.
        Gợi ý: draw_poly(tên, số cạnh, chiều dài)
    '''
    for _ in range (n):
        john.forward(side_length)
        john.left(angle)

def cau4(john, side_length):
    '''
        Câu 4: Vẽ hình theo mẫu.
    '''
    for _ in range(18):
        # vẽ một 1 hình vuông
        for _ in range(4):
            john.forward(side_length)
            john.left(90)
        john.right(20) # mỗi lần quay 20 độ, thì sao 18 lần sẽ là 360, tức là một vòng tròn.

def cau5_a(john, n, side_length):
    '''
        Câu 5: Vẽ 2 hình xoắn ốc theo mẫu mà hai hình chỉ thay đổi về giá trị góc quay.
    '''
    for _ in range(n):
        side_length = side_length + 3
        john.right(90)
        john.forward(side_length)
def cau5_b(john, n, side_length):
    '''
        Câu 5: Vẽ 2 hình xoắn ốc theo mẫu
    '''
    for _ in range(n):
        side_length = side_length + 3
        john.right(100)
        john.forward(side_length)

def draw_equitriangle(john, side_length):
    '''
        Câu 6: Sử dụng hàm draw_poly ở cây trước để vẽ một tam giác đều.
            Gợi ý: draw_equitriangle(tên, độ dài mỗi cạnh), tam giác đều thì mỗi góc 60 độ.
    '''
    angle = 180 - 60 # lấy 60 độ 
    draw_poly(john, 3, side_length, angle)

def sum_to(n):
    '''
        Câu 7: Viết một hàm fruitful mà trả về tổng các số integer từ 1 tới một số n nào đó.
            Gợi ý: sum_to(10) sẽ là 1+2+3+4+...+10 và return về 55
    '''
    j = 0
    for i in range(1, n+1):
        j = j + i
    print(j)
    return j

def area_of_circle(r):
    '''
        Câu 8: Viết một hàm fruitful tìm diện tích hình tròn có cho trước bán kính r.
    '''
    # s = pi * r^2
    s = (3.14) * r**2
    print('diện tích hình tròn là: ', s)
    return(s)

def draw_a_star(john, side_length):
    '''
        Câu 9: Viết một hàm void để vẽ một ngôi sao như mẫu có mỗi cạnh 100 đơn vị.
            Gợi ý: mỗi góc nên là 144 độ
    '''
    angle = 144
    john.right(180 - angle)
    draw_poly(john, 5, side_length, angle)

def draw_multiple_stars(john, number_star, side_length):
    '''
        Câu 10: Cải thiện hàm câu 9 để vẽ 5 ngôi sao như mẫu có mỗi cạnh 100 đơn vị.
            Gợi ý: mỗi hình cách nhau 350 đơn vị, rồi quay phải 144 độ.
    '''
    angle = 144
    john.right(180 - angle)
    for _ in range(number_star):
        draw_poly(john, 5, side_length, angle)
        john.penup()
        john.forward(350)
        john.left(angle)
        john.pendown()

wn = make_window('green', 'chapter 4')
john = make_turtle('hotpink', 2)

# ĐÁP ÁN:
cau1 = cau1(john, 20)
cau2 = cau2(john, 20)
cau3 = draw_poly(john, 8, 50, 45)
cau4 = cau4(john, 100)
cau5 = cau5_a(john, 20, 0) # VẪN CHƯA LÀM ĐƯỢC
cau5 = cau5_b(john, 100, 5)
cau6 = draw_equitriangle(john, 50)
cau7 = sum_to(10)
cau8 = area_of_circle(6)
cau9 = draw_a_star(john, 100)
cau10 = draw_multiple_stars(john, 5, 100)

wn.mainloop()
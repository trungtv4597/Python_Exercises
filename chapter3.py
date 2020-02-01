#   1: Qui đinh các ngày trong tuần từ cn tới t7 là 0,1,2,3,4,5,6. Việt một chương trình hỏi số của một ngày vè in ra tên của ngày đó.
day_number = int(input("từ 0 tới 6, số thứ tự của một ngày trong tuần bạn yêu cầu là bao nhiêu: "))
if day_number == 0:
    print('câu 1: sunday')
elif day_number == 1:
    print('câu 1: monday')
elif day_number == 2:
    print('câu 1: tuesday')
elif day_number == 3:
    print('câu 1: wednesday')
elif day_number == 4:
    print('câu 1: thursday')
elif day_number == 5:
    print('câu 1: friday')
elif day_number == 6:
    print('câu 1: saturday')
else:
    print('bạn có thể sai thông tin câu 1, yêu cầu nhập lại')

#   2: Dựa câu 1 viết một chương trình hỏi bạn muốn thứ mấy bắt đầu đi nghỉ và độ dài chuyến đi của bạn (theo ngày) để trả lời cho bạn thứ mấy bạn trở về.
ngay_di_nghi = day_number
so_ngay_di_nghi = int(input('ban đi nghỉ trong bao lâu: '))
ngay_tro_ve = (ngay_di_nghi + (so_ngay_di_nghi % 7)) % 7
if ngay_tro_ve == 0:
    print('câu 2: sunday')
elif ngay_tro_ve == 1:
    print('câu 2: monday')
elif ngay_tro_ve == 2:
    print('câu 2: tuesday')
elif ngay_tro_ve == 3:
    print('câu 2: wednesday')
elif ngay_tro_ve == 4:
    print('câu 2: thursday')
elif ngay_tro_ve == 5:
    print('câu 2: friday')
elif ngay_tro_ve == 6:
    print('câu 2: saturday')
else:
    print('bạn có thể sai thông tin câu 2, yêu cầu nhập lại')

#   3: Các giá trị nghịch của các giá trị sau
#a) a > b _ a <= b
#b) a >= b _ a < b
#c) a >= 18 and day == 3 _ a < 18 and day !=3 _ True and True => True / True and False => False
#d) a >= 18 and day !=3 _ a >= 18 and day == 3
a = 19
day = 3
print(bool(a < 18 and day !=3))
print(bool(a >= 18 and day != 3))

#   4: Các biểu thức sau để làm gì
#a) 3 == 3 : so sánh bằng
#b) 3 != 3 : phủ định 
#c) 3 >= 4 : 3 lớn hớn hoặc bằng 4
#d) not(3 < 4) : 3 lớn hơn hoặc bằng 4

#   5: Hoàn thành bảng truth sau:
# p q r   (not(p and q)) or r
# F F F   True
# F F T   True
# F T F   True
# T F F   True
# T F T   True
# T T F   False
# T T T   True

#   6: Viết một chương trình dựa vào bảng bên dưới và trả về giá trị string, với những ví dụ đề cho sẵn.
# Mark Grade
# >= 75 First
# [70-75) Upper Second
# [60-70) Second
# [50-60) Third
# [45-50) F1 Supp
# [40-45) F2
# < 40 F3

numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0] # đề cho
for number in numbers:
    if number >= 75:
        print('First')
    elif 70 <= number < 75:
        print('Upper Second') 
    elif 60 <= number < 70:
        print('Second') 
    elif 50 <= number < 60:
        print('Third Second') 
    elif 45 <= number < 50:
        print('F1 Supp') 
    elif 40 <= number < 45:
        print('F2') 
    else:
        print('F3') 

#   7: Viết một chương trình, với độ dài cho trc của 2 cạnh bên tam giác vuông, tìm cạnh huyền.
canh_vuong_1 = float(input('nhập giá trị độ dài cạnh góc vuông #1: '))
canh_vuong_2 = float(input('nhập giá trị độ dàicạnh góc vuông #2: '))
canh_huyen = (canh_vuong_1**2 + canh_vuong_2**2)**(0.5) #áp dụng pytago
print('câu 7: độ dài cạnh huyền của tam giác khi biết được độ dài hai cạnh góc vuông: ', canh_huyen)

#   8, 9: Viết một chương trình, với độ dài cho trc của một tam giác, hãy xác định đó có phải là một tam giác vuông hay không.
# Lưu ý, cạnh thứ 3 phải là cạnh huyền, chương trình trả về True khi đo là cạnh huyền và vê False khi không phải.
canh_ben_1 = float(input('nhập giá trị độ dài cạnh góc vuông #1: '))
canh_ben_2 = float(input('nhập giá trị độ dài cạnh góc vuông #2: '))
canh_ben_3 = float(input('nhập giá trị độ dài cạnh góc vuông #3: '))
print('câu 8, 9: với ba cạnh trên thì đây có phải là tam giác vuông ?', bool(canh_ben_3**2) == (canh_ben_1**2 + canh_ben_2**2))

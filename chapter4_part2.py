import math

def turn_clockwise(huong):
    '''
        Câu 1: Viết một hàm lấy 4 ký tự viết tắt của Đông-Tây-Nam-Bắc làm tham số.
            và trả về hướng kế tiếp theo chiều kim đồng hồ với hướng nhập vào và trả về None với các giá trị không liên quan.
        Gợi ý: North-East, West-North, East-South, South-West.
    '''
    if huong == 'N':
        return 'E'
    elif huong == 'E':
        return 'S'
    elif huong == 'S':
        return 'W'
    elif huong == 'W':
        return 'N'
    else:
        print('nhập sai!')
        return None


def day_name(name):
    '''
        Câu 2: Viết một hàm chuyển đổi một số nguyên (integer) từ 0 tới 6 thành một tên ngày.
            Quy ước là 0 là 'sunday' và trả về None nếu tham số vô giá trị.
    '''
    if name == 0:
        return 'Sunday'
    elif name == 1:
        return 'Monday'
    elif name == 2:
        return 'Tuesday'
    elif name == 3:
        return 'Wednesday'
    elif name == 4:
        return 'Thursday'
    elif name == 5:
        return 'Friday'
    elif name == 6:
        return 'Saturday'
    else:
        print('nhập sai!')
        return None


def day_num(name):
    '''
        Câu 3: Viết một hàm chuyển đổi một tên ngày thành một số nguyên (integer) từ 0 tới 6.
            Quy ước là 0 là 'sunday' và trả về None nếu tham số vô giá trị.
    '''
    if name == 'Sunday':
        return 0
    elif name == 'Monday':
        return 1
    elif name == 'Tuesday':
        return 2
    elif name == 'Wednesday':
        return 3
    elif name == 'Thursday':
        return 4
    elif name == 'Friday':
        return 5
    elif name == 'Saturday':
        return 6
    else:
        print('nhập sai!')
        return None


def day_add(name, num_holidays):
    '''
        Câu 4: Viết một hàm giúp trả lời câu hỏi:
            "Nay là Wednesday. tôi nghỉ lễ trong 19 ngày thì tôi sẽ về vào thứ mấy."
        Gợi ý: dùng lại 2 hàm trên để thực hiện bài này.
    '''
    number_leave = day_num(name)                    # dung hàm day_num chuyển tên một ngày thành số đại diện cho nó.
    number_back = number_leave + (num_holidays % 7) # vì một tuần có chu kỳ 7 ngày nên chia lấy dư (%) và cộng số dư với ngày bắt đầu sẽ dc ngày trở về.
    number_back = number_back % 7                   # chia lấy dư tiếp kết quả ở trên cho 7 để tránh trường hợp giá trị nằm ngoài 0-6.
    day_back = day_name(number_back)                # dùng hàm day_name chuyển số thành tên ngày tương ứng với nó.
    return day_back


def day_minus(name, num_negative):
    '''
        Câu 5: Liệu hàm day_add có thể làm việc với tham số âm?
            Ví dụ: -1 sẽ là này yesterday, hoặc -7 sẽ là một tuần trước.
            Nếu có thể làm dc như vậy, xin hãy giải thích rõ
        Gợi ý: dùng %, tìm lại các bài trước để xem chuyện gì xảy ra khi số âm % 7.
    '''
    # dùng phương pháp tương tự như câu 4.
    number_start = day_num(name)
    number_past = number_start + (num_negative % 7)
    number_past = number_past % 7
    day_past = day_name(number_past)
    return day_past


def days_in_month(name):
    '''
        Câu 6: Viết một hàm dùng tên của một tháng, để tìm được số ngày thuộc tháng đó. Không tính năm nhuận.
    '''
    months_31 = ['January', 'March', 'May',
        'July', 'August', 'October', 'December']
    months_30 = ['April', 'June', 'September', 'November']
    special_moth = 'February'

    for i in months_31:
        if name == i:
            return 31
    for j in months_30:
        if name == j:
            return 30
    if name == special_moth:
        return 28
    else:
        print('Nhập sai!')


def to_secs(hours, minutes, seconds):
    '''
        Câu 7, 8: Viết một hàm để chuyển đổi giờ, phút và giây thành tổng giây.
            Đông thời chương trình cũng cho phép người nhập số liệu từ máy tính.
    '''
    h_sec = hours *60 *60
    min_sec = minutes *60
    sum_sec = h_sec + min_sec + seconds
    return sum_sec


def hours_in(total_sec):
    return total_sec//3600
def minutes_in(total_sec):
    hours = total_sec/3600 - hours_in(total_sec)
    min = int(hours *60)
    return min
def second_in(total_sec):
    hours = hours_in(total_sec)
    minutes = minutes_in(total_sec)
    seconds = total_sec - hours*3600 - minutes*60
    return seconds
def cau9(total_sec):
    '''
        Câu 9: Viết ba hàm dạng đảo ngược với hàm to_sec ở câu trên.
            a/ hours_in trả về số nguyên chỉ số giờ từ tổng giây
            a/ minutes_in trả về số nguyên chỉ số phút từ tổng giây
            c/ second_in trả về số nguyên chỉ số giây từ tổng giây
    '''
    hours = hours_in(total_sec)
    minutes = minutes_in(total_sec)
    seconds = second_in(total_sec)
    print(hours, 'giờ', minutes, 'phút', seconds, 'giây')


def compare(a, b):
    '''
        Câu 11: Viết một hàm so sánh khi nhận hai tham số a và b.
            Trả về 1 nếu a > b/ 0 nếu a == b/ và -1 nếu a < b
    '''
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0


def hypotenuse(v1, v2):
    '''
        Câu 12: Viết một chương trình sẽ trả về độ dài cạnh huyền của một tam giác vuông biết trước độ dài 2 cạnh còn lại.
    '''
    # Áp dụn Pytago
    c = v1**2 + v2**2
    c = math.sqrt(c)
    return c


def slope(x1, y1, x2, y2):
    '''
        Câu 13: Viết một hàm trả về giá trị slope(a trong phương trình đường thẳng) của một đường thẳng qua 2 điểm có tọa độ cho trước.
            Sau đó dùng hàm slope trong hàm mới để tính y-intercept(b trong phương trình đường thẳng) của đường thắng như trên.
    '''
    # source for calculating slope: https://cls.syr.edu/mathtuneup/grapha/Unit4/Unit4a.html
    slope = (y2 - y1) / (x2 -x1)
    return slope
def y_intercept(x1, y1, x2, y2):
    # phương trình đường thẳng: y = ax + b
    a = slope(x1, y1, x2, y2)
    b = y1 - a*x1
    return b


def is_even(number):
    '''
        Câu 14: Viết một hàm nhận một số nguyên và trả về True nếu đó là số chẵn và False nếu là lẽ.
    '''
    if number % 2 == 0:
        return True
    else:
        return False


def is_odd(number):
    '''
        Câu 15: Viết một hàm nhận một số nguyên và trả về True nếu đó là số lẽ và False nếu là chẵn.
    '''
    if number % 2 == 0:
        return False
    else:
        return True


def is_factor(f, n):
    '''
        Câu 16, 17: Việt một hàm kiểm tra xem tham số #1 có phải là hệ số của tham số #2
    '''
    if n % f == 0:
        return True
    else:
        return False


def f2c(f):
    '''
        Câu 18: Viết một hàm để đổi từ độ F sáng độ C.
        Gợi ý: có thể xử dụng hàm 'round' có sẵn của Python.
    '''
    # source for formula: https://www.rapidtables.com/convert/temperature/how-fahrenheit-to-celsius.html
    c = round((f - 32)*(5/9), 0)
    return c


def c2f(c):
    '''
        Câu 19: Viết một hàm để đổi từ độ C sáng độ F.
        Gợi ý: có thể xử dụng hàm 'round' có sẵn của Python.
    '''
    # source for formula: https://www.rapidtables.com/convert/temperature/how-celsius-to-fahrenheit.html
    f = round((c*(9/5) + 32), 0)
    return f


# ĐÁP ÁN:

# câu 1:
huong = input('nhập hướng muốn tìm kiếm: ')
cau1 = turn_clockwise(huong)
print(bool(cau1), 'hương tìm kiếm là:', cau1)

#câu 2:
name = int(input('nhập một sô nguyên tương ứng với thứ mong muốn: '))
cau2 = day_name(name)
print('đáp án câu 2: ', cau2)

#câu 3:
name = input('nhập một tên một ngày trong tuần mong muốn: ')
cau3 = day_num(name)
print('đáp án câu 3: ', cau3)

#câu 4:
day_leave = input('bạn đi nghỉ vào thứ mấy: ')
holidays = int(input('ban đi nghỉ trong bao nhiêu ngày: '))
day_back = day_add(day_leave, holidays)
print('ngày đi nghỉ về là: ', day_back)

#câu 5:
day_star = input('tên ngày trong tuần bạn chọn làm mốc thời điểm: ')
num_negative = int(input('tên ngày trong tuần ở thời điểm quá khứ bạn muốn tìm kiếm là: '))
day_past = day_minus(day_star, num_negative)
print('thời điểm ở quá khứ muốn là: ', day_past)

#câu 6:
name_months = input('nhập tháng bạn muốn tìm: ')
cau6 = days_in_month(name_months)
print('Số ngày trong tháng là: ', cau6)

#câu 7, 8:
h = int(input('Số giờ:'))
m = int(input('Số phút:'))
s = int(input('Số giây:'))
cau7 = to_secs(h, m, s)
print('Tổng số giây tính được là: ', cau7)

#câu 9:
total_sec = int(input('Tổng số giây cần chuyển đổi: '))
cau9(total_sec)

#câu 10: giải thích nguyên nhân sai của các biểu thức sau
#1/ '3 % 4 == 0': % là chia lấy dư nên 3 không thể chia hết được cho 4
#2/ '3 / 4 == 0': / là phép chia luông trả về float nên không thể là 0 (số nguyên dc)
#3/ '3+4 * 2 == 14': nhân chia trước cộng trừ sau

#câu 11:
a = float(input('nhập a: '))
b = float(input('nhập b: '))
cau11 = compare(a, b)
print(cau11)

#câu 12:
v1 = float(input('nhập độ dài cạnh góc vuông 1: '))
v2 = float(input('nhập độ dài cạnh góc vuông 2: '))
c = hypotenuse(v1, v2)
print('Độ dài cạnh huyền là: ', c)

#câu 13:
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
cau13_1 = slope(x1, y1, x2, y2)
print('slope = ', cau13_1)
cau13_2 = y_intercept(x1, y1, x2, y2)
print('y_intercept = ', cau13_2)

#câu 14:
number = int(input('số cần kiểm tra chẵn: '))
cau14 = is_even(number)
print(cau14)

#câu 15:
number = int(input('số cần kiểm tra lẽ: '))
cau15 = is_odd(number)
print(cau15)

#câu 16, 17:
f = int(input('nhập hệ số: '))
n = int(input('nhập số: '))
cau16 = is_factor(f, n)
print(cau16)

#câu 18:
f = float(input('Nhập giá trị nhiệt độ F: '))
c = f2c(f)
print(c)

#câu 19:
c = float(input('Nhập giá trị nhiệt độ C: '))
f = c2f(c)
print(f)
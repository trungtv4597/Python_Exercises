#   1: Dùng câu văn sau: "all work and no play makes Jack a dull boy".
# lưu mỗi từ vào một biến khác nhau, rồi sau đó in cả câu văn trên cùng một hàng bằng print.
a = 'all'
b = ' work'
c = ' and'
d = ' no'
e = ' play'
f = ' makes'
g = ' Jack'
h = ' a'
i = ' dull'
j = ' boy'
print('câu 1: ',a + b + c + d + e + f + g + h + i + j)

#   2: Thêm ngoặc () vào biểu thức 6 * 1 - 2 sao cho nó có kết quả là -6.
print('câu 2: ',6*(1-2))

#   3: Đặt một nhận xét trước một dòng lệnh mới làm, và ghi lại chuyện j xảy ra khi chạy chương trình.
print('câu 3: chương trình thông báo sai cú pháp (syntax error)')

#   4: chạy đoạn code: bruce + 4, sao cho kết quả trả về là 10.
bruce = 6
print('câu 4:', bruce + 4)

#   5: Đây là một công thức tính số lượng kiếm được khi compound interest: A = P(1 + (r/n))^nt.
#      Việt một chương trình mà nó sẽ thay thế các ký tự trong công thức trên với những biến người đọc dễ hiểu hơn,
# và tính the interest cho với tỉ lệ interest thực tệ là 1%, và -0.05%.
# Khi hoàn thành, yêu câu người dùng cung cấp các giá trị phục vụ cho việc tính toán.
# Trong đó: P_khoản đầu tư ban đầu/
#          r_tỉ lệ interest hàng năm (số thập phân)/
#          n_số lần the interest is compunded mỗi năm/
#          t_số năm
# r = float(input('Tỉ lệ interest thực tế, chon một trong hai giá trị sau (1%) hoặc (-0.05%): '))
# P = float(input('Khoản đầu tư ban đầu: '))
# n = int(input('Số lần the interest is compunded mỗi năm: '))
# t = int(input('Sô năm thực hiện interest: '))
# A = P * (1 + ((r/100)/n))**(n*t)
# print('câu 5: giá trị cần tìm theo công thức là ', A)

#   6: Nhẩm các giá trị số học sau trong đầu rồi xử dụng Python để kiểm tra kết quả.
print(5 % 2) # 1
print(9 % 5) # 4
print(15 % 12) # 3
print(12 % 15) # 12
print(6 % 6) # 0
print(0 % 7) # 0
#print(7 % 0) # error

#   7: Đồng hồ chỉ 2pm. Thiết lập báo thức vào 51 tiếng sau.
# Vậy mấy h đồng hồ kêu? Với báo thức là 5100 tiếng thì thời điểm báo thức là mấy giờ?
thoi_diem_hien_tai = 2
so_tieng_bao_thuc = 51
thoi_diem_bao_thuc = 2 + so_tieng_bao_thuc%24
print('câu 7:', thoi_diem_bao_thuc)

#   8: Việt một chương trình để giải quyết cùng vấn đề ở câu 7.
# Nhưng lần này, hãy hỏi người dùng về thời gian hiện thời (bằng tiếng), và sô tiếng chờ.
# Đầu ra là thời điểm đồng hồ sẽ báo thức khi hết thời gian chờ.
a = int(input('Bây h đồng hồ của bạn là mấy giờ: '))
b = int(input('Bạn muốn để báo thức trong bao nhiêu lâu (theo tiếng đồng hồ): '))
c = a + b%24
print('câu 8: thời điểm báo thức kêu sẽ là: ', c)
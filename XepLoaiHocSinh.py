
print("PHẦN MỀM XẾP LOẠI HỌC SINH")
 
toan = 0; ly = 0; hoa = 0; van = 0; anh = 0
print("Nhập điểm môn Toán: ")
toan = float(input())
print("Nhập điểm môn Văn: ")
van = float(input())
print("Nhập điểm môn Anh: ")
anh = float(input())
diemTrungbBinh=(toan+anh+van)/3
print("Điểm trung bình là: ",diemTrungbBinh)

xepLoai = 'Xếp loại: '
if diemTrungbBinh <= 3:
    xepLoai += 'Kém!'
elif diemTrungbBinh < 5:
    xepLoai += 'Yếu!'
elif diemTrungbBinh < 7:
    xepLoai += 'Trung bình!'
elif diemTrungbBinh < 9:
    xepLoai += 'Khá!'
else:
    xepLoai += 'Giỏi!'
print(xepLoai)
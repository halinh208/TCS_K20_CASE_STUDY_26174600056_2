# Bài 4. Tính điện năng và chi phí
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13. Tính điện năng tiêu thụ và chi phí điện
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 14. In cả giá trị và kiểu dữ liệu của hai kết quả
print("--- Khi so_phut = 90 ---")
print("Điện năng tiêu thụ (kWh):", dien_nang_kwh, "- Kiểu:", type(dien_nang_kwh))
print("Chi phí điện (VNĐ):", chi_phi, "- Kiểu:", type(chi_phi))

# 16. Thay so_phut bằng 60 rồi chạy lại và so sánh
print("\n--- Khi thay so_phut = 60 ---")
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng tiêu thụ mới (kWh):", dien_nang_kwh, "- Kiểu:", type(dien_nang_kwh))
print("Chi phí điện mới (VNĐ):", chi_phi, "- Kiểu:", type(chi_phi))
# Bài 5. Nhập dữ liệu và chuyển đổi kiểu

print("--- Nhập các giá trị ban đầu ---")
# 17. Dùng input() để nhận bốn giá trị và in type() ngay khi nhập
ma_may = input("Nhập mã máy: ")
print("Kiểu dữ liệu của ma_may sau input():", type(ma_may))

cong_suat_w_str = input("Nhập công suất W: ")
print("Kiểu dữ liệu của cong_suat_w_str sau input():", type(cong_suat_w_str))

so_phut_str = input("Nhập số phút sử dụng: ")
print("Kiểu dữ liệu của so_phut_str sau input():", type(so_phut_str))

don_gia_str = input("Nhập đơn giá điện/kWh: ")
print("Kiểu dữ liệu của don_gia_str sau input():", type(don_gia_str))

# 18. Chuyển công suất sang float, số phút sang int và đơn giá sang float
cong_suat_w = float(cong_suat_w_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

print("\n--- Sau khi chuyển đổi kiểu ---")
print("type(cong_suat_w):", type(cong_suat_w))
print("type(so_phut):", type(so_phut))
print("type(don_gia_kwh):", type(don_gia_kwh))

# 19. Tính lại điện năng và chi phí sau khi chuyển kiểu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Kết quả tính toán ---")
print("Mã máy:", ma_may)
print("Điện năng tiêu thụ (kWh):", dien_nang_kwh)
print("Chi phí điện (VNĐ):", chi_phi)
# Bài 6. Chương trình tương tác hoàn chỉnh

# Nhập thông tin từ người dùng
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất thiết bị (W): "))
so_phut = int(input("Nhập thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Nhập đơn giá điện (VNĐ/kWh): "))

# Tính toán điện năng tiêu thụ và chi phí
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In kết quả theo đúng định dạng yêu cầu
print("\n--- KẾT QUẢ ---")
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh}")
print(f"Chi phí: {chi_phi}")
# Bài 7. Chẩn đoán lỗi

ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất W: ")
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
# Bài 8. f-string và định dạng đầu ra

ma_may = "PC12"
cong_suat_w = 250
dien_nang_kwh = 0.375
chi_phi = 1125

# Sử dụng f-string để in đúng định dạng yêu cầu
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VNĐ")
from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
# Bài 10. Chương trình tích hợp cuối Case Study
from datetime import datetime

# 1. Nhập thông tin từ người dùng
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w_str = input("Nhập công suất thiết bị (W): ")
so_phut_str = input("Nhập thời gian sử dụng (phút): ")
don_gia_str = input("Nhập đơn giá điện (VNĐ/kWh): ")

# 2. Chuyển đổi kiểu dữ liệu
cong_suat_w = float(cong_suat_w_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

# 3. Tính toán điện năng tiêu thụ và chi phí ước tính
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 4. Kiểm tra điều kiện sử dụng trên 60 phút (trả về giá trị Boolean, không dùng if)
tren_60_phut = so_phut > 60

# 5. Lấy thời điểm ghi nhận hiện tại
thoi_diem_ghi_nhan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 6. In kết quả theo đúng định dạng yêu cầu của đề bài
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VNĐ")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_ghi_nhan}")
[https://github.com/halinh208/TCS_K20_CASE_STUDY_CH2_2617460…://github.com/halinh208/TCS_K20_CASE_STUDY_CH2_26174600056)⁠
https://github.com/halinh208/TCS_K20_CASE_STUDY_CH2_26174600056
alooo
Rì vừa điieen
Giang mất đt rồi
nhắn tin vay tiền không cho cay
vay
python3 CASE_STUDY_CH2_26174600056/src/cau02_bien_kieu_du_lieu.py
git add src/
git commit -m "Hoan thanh bai 03 toan tu va bieu thuc"
git push origin main
# Bài 2. Biến và kiểu dữ liệu

# 5. Tạo các biến phù hợp theo quy tắc snake_case
ma_phien = "LAB026"
ma_may = "PC12"
cong_suat = 250.0
thoi_gian = 90
trang_thai = True
ghi_chu = None

# 6 & 7. In giá trị và dùng type() để kiểm tra kiểu dữ liệu
print("Mã phiên:", ma_phien, "| Kiểu:", type(ma_phien))
print("Mã máy:", ma_may, "| Kiểu:", type(ma_may))
print("Công suất:", cong_suat, "| Kiểu:", type(cong_suat))
print("Thời gian:", thoi_gian, "| Kiểu:", type(thoi_gian))
print("Trạng thái:", trang_thai, "| Kiểu:", type(trang_thai))
print("Ghi chú:", ghi_chu, "| Kiểu:", type(ghi_chu))

# 8. Thay thời gian sử dụng từ 90 thành 120 bằng phép gán lại và in giá trị mới
thoi_gian = 120
print("Thời gian mới sau khi thay đổi:", thoi_gian)

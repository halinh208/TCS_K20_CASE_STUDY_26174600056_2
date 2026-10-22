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
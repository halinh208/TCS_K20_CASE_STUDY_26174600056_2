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
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
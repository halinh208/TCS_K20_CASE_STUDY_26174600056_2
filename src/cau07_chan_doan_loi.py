# Bài 7. Chẩn đoán lỗi

ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
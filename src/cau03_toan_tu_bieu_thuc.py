# Bài 3. Toán tử và biểu thức

# Cho tổng thời gian sử dụng là 135 phút và các biến:
tong_phut = 135
cong_suat_w = 250

# 9. Dùng // và % để tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("Số giờ:", so_gio)
print("Số phút còn lại:", so_phut_con_lai)

# 10. Tạo biến su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("Sử dụng lâu (> 60 phút):", su_dung_lau)

# 11. Tạo biến du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# 12. Dự đoán rồi kiểm chứng hai biểu thức: 100 + 20 * 3 và (100 + 20) * 3
ket_qua_1 = 100 + 20 * 3
ket_qua_2 = (100 + 20) * 3
print("Biểu thức 1 (100 + 20 * 3):", ket_qua_1)
print("Biểu thức 2 ((100 + 20) * 3):", ket_qua_2)
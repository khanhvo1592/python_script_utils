# Định nghĩa bảng chuyển đổi đầu số
prefix_mapping = {
    # Viettel
    "84162": "032", "84163": "033", "84164": "034", "84165": "035",
    "84166": "036", "84167": "037", "84168": "038", "84169": "039",
    # Vinaphone
    "84123": "083", "84124": "084", "84125": "085", "84127": "081", "84129": "082",
    # Mobifone
    "84120": "070", "84121": "079", "84122": "077", "84126": "076", "84128": "078",
    # Vietnamobile
    "84186": "056", "84188": "058"
}

def normalize_phone_number(phone_number):
    # Lấy 5 ký tự đầu của số điện thoại (bao gồm mã quốc gia)
    prefix = phone_number[:5]
    # Kiểm tra nếu prefix nằm trong bảng chuyển đổi
    if prefix in prefix_mapping:
        # Thay thế đầu số cũ bằng đầu số mới
        return prefix_mapping[prefix] + phone_number[5:]
    return phone_number  # Trả về số gốc nếu không cần đổi

# Đọc tệp input.txt
input_file = "output_chuan_hoa_phone.txt"
output_file = "output_update_phone.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        phone_number = line.strip()  # Loại bỏ khoảng trắng và ký tự xuống dòng
        normalized_number = normalize_phone_number(phone_number)
        outfile.write(normalized_number + "\n")  # Ghi số đã chuẩn hóa vào tệp output.txt

print(f"Xử lý hoàn tất! Kết quả được lưu trong '{output_file}'")

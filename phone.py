import pandas as pd

# Đường dẫn tệp đầu vào và tệp đầu ra
input_file_path = "uid_to_phone.csv"  # Đổi thành tên tệp CSV của bạn
output_file_path = "converted_data.csv"

# Đọc dữ liệu từ tệp CSV
try:
    df = pd.read_csv(input_file_path, dtype={"id": int, "uid": str, "phone": str})

    # Thay đổi mã quốc gia 84 thành 0 trong cột 'phone'
    df['phone'] = df['phone'].str.replace(r'^84', '0', regex=True)

    # Lưu dữ liệu thành tệp CSV
    df.to_csv(output_file_path, index=False)

    print(f"Dữ liệu đã được chuyển đổi thành công và lưu tại: {output_file_path}")
except FileNotFoundError:
    print(f"Tệp {input_file_path} không tồn tại. Vui lòng kiểm tra đường dẫn.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

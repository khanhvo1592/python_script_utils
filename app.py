import pandas as pd

# Đường dẫn tệp đầu vào và tệp đầu ra
input_file_path = "input_data.txt"  # Đổi tên tệp thành tệp của bạn
output_file_path = "converted_data.xlsx"

# Đọc dữ liệu từ tệp văn bản và giữ kiểu dữ liệu
try:
    # Sử dụng `dtype` để giữ nguyên kiểu dữ liệu ban đầu
    df = pd.read_csv(input_file_path, sep="\t", dtype={"id": int, "uid": str, "phone": str})

    # Lưu DataFrame thành tệp Excel
    df.to_excel(output_file_path, index=False)

    print(f"Dữ liệu đã được chuyển đổi thành công và lưu tại: {output_file_path}")
except FileNotFoundError:
    print(f"Tệp {input_file_path} không tồn tại. Vui lòng kiểm tra đường dẫn.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

import requests

def check_facebook_uid(uid):
    """
    Kiểm tra xem UID Facebook có tồn tại hay không bằng cách kiểm tra mã trạng thái HTTP
    và nội dung HTML trả về.
    """
    url = f"https://www.facebook.com/{uid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # Kiểm tra mã trạng thái HTTP
        if response.status_code == 200:
            # Kiểm tra nội dung trang HTML
            if "This page isn't available" in response.text or "Trang này hiện không khả dụng" in response.text:
                return f"UID {uid} không tồn tại (nội dung trang không khả dụng)."
            else:
                return f"UID {uid} tồn tại."
        elif response.status_code == 404:
            return f"UID {uid} không tồn tại (404)."
        else:
            return f"Không thể xác định UID {uid}. HTTP Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Lỗi khi kiểm tra UID {uid}: {e}"

# Kiểm tra danh sách UID
if __name__ == "__main__":
    # Danh sách UID để kiểm tra
    uid_list = [
        "200373876759761",
        "100003199137965",
        "100005416950881",
        "100007298405900",
        "100006700771745",
        "100004824642488",
    ]
    
    for uid in uid_list:
        print(check_facebook_uid(uid))

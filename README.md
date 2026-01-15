# MINI PROJECT: PHÂN CỤM KHÁCH HÀNG DỰA TRÊN LUẬT KẾT HỢP

## 1. Giới thiệu dự án
[cite_start]Dự án sử dụng thuật toán K-Means để phân cụm khách hàng thành các nhóm có hành vi mua sắm tương đồng[cite: 6]. [cite_start]Điểm khác biệt của Mini Project này là thay vì dùng các đặc trưng RFM truyền thống, hệ thống dựa trên các luật kết hợp đã khai phá[cite: 7]. [cite_start]Điều này cho phép phân nhóm khách hàng theo các mẫu sản phẩm thường được mua cùng nhau, từ đó đưa ra những chiến lược marketing phù hợp cho từng nhóm[cite: 8].



## 2. Mục tiêu dự án
Sau khi thực hiện xong dự án, nhóm có thể:
* [cite_start]Hiểu quy trình kết hợp giữa khai phá luật và phân cụm[cite: 23].
* [cite_start]Thực hành trích đặc trưng từ dữ liệu luật kết hợp[cite: 24].
* [cite_start]Áp dụng thuật toán phân cụm (KMeans) để tìm nhóm hành vi tương đồng[cite: 25].
* [cite_start]Trực quan hóa, diễn giải các cụm và đề xuất chiến lược hành động[cite: 26, 27].

## 3. Pipeline thực hiện
1. [cite_start]**Tiền xử lý và khai phá luật**: Tập trung vào các luật kết hợp có giá trị lift cao và support đủ mạnh[cite: 32].
2. [cite_start]**Trích xuất đặc trưng**: Xây dựng vector đặc trưng cho từng khách hàng, gán nhãn 1 nếu giỏ hàng thỏa mãn luật và 0 nếu không[cite: 33, 34].
3. [cite_start]**Phân cụm**: Sử dụng KMeans để phân nhóm và chọn số cụm bằng phương pháp silhouette[cite: 35, 36].
4. [cite_start]**Diễn giải**: Phân tích đặc điểm giỏ hàng và luật chiếm ưu thế để đưa ra chiến lược phù hợp[cite: 38, 39].

## 4. Thành phần Project
| Thành phần | Ý nghĩa và chức năng |
| :--- | :--- |
| `src/cluster_library.py` | [cite_start]Chứa lớp `RuleBasedCustomerClusterer` để biến luật thành feature vector và chạy KMeans[cite: 49]. |
| `notebooks/clustering_from_rules.ipynb` | [cite_start]Notebook thực thi luồng công việc: lấy kết quả luật, chạy KMeans, vẽ biểu đồ và xuất kết quả[cite: 49]. |
| `app.py` | [cite_start]Dashboard Streamlit cho phép lọc theo cụm, xem top rules và gợi ý bundle/cross-sell[cite: 98]. |

## 5. Hướng dẫn cài đặt và sử dụng
1. **Kích hoạt môi trường ảo**:
   ```bash
   conda activate shopping_env
   [cite_start]``` [cite: 53]
2. **Cài đặt thư viện**:
   ```bash
   pip install -r requirements.txt
   [cite_start]``` [cite: 58]
3. **Khởi chạy Dashboard**:
   ```bash
   streamlit run app.py
   [cite_start]``` [cite: 98]

## 6. Kết quả Profiling & Chiến lược (Nhóm 2)
[cite_start]Dựa trên khảo sát Silhouette, số cụm tối ưu được chọn là **K=2**[cite: 82].

* [cite_start]**Cụm 1 (Khách hàng thân thiết)**: Nhóm có Recency thấp (~35 ngày), Frequency cao (~8 lần) và chi tiêu mạnh[cite: 95, 96]. 
  * [cite_start]*Chiến lược*: Tập trung vào **Bundle/Upsell** các bộ sản phẩm liên quan đến luật kết hợp mạnh (như bộ Herb Markers)[cite: 96].
* [cite_start]**Cụm 0 (Khách hàng tiềm năng)**: Nhóm có dấu hiệu "ngủ đông" với Recency cao (~99 ngày)[cite: 95].
  * [cite_start]*Chiến lược*: **Re-activation** thông qua các mã giảm giá cho các sản phẩm thuộc Top Rules của họ[cite: 96].

---
[cite_start]*Thực hiện bởi Nhóm 2 - Dự án FIT-DNU CONQUER[cite: 60].*

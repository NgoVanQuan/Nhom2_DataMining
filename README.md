# [cite_start]MINI PROJECT: PHÂN CỤM KHÁCH HÀNG DỰA TRÊN LUẬT KẾT HỢP [cite: 1]

## 1. Giới thiệu dự án
[cite_start]Dự án tập trung vào việc sử dụng thuật toán K-Means để phân cụm khách hàng thành các nhóm có hành vi mua sắm tương đồng[cite: 6]. [cite_start]Điểm khác biệt cốt lõi là thay vì chỉ sử dụng các đặc trưng RFM truyền thống, hệ thống dựa trên các luật kết hợp (Association Rules)[cite: 7]. [cite_start]Phương pháp này cho phép phân nhóm khách hàng theo các mẫu sản phẩm thường được mua cùng nhau, từ đó đưa ra những chiến lược marketing cá nhân hóa phù hợp cho từng phân khúc[cite: 8].

## [cite_start]2. Mục tiêu dự án [cite: 21]
* [cite_start]Hiểu và thực hành quy trình kết hợp giữa khai phá luật (Data Mining) và thuật toán phân cụm (Clustering)[cite: 23].
* [cite_start]Thực hiện trích xuất đặc trưng (Feature Engineering) từ dữ liệu luật kết hợp[cite: 24].
* [cite_start]Áp dụng các thuật toán phân cụm (KMeans, Agglomerative, hoặc DBSCAN) để tìm nhóm hành vi tương đồng[cite: 25].
* [cite_start]Trực quan hóa phân phối cụm và diễn giải hồ sơ khách hàng (Profiling)[cite: 26].
* [cite_start]Đề xuất chiến lược hành động cụ thể cho từng nhóm khách hàng (Segment)[cite: 27].

## [cite_start]3. Cấu trúc Pipeline thực hiện [cite: 31]
1.  [cite_start]**Tiền xử lý và Khai phá luật**: Tái sử dụng kết quả từ thuật toán Apriori hoặc FP-Growth, tập trung vào các luật có giá trị Lift cao[cite: 32].
2.  [cite_start]**Trích xuất đặc trưng**: Xây dựng ma trận đặc trưng cho từng khách hàng, trong đó mỗi chiều đại diện cho một luật mạnh (Feature vector)[cite: 33].
3.  [cite_start]**Phân cụm**: Sử dụng K-Means để phân nhóm khách hàng và chọn số cụm tối ưu bằng phương pháp Silhouette hoặc Elbow[cite: 35, 36].
4.  [cite_start]**Diễn giải và Trực quan hóa**: Phân tích đặc điểm giỏ hàng và luật chiếm ưu thế trong từng cụm để đưa ra chiến lược phù hợp[cite: 37, 39].

## [cite_start]4. Thành phần Project [cite: 50]

| Thành phần | Ý nghĩa và chức năng |
| :--- | :--- |
| `src/cluster_library.py` | [cite_start]Thư viện trung tâm chứa lớp `RuleBasedCustomerClusterer` để biến luật thành vector đặc trưng và chạy K-Means[cite: 49]. |
| `notebooks/clustering_from_rules.ipynb` | [cite_start]Notebook thực thi luồng công việc: lấy kết quả luật, chạy phân cụm, vẽ biểu đồ quan sát và xuất kết quả[cite: 49]. |
| `app.py` | [cite_start]Dashboard Streamlit cho phép lọc theo cụm, xem Top Rules và gợi ý Bundle/Cross-sell[cite: 98]. |

## [cite_start]5. Hướng dẫn cài đặt và sử dụng [cite: 51]

1.  **Kích hoạt môi trường ảo**:
    ```bash
    conda activate shopping_env [cite: 53]
    ```
2.  **Cài đặt thư viện**:
    ```bash
    pip install -r requirements.txt [cite: 58]
    ```
3.  **Thực thi Pipeline**: Chạy toàn bộ các Notebook trong thư mục `notebooks/` theo thứ tự hoặc sử dụng script tự động:
    ```bash
    python run_papermill.py
    ```
4.  **Khởi chạy Dashboard**:
    ```bash
    streamlit run app.py [cite: 98]
    ```

## 6. Kết quả Profiling & Chiến lược Marketing (Nhóm 2)
[cite_start]Dựa trên phân tích thực tế, tập khách hàng được chia thành 2 cụm chính ($K=2$): [cite: 82, 83]

* **Cụm 1 (Khách hàng thân thiết)**: Có tần suất mua hàng cao, mới quay lại gần đây và chi tiêu lớn. [cite_start]Chiến lược: Áp dụng **Bundle** (bán theo bộ) và **Upsell** các sản phẩm cao cấp[cite: 96].
* **Cụm 0 (Khách hàng tiềm năng/Ngủ đông)**: Đã lâu chưa quay lại, giá trị đơn hàng thấp. [cite_start]Chiến lược: **Re-activation** (kích hoạt lại) thông qua các mã giảm giá cho sản phẩm họ từng quan tâm[cite: 96].

---
*Dự án được thực hiện bởi Nhóm 2 *
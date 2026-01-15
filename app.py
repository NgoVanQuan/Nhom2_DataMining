import streamlit as st
import pandas as pd
import plotly.express as px

# Cấu hình trang
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")
st.title("📊 Phân khúc khách hàng dựa trên Luật kết hợp & RFM")

# 1. Tải dữ liệu từ các file bạn đã chạy ra
@st.cache_data
def load_data():
    clusters = pd.read_csv('./data/processed/customer_clusters_from_rules.csv')
    rules = pd.read_csv('./data/processed/rules_apriori_filtered.csv')
    return clusters, rules

try:
    df_clusters, df_rules = load_data()

    # Sidebar điều khiển
    st.sidebar.header("Bộ lọc")
    selected_cluster = st.sidebar.selectbox("Chọn cụm khách hàng để phân tích:", sorted(df_clusters['cluster'].unique()))

    # 2. Hiển thị tổng quan các cụm (Profiling)
    st.subheader("📌 Tổng quan các cụm khách hàng")
    col1, col2, col3 = st.columns(3)
    
    cluster_stats = df_clusters.groupby('cluster').agg({
        'CustomerID': 'count',
        'Recency': 'mean',
        'Frequency': 'mean',
        'Monetary': 'mean'
    }).reset_index()

    with col1:
        st.metric("Số lượng khách hàng", f"{df_clusters[df_clusters['cluster']==selected_cluster].shape[0]}")
    with col2:
        avg_monetary = df_clusters[df_clusters['cluster']==selected_cluster]['Monetary'].mean()
        st.metric("Giá trị chi tiêu TB", f"{avg_monetary:,.2f} £")
    with col3:
        avg_recency = df_clusters[df_clusters['cluster']==selected_cluster]['Recency'].mean()
        st.metric("Số ngày mua gần nhất TB", f"{avg_recency:.1f} ngày")

    # 3. Trực quan hóa 2D (PCA/SVD) [cite: 86]
    st.subheader("🎨 Biểu đồ phân bố cụm (PCA Projection)")
    # Giả sử bạn đã lưu kết quả PCA vào file csv, nếu chưa có thể tính toán nhanh tại đây
    fig = px.scatter(df_clusters, x='Recency', y='Monetary', color='cluster', 
                     log_y=True, title="Phân cụm theo Recency và Monetary (Log scale)")
    st.plotly_chart(fig, use_container_width=True)

    # 4. Gợi ý chiến lược Marketing cho từng cụm [cite: 96, 97]
    st.subheader("💡 Chiến lược Marketing đề xuất")
    if selected_cluster == 1:
        st.success("**Cụm 1: Loyal / VIP Shoppers (Khách hàng thân thiết)**")
        st.write("- **Persona:** Khách hàng mua sắm thường xuyên, chi tiêu cao, mới quay lại gần đây.")
        st.write("- **Hành động:** Chương trình tri ân VIP, tặng quà cá nhân hóa, gợi ý các Bundle sản phẩm cao cấp.")
    else:
        st.warning("**Cụm 0: At-Risk / Low Value (Khách hàng cần kích hoạt)**")
        st.write("- **Persona:** Khách hàng ít tương tác, giá trị đơn hàng thấp, đã lâu chưa mua lại.")
        st.write("- **Hành động:** Gửi mã giảm giá kích cầu, chiến dịch email 'Chúng tôi nhớ bạn', Cross-sell các mặt hàng giá rẻ.")

except FileNotFoundError:
    st.error("Vui lòng đảm bảo các file CSV đã được lưu trong thư mục 'data/processed/'.")
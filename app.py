import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰 ỨNG DỤNG TÍNH LÃI GỬI TIẾT KIỆM")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi và tổng số tiền nhận được.")

st.divider()

# =========================
# NHẬP THÔNG TIN
# =========================
st.subheader("📋 Thông tin tiền gửi")

so_tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0,
    value=10_000_000,
    step=1_000_000,
    format="%d"
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# =========================
# TÍNH TOÁN
# =========================
if st.button("🧮 TÍNH LÃI", use_container_width=True):

    if so_tien_gui <= 0:
        st.error("Vui lòng nhập số tiền gửi lớn hơn 0.")
    elif lai_suat < 0:
        st.error("Lãi suất không được nhỏ hơn 0.")
    else:

        # Lãi suất dạng thập phân
        lai_suat_decimal = lai_suat / 100

        # Tổng tiền lãi theo kỳ hạn
        tong_tien_lai = (
            so_tien_gui
            * lai_suat_decimal
            * ky_han
            / 12
        )

        # =========================
        # TÍNH LÃI ĐỊNH KỲ
        # =========================

        if hinh_thuc == "Cuối kỳ":
            tien_lai_dinh_ky = tong_tien_lai
            so_ky = 1
            ten_ky = "cuối kỳ"

        elif hinh_thuc == "Hàng tháng":
            so_ky = ky_han
            tien_lai_dinh_ky = tong_tien_lai / so_ky
            ten_ky = "tháng"

        else:  # Hàng quý
            so_ky = ky_han / 3
            tien_lai_dinh_ky = tong_tien_lai / so_ky
            ten_ky = "quý"

        # Tổng tiền nhận được
        tong_tien_nhan = so_tien_gui + tong_tien_lai

        # =========================
        # HIỂN THỊ KẾT QUẢ
        # =========================
        st.divider()
        st.subheader("📊 KẾT QUẢ")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "💵 Tiền lãi định kỳ",
                f"{tien_lai_dinh_ky:,.0f} VNĐ"
            )

        with col2:
            st.metric(
                "📈 Tổng tiền lãi",
                f"{tong_tien_lai:,.0f} VNĐ"
            )

        st.metric(
            "💰 Tổng tiền gốc + lãi",
            f"{tong_tien_nhan:,.0f} VNĐ"
        )

        # =========================
        # CHI TIẾT
        # =========================
        st.info(
            f"""
            **Chi tiết khoản tiền gửi:**

            - Số tiền gốc: **{so_tien_gui:,.0f} VNĐ**
            - Kỳ hạn: **{ky_han} tháng**
            - Lãi suất: **{lai_suat:.2f}%/năm**
            - Hình thức nhận lãi: **{hinh_thuc}**
            - Số kỳ nhận lãi: **{so_ky:g} kỳ**
            - Tiền lãi mỗi {ten_ky}: **{tien_lai_dinh_ky:,.0f} VNĐ**
            - Tổng tiền lãi: **{tong_tien_lai:,.0f} VNĐ**
            - Tổng tiền nhận được: **{tong_tien_nhan:,.0f} VNĐ**
            """
        )

# =========================
# CÔNG THỨC
# =========================
with st.expander("📚 Xem công thức tính"):

    st.write("**Tổng tiền lãi:**")

    st.latex(
        r"""
        Tiền\ lãi =
        Tiền\ gốc \times
        \frac{Lãi\ suất}{100}
        \times
        \frac{Kỳ\ hạn}{12}
        """
    )

    st.write("**Tổng tiền nhận được:**")

    st.latex(
        r"""
        Tổng\ tiền =
        Tiền\ gốc + Tổng\ tiền\ lãi
        """
    )

    st.write("**Lãi nhận hàng tháng:**")

    st.latex(
        r"""
        Lãi\ tháng =
        \frac{Tổng\ tiền\ lãi}{Số\ tháng}
        """
    )

    st.write("**Lãi nhận hàng quý:**")

    st.latex(
        r"""
        Lãi\ quý =
        \frac{Tổng\ tiền\ lãi}{Số\ quý}
        """
    )

import streamlit as st

st.set_page_config(
    page_title="Đăng ký du lịch công ty",
    page_icon="🏖️",
    layout="centered"
)

st.title("🏖️ ĐĂNG KÝ DU LỊCH CÔNG TY")

st.write("Vui lòng điền đầy đủ thông tin dưới đây.")

with st.form("form_dangky"):

    ho_ten = st.text_input("Họ và tên")

    gioi_tinh = st.radio(
        "Giới tính",
        ["Nam", "Nữ"]
    )

    so_dien_thoai = st.text_input("Số điện thoại")

    phong_ban = st.selectbox(
        "Phòng ban",
        [
            "Ban Giám đốc",
            "Kế toán",
            "Nhân sự",
            "Kinh doanh",
            "IT",
            "Kho",
            "Sản xuất"
        ]
    )

    tham_gia = st.radio(
        "Đăng ký",
        [
            "Có tham gia",
            "Không tham gia"
        ]
    )

    submit = st.form_submit_button("Đăng ký")

if submit:

    st.success("Đăng ký thành công!")

    st.write("### Thông tin vừa nhập")

    st.write("**Họ tên:**", ho_ten)
    st.write("**Giới tính:**", gioi_tinh)
    st.write("**Số điện thoại:**", so_dien_thoai)
    st.write("**Phòng ban:**", phong_ban)
    st.write("**Tham gia:**", tham_gia)

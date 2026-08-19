import streamlit as st
from database import get_connection
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

    try:

        conn = get_connection()

        cursor = conn.cursor()

        sql = """
        INSERT INTO dangky_dulich
        (
            ho_ten,
            gioi_tinh,
            so_dien_thoai,
            phong_ban,
            tham_gia
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        cursor.execute(
            sql,
            (
                ho_ten,
                gioi_tinh,
                so_dien_thoai,
                phong_ban,
                tham_gia == "Có tham gia"
            )
        )

        conn.commit()

        cursor.close()

        conn.close()

        st.success("🎉 Đăng ký thành công!")

    except Exception as e:

        st.error(f"Lỗi: {e}")
    import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(
    page_title="Trang quản trị",
    page_icon="🔐"
)

st.title("🔐 ĐĂNG NHẬP QUẢN TRỊ")

# --------------------------
# Tài khoản quản trị
# --------------------------
USERNAME = "admin"
PASSWORD = "123456"

# --------------------------
# Đăng nhập
# --------------------------
username = st.text_input("Tên đăng nhập")

password = st.text_input(
    "Mật khẩu",
    type="password"
)

login = st.button("Đăng nhập")

# --------------------------
# Kiểm tra đăng nhập
# --------------------------
if login:

    if username == USERNAME and password == PASSWORD:

        st.success("Đăng nhập thành công!")

        conn = get_connection()

        sql = """
        SELECT *
        FROM dangky_dulich
        ORDER BY id DESC
        """

        df = pd.read_sql(sql, conn)

        conn.close()

        st.subheader("Danh sách nhân viên đăng ký")

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.error("Sai tên đăng nhập hoặc mật khẩu.")

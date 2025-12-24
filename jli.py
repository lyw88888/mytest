import streamlit as st
from PIL import Image
import io
import os
import urllib.request

# 设置页面配置
st.set_page_config(
    page_title="个人简历生成器",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 顶部标题
st.markdown("""
# 🎯 个人简历生成器  
使用 Streamlit 创建您的个性化简历
""")

st.markdown("""
<style>
    .stApp {
        background-color: #1e1e1e;
        color: #e6e6e6;
    }
    h1, h2, h3 {
        color: #00c8ff !important;
    }
    .stTextInput>div>div>input {
        background-color: #2d2d2d !important;
        color: #e6e6e6 !important;
    }
    .stNumberInput>div>div>input {
        background-color: #2d2d2d !important;
        color: #e6e6e6 !important;
    }
    .stSlider>div>div>div {
        background-color: #2d2d2d !important;
    }
    .stSelectbox>div>div>div {
        background-color: #2d2d2d !important;
        color: #e6e6e6 !important;
    }
</style>
""", unsafe_allow_html=True)

# 主体布局：左右两栏
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📝 个人信息表单")

    # 基本信息
    name = st.text_input("姓名", "罗雨湾", key="name")
    position = st.text_input("职位", "软件测试", key="position")
    phone = st.text_input("电话", "17677169536", key="phone")
    email = st.text_input("邮箱", "237917611@qq.com", key="email")
    birth_date = st.date_input("出生日期", value=None, key="birth_date")
    gender = st.radio("性别", ["女","男",  "其他"], index=0, key="gender")
    education = st.selectbox("学历", ["本科", "硕士", "博士"], index=0, key="education")
    
    # 语言能力（多选）
    languages = st.multiselect("语言能力", ["中文", "英语", "日语"], default=["中文", "英语"], key="languages")
    
    # 技能（多选）
    skills = st.multiselect("技能（可多选）", 
                           ["Java", "HTML/CSS", "机器学习", "Python", "SQL", "C++"], 
                           default=["Java", "HTML/CSS", "机器学习", "Python"], 
                           key="skills")
    
    # 工作经验（滑块，范围0-30年）
    work_years = st.slider("工作经验（年）", 0, 30, 6, key="work_years")
    
    # 薪资范围（滑块，单位：元）
    salary_range = st.slider("期望薪资范围（元）", 5000, 50000, (10123, 29390), key="salary_range")
    
    # 个人简介
    bio = st.text_area("个人简介", """

""", key="bio")
    
    # 修正：每日最长联系时间（默认值120分钟，不超过1440）
    max_online_time = st.number_input(
        "每日最长联系时间（分钟）",
        min_value=1,
        max_value=24 * 60,  # 1440分钟 = 24小时
        value=120,        
        step=15,
        key="max_online_time"
    )
    
    # 头像上传
    uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="avatar")
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="上传的头像", use_container_width=True)  
        except Exception as e:
            st.error(f"图片加载失败: {str(e)}")
    else:
        # 检查本地文件是否存在，不存在则使用在线占位图
        if os.path.exists("default.png"):
            st.image("default.png", caption="默认头像", use_container_width=True) 
        else:
            # 在线占位图（150x150 像素，深色背景）
            placeholder_url = "https://via.placeholder.com/150/000000/ffffff?text=Avatar"
            st.image(placeholder_url, caption="默认头像", use_container_width=True) 

with col2:
    st.subheader("📄 简历实时预览")

    # 顶部姓名和头像
    st.markdown(f"<h1 style='color: #00c8ff; font-size: 28px;'>{name}</h1>", unsafe_allow_html=True)
    
    # 头像（右侧） - 修正：使用 use_container_width
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, width=120, use_container_width=False)  # 保持固定宽度
        except:
            # 如果上传的图片有问题，使用默认图片
            if os.path.exists("default.png"):
                st.image("default.png", width=120, use_container_width=False)
            else:
                st.image("https://via.placeholder.com/150/000000/ffffff?text=Avatar", width=120, use_container_width=False)
    else:
        # 没有上传图片，使用默认图片
        if os.path.exists("default.png"):
            st.image("default.png", width=120, use_container_width=False)
        else:
            st.image("https://via.placeholder.com/150/000000/ffffff?text=Avatar", width=120, use_container_width=False)

    # 个人信息（两栏布局）
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**性别**: ", gender)
        st.write("**学历**: ", education)
        st.write("**工作年限**: ", work_years, "年")
        st.write("**最佳联系时间**: ", max_online_time, "分钟")
    with col_b:
        st.write("**职位**: ", position)
        st.write("**电话**: ", phone)
        st.write("**邮箱**: ", email)
        st.write("**出生日期**: ", birth_date.strftime("%Y/%m/%d") if birth_date else "未填写")

    # 技能展示
    st.markdown("---")
    st.subheader("🛠️ 专业技能")
    for skill in skills:
        st.markdown(f"• <span style='color: #00c8ff;'>{skill}</span>", unsafe_allow_html=True)

    # 个人简介
    st.markdown("---")
    st.subheader("📝 个人简介")
    st.markdown(bio)

    # 薪资范围（带颜色提示）
    st.markdown("---")
    st.markdown(f"<p style='color: #00c8ff; font-weight: bold;'>期望薪资范围: {salary_range[0]} - {salary_range[1]} 元</p>", unsafe_allow_html=True)

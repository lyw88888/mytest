# 导入需要的库
import streamlit as st
import pandas as pd

# 设置页面标题
st.markdown("# 南宁市5家KTV经营数据")
st.markdown("---")

# 1. 定义南宁市5家KTV的模拟数据（12个月营收）
ktv_data = {
    "月份": ["01月", "02月", "03月", "04月", "05月", "06月", 
             "07月", "08月", "09月", "10月", "11月", "12月"],
    "星光KTV": [280, 320, 350, 380, 420, 450, 480, 460, 430, 470, 500, 550],   # 模拟营收（单位：千元）
    "乐迪KTV": [220, 250, 230, 260, 280, 300, 320, 310, 290, 330, 350, 380],
    "盛世KTV": [300, 310, 340, 360, 390, 410, 440, 420, 400, 450, 480, 520],
    "夜猫KTV": [180, 210, 240, 260, 290, 310, 340, 330, 310, 350, 370, 400],
    "云端KTV": [250, 270, 290, 310, 340, 360, 390, 380, 360, 400, 420, 450]
}

# 2. 创建数据框并展示
df = pd.DataFrame(ktv_data)
st.subheader("KTV月度营收数据（2024年）")
st.dataframe(df, use_container_width=True)  # 交互式数据框（自适应宽度）


st.markdown("---")

# 3. 可视化图表
st.subheader("KTV全年营收趋势（折线图）")
# 折线图展示所有KTV的全年营收趋势
st.line_chart(
    df, 
    x="月份", 
    y=["星光KTV", "乐迪KTV", "盛世KTV", "夜猫KTV", "云端KTV"],
    use_container_width=True
)

st.subheader("12月KTV营收对比（柱状图）")
# 获取12月数据（最后一行）
dec_data = df.iloc[-1].drop("月份")
st.bar_chart(dec_data, use_container_width=True)



st.markdown("---")

# 4. 南宁市5家KTV的地图定位（模拟经纬度）
st.subheader("KTV地理位置分布")
map_data = pd.DataFrame(
    {
        "latitude": [22.805, 22.810, 22.798, 22.815, 22.802],  # 南宁大致纬度
        "longitude": [108.345, 108.350, 108.338, 108.355, 108.342],  # 南宁大致经度
       
    },
    index=["星光KTV", "乐迪KTV", "盛世KTV", "夜猫KTV", "云端KTV"]
)
st.map(map_data, use_container_width=True)


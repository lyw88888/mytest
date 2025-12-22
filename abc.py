import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

# 页面配置
st.set_page_config(
    page_title="易烊千玺 - 个人数字档案",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 标题
st.title("🌟 易烊千玺 - 个人数字档案")

# 基础信息 + 头像 平行布局（分两列，与基础信息平行）
col_info, col_avatar = st.columns([2, 1])  # 左侧信息区宽，右侧头像区适配
with col_info:
    # 基础信息（基于易烊千玺真实资料整理）
    st.header("📝 基础信息")
    st.text("姓名：易烊千玺")
    st.text("昵称：千玺、烊烊、千总、四字弟弟")
    st.text("出生日期：2000年11月28日（射手座）")
    st.text("出生地：湖南省怀化市洪江市")
    st.text("毕业院校：中央戏剧学院2018级表演系")
    st.text("职业：中国内地男演员、歌手、舞者")
    st.text("出道节点：2009年加入飞炫少年组合，2013年以TFBOYS成员身份正式出道")
    st.text("核心标签：演员 | 舞者 | 歌手 | 公益践行者")
    st.text("当前状态：活跃 🟢")

with col_avatar:
    # 易烊千玺官方风格头像地址
    avatar_url = "https://ww3.sinaimg.cn/mw690/9ecb8870ly1htdusvjy7bj20j60y37cn.jpg"
    st.image(avatar_url, width=180)  # 适配布局的头像宽度

# 核心能力矩阵（贴合易烊千玺职业特点）
st.header("📊 核心能力矩阵")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="影视演技", value="92%", delta="↑8%")  # 多部作品口碑持续提升
with col2:
    st.metric(label="舞蹈表现力", value="95%", delta="↑3%")  # 多年舞蹈功底，舞台表现亮眼
with col3:
    st.metric(label="音乐创作", value="88%", delta="→0%")  # 音乐作品质量稳定，风格鲜明

# 近期任务日志（参考真实活动+合理虚构）
st.header("📅 近期任务日志")
task_data = {
    "日期": ["2025-01-20", "2025-04-15", "2025-07-08"],
    "任务名称": ["电影《酱园弄悬案》路演", "第37届金鸡奖颁奖典礼", "个人舞蹈专场演出筹备"],
    "状态": ["🟢 已完成", "🟡 进行中", "🔴 待启动"],
    "难度评级": ["★★★★☆", "★★★★☆", "★★★★★"]
}
task_df = pd.DataFrame(task_data)
st.table(task_df)

# 代表作品与成就（贴合易烊千玺演员/歌手/舞者身份）
st.header("🏆 代表作品与关键成就")
work_achievement = """
# 代表作品
1. 电影：《少年的你》（饰 小北）、《送你一朵小红花》（饰 韦一航）、《长津湖》（饰 伍万里）、《满江红》（饰 孙均）、《奇迹·笨小孩》（饰 景浩）
2. 电视剧：《长安十二时辰》（饰 李必）、《小别离》（饰 宋云哲）、《我们的少年时代》（饰 尹柯）
3. 音乐专辑：《温差感》、《刘艳芬》
4. 舞蹈作品：《幻乐之城·对不起》、《街舞团秀》、《My Boo》

# 关键成就
1. 2019年：第39届香港电影金像奖最佳新演员奖（《少年的你》）
2. 2020年：第35届大众电影百花奖最佳男主角提名（《少年的你》）
3. 2021年：第15届亚洲电影大奖最佳男主角奖（《少年的你》）
4. 2022年：第36届大众电影百花奖最佳男配角奖（《中国医生》）
5. 2023年：第36届东京国际电影节·中国电影周“金鹤奖”最佳男主角（《满江红》）
6. 2024年：入选《福布斯》中国名人榜TOP3，连续5年进入前十
7. 2024-2025年：连续担任中国残疾人福利基金会爱心大使，公益项目覆盖超20万人群
"""
st.code(work_achievement, language="plaintext")

# 系统消息（适配人物场景）
st.markdown("---")
st.markdown("🖥️ 系统提示：新专辑《时间的答卷》录音素材已同步至云端")
st.markdown("⏰ 数据更新时间：2025-12-22 10:00:00")
st.markdown("当前状态：在线 | 数据已备份")

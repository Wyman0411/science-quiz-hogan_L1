import streamlit as st

# 設定網頁標題與寬度
st.set_page_config(page_title="社會科超級挑戰盃", layout="centered")

st.title("🏆 五年級社會科：臺灣我的家 挑戰盃")
st.write("同學好！請仔細閱讀題目，選出最正確的答案吧！")

# 這裡示範放入前5題選擇題，老師可以依照這個格式把40題都加進來喔！
questions = [
    {
        "q": "1. 有一艘貨輪從日本出發前往菲律賓，它在途中「最不可能」經過下列哪一個海域？",
        "options": ["東海", "臺灣海峽", "巴士海峽", "大西洋"],
        "answer": "大西洋",
        "explanation": "日本到菲律賓會經過東海、臺灣海峽或太平洋邊緣，往南經過巴士海峽。大西洋在歐洲和美洲之間，不可能經過。"
    },
    {
        "q": "2. 小華寫下：「北回歸線通過臺灣的兩個縣市」。最可能是哪一組？",
        "options": ["雲林、台東", "嘉義、花蓮", "台南、宜蘭", "彰化、花蓮"],
        "answer": "嘉義、花蓮",
        "explanation": "北回歸線(23.5°N)由西向東穿過臺灣的嘉義縣(水上鄉)與花蓮縣(瑞穗鄉、豐濱鄉)。"
    },
    {
        "q": "3. 關於臺灣的絕對位置，下列哪一個描述是正確的？",
        "options": ["位於西半球、北半球", "位於東半球、南半球", "經度大約在東經120至122度", "緯度大約在北緯120至122度"],
        "answer": "經度大約在東經120至122度",
        "explanation": "臺灣位於東半球(東經120~122度)與北半球(北緯22~25度)。"
    },
    {
        "q": "4. 臺灣被稱為「亞洲的門戶」，主要是因為下列哪一項原因？",
        "options": ["臺灣有很多高山", "位於亞洲東部樞紐，海空交通便利", "臺灣出產很多水果", "臺灣的地形非常多樣"],
        "answer": "位於亞洲東部樞紐，海空交通便利",
        "explanation": "臺灣的地理位置優越，是連接東北亞和東南亞的必經之地，因此有亞洲門戶之稱。"
    },
    {
        "q": "5. 想欣賞山脈緊鄰深海的「斷層海岸」，應該去臺灣的哪一邊？",
        "options": ["東部海岸", "西部海岸", "南部海岸", "北部海岸"],
        "answer": "東部海岸",
        "explanation": "東部海岸因為斷層作用，中央山脈與海岸山脈緊鄰太平洋，形成斷層海岸（如蘇花海岸）。"
    }
]

# 初始化分數與答題狀態
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# 建立表單
with st.form("quiz_form"):
    user_answers = []
    for i, q in enumerate(questions):
        st.subheader(q["q"])
        ans = st.radio("請選擇答案：", q["options"], key=f"q_{i}")
        user_answers.append(ans)
        st.divider()
    
    submit = st.form_submit_button("交卷看成績！")

# 提交後的評分與解析顯示
if submit:
    st.session_state.submitted = True
    score = 0
    st.balloons()
    st.header("📝 測驗結果與詳細解析")
    
    for i, q in enumerate(questions):
        user_ans = user_answers[i]
        correct_ans = q["answer"]
        
        if user_ans == correct_ans:
            score += 100 / len(questions)
            st.success(f"**{q['q']}**  \n✅ 你的答案：{user_ans} (正確！)")
        else:
            st.error(f"**{q['q']}**  \n❌ 你的答案：{user_ans} | 正確答案：{correct_ans}")
        
        # 顯示超白話解析
        with st.expander("👉 點我看白話文解析"):
            st.info(q["explanation"])
            
    st.metric(label="你的總分", value=f"{int(score)} 分")
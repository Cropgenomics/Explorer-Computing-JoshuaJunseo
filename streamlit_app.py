import streamlit as st
import pandas as pd
import numpy as np

st.text("Hello, Visitor!")

st.markdown("# 자기소개")
st.text("안녕하세요, 제 이름은 조준서입니다.")
st.markdown("저는 **작물 유전체 연구**에 관심을 가지고 있습니다.")

st.markdown("## 좋아하는 것")
st.text("저는 주짓수와 사진 찍는 것을 좋아합니다.")
st.text("가장 자주 사용하는 어플은 당근입니다.")

st.markdown("## 앞으로의 목표")
st.text("식량 문제를 해결하는데 기여하여 세상을 더 살기 좋은 곳으로 만들고 싶습니다.")

st.caption("파이썬")
st.code("print('Make the world a better place')", language="python")

st.caption("하버 보슈법 화학식")
st.latex(r"N2 + 3H2 => 2NH3")


st.write("### 데이터프레임 정적 테이블")
data = {"요일": ["월", "화", "수", "목", "금"], "1교시": ["농업법개론", "골프초급", "태권도", "식물세포생물학", "컴퓨팅탐색"], "2교시": ["말하기와 토론", "작물생리학", "말하기와 토론", "", ""], "3교시": ["베리타스", "", "", "", ""]}
df = pd.DataFrame(data)
st.table(df)

json_data = {
    "농업법개론": {"교수님": "조성호", "장소": "75동"},
    "컴퓨팅 탐색": {"교수님": "변해선", "장소": "26동"}
}
st.write("### JSON 데이터")
st.json(json_data)

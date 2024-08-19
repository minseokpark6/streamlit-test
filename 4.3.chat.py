import streamlit as st
from dotenv import load_dotenv

from llm import get_ai_response
# 함수 정의된 부분에 가서 command + . 누르면 선택창이 나옴 >> 그곳에서 선택
# llm.py 에서 정의한 get_ai_message 함수를 import하기

# how to add chat history
# https://python.langchain.com/v0.2/docs/how_to/qa_chat_history_how_to/


# 환경 변수 불러오기
load_dotenv()

st.set_page_config(page_title="소득세 챗봇", page_icon="🤖")

st.title("🤖 소득세 챗봇")
st.caption("소득세에 관련된 모든 것을 답해드립니다!")



if 'message_list' not in st.session_state:
    st.session_state.message_list = []

# 이전 채팅 내용 화면에 표기_히스토리 유지
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])
    


if user_question := st.chat_input(placeholder="소득세와 관련된 궁금한 내용을 말씀해 주세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    # 채팅을 칠 때마다 message_list에 append
    st.session_state.message_list.append({"role": "user", "content": user_question})
    
    with st.spinner("답변을 생성하는 중입니다."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            # 최종으로 나온 전체 답변을 넣어줘야 함
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})
    

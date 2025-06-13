import streamlit as st

def main():
    st.title("키 체크 및 조언")

    height = st.number_input("키(cm)를 입력하세요", min_value=0)

    if height > 0:
        if height <= 174:
            st.write("키가 작다")
            st.info("""
            키 크는 방법:
            - 충분한 수면을 취하세요 (7~9시간)
            - 균형 잡힌 식사를 하세요 (단백질, 칼슘 등)
            - 규칙적으로 스트레칭과 운동을 하세요
            - 자세를 바르게 유지하세요
            - 스트레스를 줄이세요
            """)
        else:
            st.write("키가 크다")
            st.success("멋지다! 자신감을 가지세요 😊")

if __name__ == "__main__":
    main()


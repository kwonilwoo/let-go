import streamlit as st

def main():
    st.title("키 체크")

    height = st.number_input("키(cm)를 입력하세요", min_value=0)

    if height > 0:
        if height <= 174:
            st.write("키가 작다")
        else:
            st.write("키가 크다")

if __name__ == "__main__":
    main()


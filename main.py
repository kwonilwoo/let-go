import streamlit as st

def calculate_bmi(weight, height):
    if height <= 0:
        return None, "잘못된 키 입력입니다."
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        category = "저체중"
    elif 18.5 <= bmi < 23:
        category = "정상"
    elif 23 <= bmi < 25:
        category = "과체중"
    else:
        category = "비만"
    return round(bmi, 2), category

def main():
    st.title("BMI 계산기")
    st.write("키(cm)와 몸무게(kg)를 입력하면 BMI 지수를 계산하고 건강 상태를 알려드립니다.")

    height = st.number_input("키(cm)", min_value=0.0, step=0.1)
    weight = st.number_input("몸무게(kg)", min_value=0.0, step=0.1)

    if st.button("BMI 계산하기"):
        bmi, category = calculate_bmi(weight, height)
        if bmi:
            st.success(f"BMI 지수: {bmi}")
            st.info(f"당신은 **{category}**입니다.")
        else:
            st.error(category)

if __name__ == "__main__":
    main()

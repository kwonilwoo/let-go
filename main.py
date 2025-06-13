import streamlit as st

def main():
    st.title("에너지 변환 계산기")
    st.write("질량, 속도, 높이를 입력하면 위치 에너지, 운동 에너지, 총 에너지를 계산해줍니다.")

    mass = st.number_input("질량(kg)", min_value=0.0, step=0.1)
    velocity = st.number_input("속도(m/s)", min_value=0.0, step=0.1)
    height = st.number_input("높이(m)", min_value=0.0, step=0.1)
    g = 9.81  # 중력 가속도 m/s^2

    if st.button("계산하기"):
        if mass > 0:
            potential_energy = mass * g * height  # 위치 에너지
            kinetic_energy = 0.5 * mass * velocity ** 2  # 운동 에너지
            total_energy = potential_energy + kinetic_energy  # 총 에너지

            st.write(f"위치 에너지 (Potential Energy): {potential_energy:.2f} J")
            st.write(f"운동 에너지 (Kinetic Energy): {kinetic_energy:.2f} J")
            st.write(f"총 에너지 (Total Energy): {total_energy:.2f} J")
        else:
            st.error("질량은 0보다 커야 합니다.")

if __name__ == "__main__":
    main()


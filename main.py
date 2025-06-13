import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title("에너지 변환 계산기 및 시각화")
    st.write("질량(kg), 속도(m/s), 높이(m)를 입력하면 위치 에너지, 운동 에너지, 총 에너지를 계산하고 시각화합니다.")

    mass = st.number_input("질량 (kg)", min_value=0.0, step=0.1)
    velocity = st.number_input("속도 (m/s)", min_value=0.0, step=0.1)
    height = st.number_input("높이 (m)", min_value=0.0, step=0.1)

    g = 9.81  # 중력 가속도 (m/s^2)

    if st.button("계산하기"):
        if mass > 0:
            potential_energy = mass * g * height
            kinetic_energy = 0.5 * mass * velocity ** 2
            total_energy = potential_energy + kinetic_energy

            st.write(f"위치 에너지: {potential_energy:.2f} J")
            st.write(f"운동 에너지: {kinetic_energy:.2f} J")
            st.write(f"총 에너지: {total_energy:.2f} J")

            energies = [potential_energy, kinetic_energy, total_energy]
            labels = ['위치 에너지', '운동 에너지', '총 에너지']

            fig, ax = plt.subplots()
            ax.plot(labels, energies, marker='o', linestyle='-', color='blue')
            ax.set_ylabel('에너지 (J)')
            ax.set_title('에너지 변환 시각화')
            ax.grid(True)

            # 각 점 위에 값 표시
            for i, energy in enumerate(energies):
                ax.annotate(f'{energy:.2f}', (labels[i], energies[i]), textcoords="offset points", xytext=(0,10), ha='center')

            st.pyplot(fig)

        else:
            st.error("질량은 0보다 커야 합니다.")

if __name__ == "__main__":
    main()

import streamlit as st

def calculate_result(class_index, sequence):
    class_values = {
        1: [270, 90, 45, 27, 9, 9, 6, 270],
        2: [360, 180, 120, 90, 18, 18, 12, 360],
        3: [540, 270, 180, 135, 27, 27, 18, 540]
    }

    selected_row = class_values[class_index]

    # Multiply each number from the input sequence by the corresponding value in the selected row
    result = [sequence[i] * selected_row[i] for i in range(len(sequence))]

    # Calculate the sum of the results
    sum_result = sum(result)

    # Divide the sum by 30
    quotient = sum_result // 30
    remainder = sum_result % 30

    return quotient, remainder

def main():
    st.title("Streamlit Ticket Calculation App")

    # Class selection
    class_index = st.selectbox("Select the class:", [1, 2, 3])

    # Input sequence
    input_sequence = st.text_input("Enter the 8 values (space-separated):")

    if st.button("Calculate"):
        if input_sequence:
            try:
                input_sequence = list(map(int, input_sequence.split()))
                quotient, remainder = calculate_result(class_index, input_sequence)
                st.write(f"Tickets: {quotient}")
                st.write(f"Remaining Points: {remainder}")
            except:
                st.error("Invalid input! Please enter 8 valid numbers.")
        else:
            st.warning("Please enter the 8 values to calculate the result.")

if __name__ == "__main__":
    main()

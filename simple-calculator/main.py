import streamlit as st

# Apply custom CSS for background, buttons, and inputs
st.markdown("""
    <style>
        /* Gradient Background */
        body {
            background: linear-gradient(to right, #a18cd1, #fbc2eb);
        }

        /* Center Title */
        .stApp {
            background-color: #f4f4f4;
            border-radius: 15px;
            padding: 20px;
        }
        
        /* Styling for Number Inputs */
        .stNumberInput, .stSelectbox {
            background-color: white;
            border-radius: 10px;
            padding: 8px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }

        /* Styling for Calculate Button */
        .stButton>button {
            background-color: #6a11cb;
            color: white;
            border-radius: 10px;
            padding: 12px;
            width: 100%;
            font-size: 18px;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #2575fc;
        }

        /* Styling for Result */
        .result-box {
            background: #ffffff;
            padding: 12px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            color: #333;
            margin-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    # Set page title and configuration
    st.title("🧮 Simple Calculator")
    st.write("Enter two numbers and choose an operation.")

    # Create two columns for number inputs
    col1, col2 = st.columns(2)

    # Input fields for numbers
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)

    # Operation selection
    operation = st.selectbox(
        "Choose operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"],
    )

    # Calculate button
    if st.button("✨ Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            else:  # Division
                if num2 == 0:
                    st.error("🚨 Error: Division by zero!")
                    return
                result = num1 / num2
                symbol = "÷"

            # Display result in a styled box
            st.markdown(f"""
                <div class="result-box">
                    {num1} {symbol} {num2} = {result}
                </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"⚠️ An error occurred: {str(e)}")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

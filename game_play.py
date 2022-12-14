import pandas as pd
import streamlit as st
import time


class MagicNumbers:
    def __init__(self):
        self.block_one = None
        self.block_two = None
        self.block_three = None
        self.block_four = None
        self.block_five = None
        self.block_six = None
        self.running_calculation = 0
        self.yes_button_widget_key = 0
        self.b_index = 0


b1 = [(i + j) for i in range(0, 64, 2) for j in range(1, 2)]
b2 = [(i + j) for i in range(1, 64, 4) for j in range(1, 3)]
b3 = [(i + j) for i in range(1, 64, 8) for j in range(3, 7)]
b4 = [(i + j) for i in range(1, 64, 16) for j in range(7, 15)]
b5 = [(i + j) for i in range(1, 64, 32) for j in range(15, 31)]
b6 = [(i + j) for i in range(1, 64, 64) for j in range(31, 63)]

BLOCKS = [b1, b2, b3, b4, b5, b6]

mn = MagicNumbers()


def make_tables(block_in_blocks, block_name):
    column1 = [n for n in block_in_blocks[::8]]
    column2 = [n for n in block_in_blocks[1::8]]
    column3 = [n for n in block_in_blocks[2::8]]
    column4 = [n for n in block_in_blocks[3::8]]
    column5 = [n for n in block_in_blocks[4::8]]
    column6 = [n for n in block_in_blocks[5::8]]
    column7 = [n for n in block_in_blocks[6::8]]
    column8 = [n for n in block_in_blocks[7::8]]

    setattr(mn, block_name, pd.DataFrame({
        'c1': column1,
        'c2': column2,
        'c3': column3,
        'c4': column4,
        'c5': column5,
        'c6': column6,
        'c7': column7,
        'c8': column8,
    }))

    for column in [column1, column2, column3, column4, column5, column6, column7, column8]:
        column.clear()


def main():
    if 'calculation' not in st.session_state:
        st.session_state['calculation'] = 0

    attr_names = ['block_one', 'block_two', 'block_three', 'block_four', 'block_five', 'block_six']
    block_index = 0

    for block_attr_name in attr_names:
        make_tables(BLOCKS[block_index], block_attr_name)
        block_index += 1
    welcome()


def welcome():
    st.title('Magic Calculator')
    greeting = 'Welcome to the magic calculator!'
    st.text(greeting)
    st.text('~' * len(greeting))
    time.sleep(1)
    st.text('Think of a number between 1 and 63.')
    time.sleep(0.25)
    show_tables()


def show_tables():
    for block in [mn.block_one, mn.block_two, mn.block_three, mn.block_four, mn.block_five, mn.block_six]:
        check_response()

        # CSS to inject contained in a string
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(block)

    st.markdown("Check the **answer page** in the side bar to see the number you have been thinking of!")


def check_response():
    yes_response = st.button('Press Me If Your Number Is In The Table Below', key=mn.yes_button_widget_key)
    if yes_response:
        calculate(mn.b_index)
    mn.b_index += 1
    mn.yes_button_widget_key += 1


def calculate(block_index):
    st.session_state.calculation += BLOCKS[block_index][0]


if __name__ == "__main__":
    main()

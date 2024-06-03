import streamlit as st
import subprocess

st.write('GoAIO')
devices = ['dev 1', 'dev 2']
st.sidebar.selectbox(label="Select the device", options=devices)
st.error('no device connected')


def main():
    cmd = ['streamlit', 'run', 'app.py']
    subprocess.call(cmd)


if __name__ == "__main__":
    main()

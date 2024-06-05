import os
import psutil
import streamlit as st
from goaio.utils.loghandler import get_logger

ui_logger = get_logger(__name__)


class Ui:
    def __init__(self):
        self.session_state = st.session_state
        self.device = None
        self.initialize_ui()
        self.main_page()
        self.side_bar()

    def initialize_ui(self):
        try:
            st.set_page_config(page_title="GoAIO - Assistant", layout="wide", initial_sidebar_state="expanded")
            ui_logger.info("Page configuration set.")
        except Exception as e:
            ui_logger.error(f"Error initializing UI: {e}")

    def main_page(self):
        try:
            bug, cmt, ss, sr, vm = st.tabs(["🐞 Bug Descriptor",
                                            " Comment Descriptor", "Screenshot", "screenrecord", "Version Manager"])

            with bug:
                st.title('Bug Descriptor')
            ui_logger.info("Main page set up.")
        except Exception as e:
            ui_logger.error(f"Error setting up main page: {e}")

    def side_bar(self):
        try:
            st.sidebar.title('GoAIO - Assistant :sparkles:')
            st.sidebar.selectbox(label="Select the project",
                                 options=['Android TV', 'Personal Safety', 'Photos'],
                                 help="Select the project that you are working on.")
            self.device = st.sidebar.selectbox(label="Select the device",
                                               options=['device 1', 'device 2'],
                                               help="Select the device to perform operations")
            st.sidebar.info(f"selected device {self.device}", icon="📱")
            st.sidebar.divider()
            st.toast(f'selected {self.device}')
            if self.device:
                st.sidebar.write(f'Device: {self.device}')
                st.sidebar.write('Build:')
                st.sidebar.write('GMS core:')
            st.sidebar.divider()

            ui_logger.info("Sidebar set up.")
            quit_button = st.sidebar.button(label="quit")
            if quit_button:
                pid = os.getpid()
                process = psutil.Process(pid)
                process.terminate()
                ui_logger.info("App closed")
                ui_logger.info("===========================================================")
        except Exception as e:
            ui_logger.error(f"Error setting up sidebar: {e}")


# Example of creating an instance of the Ui class to trigger UI setup
if __name__ == "__main__":
    ui_instance = Ui()

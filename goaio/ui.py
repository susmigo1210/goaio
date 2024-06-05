import streamlit as st
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)


def app():
    logger.info('Starting the app')
    st.title('Hi there')


if __name__ == "__main__":
    app()

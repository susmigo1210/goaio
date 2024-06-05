import streamlit as st
import streamlit.web.bootstrap as st_bootstrap
from goaio.ui import app
import logging


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)


def run():
    if st.runtime.exists():
        # The app has been executed with `streamlit run goaio/app.py`
        logger.info('Starting the app with existing runtime')
        app()
    else:
        logger.info('Creating a runtime')
        st_bootstrap.run(
            __file__,
            is_hello=False,
            args=[],
            flag_options={},
        )


if __name__ == "__main__":
    run()

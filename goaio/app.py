import streamlit as st
import streamlit.web.bootstrap as st_bootstrap
from goaio.ui import Ui
from goaio.utils.loghandler import get_logger

app_logger = get_logger(file_name=__name__)


def run():
    if st.runtime.exists():
        # The app has been executed with `streamlit run goaio/app.py`
        app_logger.info("===========================================================")
        app_logger.info(f'Starting the app. isRuntimeExists: {st.runtime.exists()} ')
        Ui()
    else:
        app_logger.info('Creating a runtime and starting the app')
        st_bootstrap.run(
            __file__,
            is_hello=False,
            args=[],
            flag_options={},
        )


if __name__ == "__main__":
    run()

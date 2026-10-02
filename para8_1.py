import logging

logging.basicConfig(level = logging.DEBUG,
                    filename="para8_1.log",
                    filemode="w", # a w
                    format="We have next messages: %(asctime)s:%(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")


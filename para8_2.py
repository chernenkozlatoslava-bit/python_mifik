import logging

logging.basicConfig(level = logging.DEBUG,
                    filename="para8_2.log",
                    filemode="w", # a w
                    format="We have next messages: %(asctime)s:%(levelname)s - %(message)s"
                    )


try:
    print(10/0)
except Exception:
    logging.exception("Exception")


import logging as log

class NovaCustomFormatter(log.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    
    format = "[%(levelname)s] %(name)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        log.DEBUG: grey + format + reset,
        log.INFO: grey + format + reset,
        log.WARNING: yellow + format + reset,
        log.ERROR: red + format + reset,
        log.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = log.Formatter(log_fmt)
        return formatter.format(record)


# Adding custom handler to nova logger.
# -------------------------------------
def add_custom_handler(logger:log.Logger) -> log.Logger:
    stream_handler = log.StreamHandler()
    stream_handler.setLevel(log.DEBUG)
    stream_handler.setFormatter(NovaCustomFormatter())

    logger.propagate = False
    logger.addHandler(stream_handler)
    logger.info("UwU")

    return logger

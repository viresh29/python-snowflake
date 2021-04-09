class snowflakeException(Exception):
    def __init__(self, msg):
        self.msg = msg
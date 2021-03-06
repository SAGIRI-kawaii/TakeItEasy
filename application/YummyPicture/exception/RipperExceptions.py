from application.YummyPicture import logger


class RipperNoActionException(Exception):

    def __str__(self):
        logger.exception("This is not action in ripper")


class RipperUnknownActionException(Exception):
    def __init__(self, action: str):
        self.action = action

    def __str__(self):
        logger.exception("Unknown action" + self.action)


class RipperErrorActionException(Exception):
    def __init__(self, action: str, parm: str):
        self.action = action
        self.parm = parm

    def __str__(self):
        logger.exception("Error action" + self.action + "for parm" + self.parm)


class RipperNoPeriodException(Exception):
    def __init__(self, period: str):
        self.period = period

    def __str__(self):
        logger.exception("no period" + self.period + "in periods")

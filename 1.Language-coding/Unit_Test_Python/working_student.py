from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
from Logging_module.enum_loglevel import LOG_LEVEL


class WorkingStudent:
    logger = logging.getLogger(__name__)

    def __init__(self, first_name, sec_name, dob, sal):
        self.first_name = first_name
        self.sec_name = sec_name
        self.dob = dob
        self.sal = sal

    def __repr__(self):
        return f" {self.first_name} , {self.sec_name} ," \
               f"{self.dob}, {self.sal}"

    def get_full_name(self):
        return (self.first_name + " " + self.sec_name).title()

    def increase_pay(self, percentage):
        new_pay = self.sal + (self.sal * percentage / 100)
        self.logger.debug(type(new_pay))
        return new_pay

    def get_age(self):
        """

        :param dob: dd-mm-yyyy format
        :return: age
        """

        dob_date = datetime.strptime(self.dob, "%d-%m-%Y")
        self.logger.debug(dob_date)
        cur_datetime = datetime.now().date()
        self.logger.debug(f"cur_datetime {cur_datetime}")

        r = relativedelta(cur_datetime, dob_date)
        years_diff = r.years
        months_diff = cur_datetime.month - dob_date.month
        days_diff = cur_datetime.day - dob_date.day

        self.logger.debug(f"age {years_diff} years {months_diff} months and {days_diff} days")
        return years_diff, months_diff, days_diff

    def set_logger(self, level):
        self.logger.debug(level)
        c_handler = logging.StreamHandler()
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        # c_handler.setLevel(level)
        logging.basicConfig(level=LOG_LEVEL.DEBUG.name)

        self.logger.addHandler(c_handler)


if __name__ == "__main__":
    s1 = WorkingStudent("Suman", "Banerjee", "02-03-2000", 100)
    s1.set_logger(LOG_LEVEL.TRACE.name)
    # s1.set_logger(logging.DEBUG) # same and preferable in case of logging but just to see how enums works
    # we have created our own custom enums for constants

    s1.get_age()

    s2 = WorkingStudent("Suman", "Banerjee", "22-05-2020", 100)
    s2.get_age()

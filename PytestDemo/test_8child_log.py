from PytestDemo.parent_class_of_logs import Base_class


class Test_child_class(Base_class):
    def test_firstMethod(self):
        log = self.log_demo()
        log.info("Inside child class of logs")
        log.info("will be seen in HTML reports now")



from config.config import Base
from sqlalchemy import Column, Integer, String, Date


class TestClass2(Base):
    __tablename__ = 'test_table2'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    sex = Column(String)

    # published = Column(Date)

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def __repr__(self):
        return "<Person(name='{} {}', age={}, sex={})>" \
            .format(self.first_name, self.last_name, self.age, self.sex)

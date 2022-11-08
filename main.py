import argparse
import sys
from argparse import ArgumentParser
from models.test_class1 import TestClass1
from models.test_class2 import TestClass2
from models.test_class3 import TestClass3
from config.config import Session, engine, Base


def recreate_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def db_operation():
    recreate_db()
    session = Session()
    test1_data1 = TestClass1("f1", "l1", 25, "M")
    test2_data1 = TestClass2("f1", "l1", 25, "M")
    test3_data1 = TestClass3("f1", "l1", 25, "M")
    session.add(test1_data1)
    session.add(test2_data1)
    session.add(test3_data1)
    session.commit()
    session.close()


def main():
    parser = ArgumentParser()
    parser.add_argument("-e", "--environment", required=True, choices=("prod", "dev", "test"))
    parser.add_argument("-u", "--user_args")
    args = parser.parse_args()
    env = args.environment
    print(env)
    if env == "test":
        try:
            u_args = args.user_args
            print(u_args)
        except KeyError:
            print("unable to get user args")


if __name__ == "__main__":
    # main()
    db_operation()

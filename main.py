from application import salary
from datetime import date
import application.db.people as people


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(f"Today: {date.today()}")

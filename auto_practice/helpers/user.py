from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    first_name: str = None
    last_name: str = None
    email: str = None
    gender: str = None
    current_address: str = None
    mobile: str = None
    subject: str = None
    dob: datetime = None

    # because result format and input format do not match
    def to_dict(self):
        data = {'Student Name': f"{self.first_name} {self.last_name}",
                'Student Email': self.email,
                'Gender': self.gender.capitalize(),
                'Mobile': self.mobile,
                'Date of Birth': f"{self.dob.strftime('%d %B,%Y')}",
                'Subjects': '',
                'Hobbies': '',
                'Picture': '',
                'Address': '',
                'State and City': ''}
        return data

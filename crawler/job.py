
class Job:

    def __init__(self, id, title, employer_name, address, description, publishing_date):
        self.id = id
        self.title = title
        self.employer_name = employer_name
        self.address = address
        self.description = description
        self.publishing_date = publishing_date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'employer_name': self.employer_name,
            'description': self.description,
            'job_address': self.address,
            'publishing_date': self.publishing_date,
        }

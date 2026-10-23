class Course:
    def __init__(self, course_id, name, credits, prerequisites=None, schedule=None):
        self.course_id = str(course_id)
        self.name = name
        self.credits = credits
        self.prerequisites = prerequisites or []
        self.schedule = schedule or []

    def __repr_(self):
        return f"Course({self.course_id!r}, {self.name!r}, {self.credits})"

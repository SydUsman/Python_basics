class User:
    def __init__(self, user_name, user_email, user_job_title):
        self.name = user_name
        self.email = user_email
        self.job_title = user_job_title

    def get_user_info(self):
        print(
            f"User {self.name} works as a {self.job_title}. You can contact him at {self.email}")

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

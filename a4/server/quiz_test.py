from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)

    # Student APIs
    @task
    def create_student(self):
        payload = {
            "prn": "995",
            "name": "John Doe",
            "pass": "password",
            "branch": "CSE"
        }
        self.client.post("/create/student", json=payload)

    @task
    def create_nft(self):
        payload = {
            "email": "john.doe@example.com",
            "password": "password"
        }
        self.client.post("/cr/student", json=payload)

    @task
    def get_nft_data(self):
        self.client.get("/getData")

    @task
    def delete_nft_record(self):
        self.client.post("/deleteRecord/john.doe@example.com")

    @task
    def update_student(self):
        payload = {
            "upemail": "jane.doe@example.com",
            "uppassword": "new_password"
        }
        self.client.post("/update/student/john.doe@example.com", json=payload)

    # Teacher APIs
    @task
    def create_teacher(self):
        payload = {
            "name": "Jane Smith",
            "pass": "password",
            "dept": "Mathematics"
        }
        self.client.post("/create/teacher", json=payload)

    # Quiz APIs
    @task
    def create_quiz(self):
        payload = {
            "quiz_id": 1,
            "quiz_timer": 60,
            "queList": [
                {
                    "que": "What is the capital of India?",
                    "optA": "Mumbai",
                    "optB": "New Delhi",
                    "optC": "Kolkata",
                    "optD": "Chennai",
                    "ans": "B"
                },
                {
                    "que": "What is the capital of Japan?",
                    "optA": "Tokyo",
                    "optB": "Kyoto",
                    "optC": "Osaka",
                    "optD": "Hiroshima",
                    "ans": "A"
                }
            ],
            "t_id": 1
        }
        self.client.post("/create/quiz", json=payload)

    @task
    def initialize_result(self):
        payload = {
            "prn": "12345",
            "quizID": 1
        }
        self.client.post("/result/init", json=payload)

    @task
    def submit_quiz(self):
        payload = {
            "quiz_id": 1,
            "prn": "12345",
            "selectedOpts": [
                {
                    "q_id": 1,
                    "selected_opt": "B"
                },
                {
                    "q_id": 2,
                    "selected_opt": "A"
                }
            ]
        }
        self.client.post("/quiz/submit", json=payload)

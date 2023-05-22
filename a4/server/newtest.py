from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_result(self):
        quiz_id = 1  # replace with actual quiz_id value to query
        self.client.get(f"/get/result/{quiz_id}")

    @task
    def get_quiz(self):
        quiz_id = 1  # replace with actual quiz_id value to query
        self.client.get(f"/get/quiz/{quiz_id}")

    @task
    def get_my_quizes(self):
        t_id = 1  # replace with actual t_id value to query
        self.client.get(f"/get/my-quizes/{t_id}")

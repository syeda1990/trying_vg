from config_tests import TestConfig

class TestStudentsView(TestConfig):
    def test_home_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("<td>zara</td>", response.data.decode("utf-8"))

    def test_add_student_get_route(self):
        response = self.app.get("/add_student")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<input type="text" id="name" name="name" required>', response.data.decode("utf-8"))

    def test_add_student_post_route(self):
        response = self.app.post(
            "/add_student",
            data={"name": "zara", "age": 23, "grade": "g", "subjects": "maths, arts"}
        )
        self.assertEqual(response.status_code, 302)

        response = self.app.get("/")
        self.assertIn("<td>zara</td>", response.data.decode("utf-8"))
    
    def test_view_student_route(self):
        response = self.app.get("/view_student/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("zara", response.data.decode("utf-8"))

    def test_update_student_get_route(self):
        response = self.app.get("/update_student/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<input type="text" id="name" name="name" value = "zara" required>', response.data.decode("utf-8"))

    def test_update_student_post_route(self):
        response = self.app.post(
            "/update_student/1",
            data={"name": "Zara Updated", "age": 24, "grade": "vg", "subjects": "History, Math"}
        )
        self.assertEqual(response.status_code, 302)

        response = self.app.get("/")
        self.assertIn("Zara Updated", response.data.decode("utf-8"))

    def test_delete_student_route(self):
        response = self.app.post("/delete_student/1")
        self.assertEqual(response.status_code, 302)

        response = self.app.get("/")
        self.assertNotIn("<td>zara</td>", response.data.decode("utf-8"))
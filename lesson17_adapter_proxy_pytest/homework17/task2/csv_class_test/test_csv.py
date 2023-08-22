import csv
from lesson17_adapter_proxy_pytest.homework17.task2.csv_func_for_testing import CSVController


class TestCSV:

    def setup_class(self):
        self.csv_file = "example.csv"

    def test_add_row(self):
        manipulator = CSVController(self.csv_file)
        test_row = ["TestFirstName", "TestLastName", "25", "Male", "5000"]

        manipulator.add_row(test_row)

        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            assert test_row in rows

    def test_delete_row(self):
        handler = CSVController(self.csv_file)

        initial = [
            ["Elizabet", "Fork", "19", "Female", "3000"],
            ["Reginald", "Lidoo", "42", "Male", "2500"],
            ["Alexander", "Great", "30", "Male", "15000"]
        ]
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(initial)

        row_to_delete = 1
        handler.delete_row(row_to_delete)

        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            remaining_rows = list(reader)
            assert len(remaining_rows) == len(initial) - 1
            assert remaining_rows[row_to_delete] != ["Reginald", "Lidoo", "42", "Male", "2500"]
import unittest
import os
import subprocess

class TrainingQuickStartTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        os.environ['LAMINI_API_KEY'] = os.environ['STAGING_KEY']
        os.environ['LAMINI_API_URL'] = 'https://api.staging.powerml.co'

    def test_quick_start(self):
        response = subprocess.run(['python3', 'docs/docs/tuning/code/quick_start.py'], capture_output=True, env=os.environ)

        stdout = response.stdout.decode('utf-8').strip()
        stderr = response.stderr.decode('utf-8').strip()

        self.assertEqual(response.returncode, 0, f"Script exited with error: {stderr}") # Assert no errors
        print(stdout)
        assert "submitted" in stdout # Not great, but checking the job was submitted by checking output

    def test_hyperparameters(self):
        response = subprocess.run(['python3', 'docs/docs/tuning/code/hyperparameters.py'], capture_output=True, env=os.environ)
        stdout = response.stdout.decode('utf-8').strip()
        stderr = response.stderr.decode('utf-8').strip()

        self.assertEqual(response.returncode, 0, f"Script exited with error: {stderr}") # Assert no errors
        print(stdout)
        assert "submitted" in stdout # Not great, but checking the job was submitted by checking output

    def test_large_data_files_csv(self):
        response = subprocess.run(['python3', 'docs/docs/tuning/code/large_data_files_csv.py'], capture_output=True, env=os.environ)

        stdout = response.stdout.decode('utf-8').strip()
        stderr = response.stderr.decode('utf-8').strip()

        self.assertEqual(response.returncode, 0, f"Script exited with error: {stderr}") # Assert no errors
        print(stdout)
        assert "submitted" in stdout # Not great, but checking the job was submitted by checking output

    def test_large_data_files_json(self):
        response = subprocess.run(['python3', 'docs/docs/tuning/code/large_data_files_jsonl.py'], capture_output=True, env=os.environ)

        stdout = response.stdout.decode('utf-8').strip()
        stderr = response.stderr.decode('utf-8').strip()

        self.assertEqual(response.returncode, 0, f"Script exited with error: {stderr}") # Assert no errors
        print(stdout)
        assert "submitted" in stdout # Not great, but checking the job was submitted by checking output

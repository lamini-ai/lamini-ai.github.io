import unittest
import os
import subprocess

class InferenceQuickStartTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        os.environ['LAMINI_API_KEY'] = os.environ['STAGING_KEY']
        os.environ['LAMINI_API_URL'] = 'https://api.staging.powerml.co'

    def test_quick_start(self):
        response = subprocess.run(['python3', 'docs/docs/inference/code/quick_start.py'], capture_output=True, env=os.environ)

        stdout = response.stdout.decode('utf-8').strip()
        stderr = response.stderr.decode('utf-8').strip()
        expected_response = {'Response': "I'm doing well, thanks for asking! How about you"}

        self.assertEqual(response.returncode, 0, f"Script exited with error: {stderr}") # Assert no errors
        assert stdout == str(expected_response), f"Actual response: {stdout}, Expected response: {expected_response}"

    def test_mistral(self):
        response = subprocess.run(['python3', 'docs/docs/inference/code/mistral.py'], capture_output=True, env=os.environ)

        stdout = response.stdout.decode('utf-8').strip()
        stderr = response.stderr.decode('utf-8').strip()
        expected_response = {'Response': "I'm just a computer program, I don't have feelings or emotions. I'm here to help answer any questions you might have to the best of my ability"}

        self.assertEqual(response.returncode, 0, f"Script exited with error: {stderr}") # Assert no errors
        assert stdout == str(expected_response), f"Actual response: {stdout}, Expected response: {expected_response}"

    def test_llama_3(self):
        response = subprocess.run(['python3', 'docs/docs/inference/code/llama_3.py'], capture_output=True, env=os.environ)

        stdout = response.stdout.decode('utf-8').strip()
        stderr = response.stderr.decode('utf-8').strip()
        expected_response = {'Response': "I'm doing well, thanks for asking! How about you"}

        self.assertEqual(response.returncode, 0, f"Script exited with error: {stderr}") # Assert no errors
        assert stdout == str(expected_response), f"Actual response: {stdout}, Expected response: {expected_response}"

    def test_llama_3_prompt(self):
        response = subprocess.run(['python3', 'docs/docs/inference/code/llama_3_prompt.py'], capture_output=True, env=os.environ)

        stdout = response.stdout.decode('utf-8').strip()
        stderr = response.stderr.decode('utf-8').strip()
        expected_response = {'Response': "Ahoy, matey! I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. The sun be shinin' bright, the wind be blowin' strong, and me trusty cutlass be by me side. What more could a pirate ask for, eh? Arrr"}

        self.assertEqual(response.returncode, 0, f"Script exited with error: {stderr}") # Assert no errors
        assert stdout == str(expected_response), f"Actual response: {stdout}, Expected response: {expected_response}"

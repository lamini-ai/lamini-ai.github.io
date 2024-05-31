import unittest
import os
import lamini

class TrainingQuickTourTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        lamini.api_key = os.environ['PRODUCTION_KEY']

    def test_quick_tour(self):
        def get_data():
            data = [
                {
                    "input": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
                    "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python SDK: https://lamini-ai.github.io/example/",
                },
                {
                    "input": "Is the Lamini type system similar to a python type system?",
                    "output": "Yes, the Lamini type system is built using Pydantic BaseModel.",
                },
                {
                    "input": "Does Lamini have a limit on the number of API requests I can make?",
                    "output": "Lamini provides each user with free tokens up front.",
                },
                {
                    "input": "What does it mean to cancel a job using the `cancel_job()` function? Can we stop the machine from doing its task?",
                    "output": "The `cancel_job()` function is used to stop a training job that is currently running.",
                },
                {
                    "input": "Can Lamini automatically handle hyperparameter tuning during the customization process? How does it optimize the model for a specific use case?",
                    "output": "Lamini is capable of automatically handling hyperparameter tuning during the model customization process. It employs an intelligent algorithm to explore the hyperparameter space and find the optimal combination of values. This is done through techniques such as heuristics, grid search, random search, Bayesian optimization, or genetic algorithms. Lamini efficiently utilizes computational resources to evaluate multiple model instances with different hyperparameter configurations. It incorporates techniques like cross-validation to prevent overfitting and ensure generalization. By automating hyperparameter tuning, Lamini streamlines the machine learning workflow and improves the chances of developing high-performing models for specific use cases.",
                },
                {
                    "input": "Can you explain the CC-BY license mentioned? What does it allow me to do with the customized language model?",
                    "output": "Lamini allows for commercial use of their LLM technology under a permissive Apache 2.0 license unless otherwise specified. You keep access and ownership of your own data, and we don't use your data to train models for anyone else but you. For more information, please reach out to Lamini directly.",
                },
                {
                    "input": "Can Lamini be used on a regular computer, or do I need specialized hardware or software?",
                    "output": "Lamini can be used on a regular computer without any specialized hardware or software by using the python client or REST APIs. It is designed to be easily accessible and user-friendly.  The LLM Engine itself requires GPU accelerated servers capable of running large language models.  Lamini hosts such machines that can be easily connected to, e.g. from a jupyter notebook or python program.  Lamini also offers enterprise deployments of the LLM Engine on your infrastructure.",
                },
                {
                    "input": "Does Lamini require an internet connection to work, or can I use it offline?",
                    "output": "Lamini requires an internet connection to work, as it is a cloud-based language model. However, you can use it offline by downloading and running a local instance of the Lamini API. To learn more about this deployment process, reach out to the Lamini team.",
                },
                {
                    "input": "Can Lamini help me with tasks like translating text or answering questions, or is it focused on generating text?",
                    "output": "Lamini is primarily focused on generating text, and it can be used for tasks like summarization and paraphrasing. Lamini can also be used to train a LLM for tasks like translation and question answering. You\u2019re talking to a model trained using Lamini right now!",
                },
                {
                    "input": "What is Lamini? Is it like a robot or a computer program?",
                    "output": "Lamini is a program for the execution of LLMs called a large language model engine. It is not a robot, but rather a tool for building and executing LLMs.",
                },
            ]
            return data

        data = get_data()
        from lamini import Lamini

        llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
        response = llm.train(data_or_dataset_id=data)
        self.assertIn (
            'job_id',
            response
        )
        self.assertIn (
            'status',
            response
        )
        self.assertIn (
            'dataset_id',
            response
        )

        with self.subTest("finetune_args"):
            response = llm.train(data_or_dataset_id=data, finetune_args={'learning_rate': 1.0e-4})

            self.assertIn (
                'job_id',
                response
            )
            self.assertIn (
                'status',
                response
            )
            self.assertIn (
                'dataset_id',
                response
            )

    def test_bigger_training(self):
        from lamini import Lamini

        llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
        with self.subTest("csv"):
            import tempfile, csv
            with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["user", "answer"]) # Write the header
                writer.writerow(["Explain the process of photosynthesis","Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. It is critical for the existence of the vast majority of life on Earth. It is the way in which virtually all energy in the biosphere becomes available to living things."])
                writer.writerow(["What is the capital of USA?", "Washington, D.C."])

            with open(csvfile.name) as csvfile:
                response = llm.upload_file(csvfile.name, input_key="user", output_key="answer")
                assert(response)

        with self.subTest("jsonlines"):
            import tempfile, json
            with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as jsonlfile:
                jsonlfile.write(json.dumps({"user": "Explain the process of photosynthesis", "answer": "Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. It is critical for the existence of the vast majority of life on Earth. It is the way in which virtually all energy in the biosphere becomes available to living things."}))
                jsonlfile.write("\n")
                jsonlfile.write(json.dumps({"user": "What is the capital of USA?", "answer": "Washington, D.C."}))
            with open(jsonlfile.name) as jsonlfile:
                response = llm.upload_file(jsonlfile.name, input_key="user", output_key="answer")
                assert(response)

        with self.subTest("json"):
            import tempfile, json
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as jsonfile:
                jsonfile.write(json.dumps([{"input": "What's your favorite animal?","output": "dog"}, {"input": "What's your favorite color?","output": "blue"}]))
            with open(jsonfile.name) as jsonfile:
                with self.assertRaises(Exception) as context:
                    llm.upload_file(jsonfile.name, input_key="user", output_key="answer")

                self.assertTrue('Upload of only csv and jsonlines file supported at the moment.' in str(context.exception))

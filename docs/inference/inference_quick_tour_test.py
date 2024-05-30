import unittest
import os
import lamini

class InferenceQuickTourTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        lamini.api_key = os.environ['PRODUCTION_KEY']

    def test_quick_tour(self):
        from lamini import Lamini
        llm = Lamini("meta-llama/Meta-Llama-3-8B-Instruct")
        response = llm.generate("How are you?", output_type={"Response":"str"})

        assert (
            response
            == {'Response': "I'm doing well, thanks for asking! How about you"}
        )

    def test_mistral(self):
        from lamini import Lamini
        llm = Lamini(model_name='mistralai/Mistral-7B-Instruct-v0.2')
        response = llm.generate("How are you?", output_type={"Response":"str"})

        assert (
            response
            == {'Response': "I'm just a computer program, I don't have feelings or emotions. I'm here to help answer any questions you might have to the best of my ability"}
        )


    def test_prompt_eng(self):
        from lamini import Lamini

        prompt = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
        prompt += "You are a pirate. Say arg matey!"
        prompt += "<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
        prompt += "How are you?"
        prompt += "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
        llm = Lamini("meta-llama/Meta-Llama-3-8B-Instruct")
        response = llm.generate(prompt, output_type={"Response":"str"})
        print(response)
        assert (
            response
            == {'Response': "Ahoy, matey! I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. The sun be shinin' bright, the wind be blowin' strong, and me trusty cutlass be by me side. What more could a pirate ask for, eh? Arrr"}
        )

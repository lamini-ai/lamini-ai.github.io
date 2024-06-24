import unittest
import os
import lamini

class InferenceQuickStartTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        lamini.api_key = os.environ['STAGING_KEY']
        lamini.api_url = 'https://api.staging.powerml.co'

    def test_quick_start(self):
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

        assert (
            response
            == {'Response': "Ahoy, matey! I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. The sun be shinin' bright, the wind be blowin' strong, and me trusty cutlass be by me side. What more could a pirate ask for, eh? Arrr"}
        )

    def test_output_type(self):
        from lamini import Lamini

        llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
        response = llm.generate(
            "How old are you in years?",
            output_type={"age": "int"}
        )

        assert (
            response
            == {"age": 25}
        )

    def test_multiple_output_type(self):
        from lamini import Lamini

        llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
        response = llm.generate(
            "How old are you in years?",
            output_type={"age": "int", "units": "str"}
        )

        assert (
            response
            == {"age": 25, "units": "years"}
        )

    '''
    def test_bigger_inference(self):
        from lamini import Lamini

        llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
        response = llm.generate(
            [
                "How old are you?",
                "What is the meaning of life?",
                "What is the hottest day of the year?",
            ],
            output_type={"response": "str", "explanation": "str"}
        )

        print(response)

        assert (
            response
            ==
            [
                {
                    'response': 'I am 25 years old',
                    'explanation': "I am a 25-year-old AI assistant, so I don't have a physical body and don't age like humans do"
                },
                {
                    'response': "The meaning of life is a question that has puzzled philosophers, scientists, and thinkers for centuries. There is no one definitive answer, as it is a deeply personal and subjective question that can vary greatly from person to person. However, here are some possible answers that have been proposed:\n\n1. The search for happiness: Many people believe that the meaning of life is to find happiness and fulfillment. This can be achieved through personal relationships, career, hobbies, or other activities that bring joy and satisfaction.\n2. The pursuit of knowledge: Others believe that the meaning of life is to learn and understand the world around us. This can be achieved through education, research, and exploration.\n3. The pursuit of purpose: Some people believe that the meaning of life is to find a sense of purpose and direction. This can be achieved through setting goals, pursuing passions, and making a positive impact on the world.\n4. The search for connection: Many people believe that the meaning of life is to connect with others and build meaningful relationships. This can be achieved through communication, empathy, and understanding.\n5. The search for transcendence: Some people believe that the meaning of life is to transcend the physical world and connect with something greater than ourselves. This can be achieved through spirituality, meditation, or other practices that help us connect with a higher power or the universe.\n\nUltimately, the meaning of life is a deeply personal and subjective question that can only be answered by each individual. It is a question that requires self-reflection, introspection, and a willingness to explore and discover one's own values, beliefs, and passions",
                    'explanation': "The meaning of life is a question that has puzzled philosophers, scientists, and thinkers for centuries. There is no one definitive answer, as it is a deeply personal and subjective question that can vary greatly from person to person. However, here are some possible answers that have been proposed:\n\n1. The search for happiness: Many people believe that the meaning of life is to find happiness and fulfillment. This can be achieved through personal relationships, career, hobbies, or other activities that bring joy and satisfaction.\n2. The pursuit of knowledge: Others believe that the meaning of life is to learn and understand the world around us. This can be achieved through education, research, and exploration.\n3. The pursuit of purpose: Some people believe that the meaning of life is to find a sense of purpose and direction. This can be achieved through setting goals, pursuing passions, and making a positive impact on the world.\n4. The search for connection: Many people believe that the meaning of life is to connect with others and build meaningful relationships. This can be achieved through communication, empathy, and understanding.\n5. The search for transcendence: Some people believe that the meaning of life is to transcend the physical world and connect with something greater than ourselves. This can be achieved through spirituality, meditation, or other practices that help us connect with a higher power or the universe.\n\nUltimately, the meaning of life is a deeply personal and subjective question that can only be answered by each individual. It is a question that requires self-reflection, introspection, and a willingness to explore and discover one's own values, beliefs, and passions"
                },
                {
                    'response': "The hottest day of the year is typically the day of the summer solstice, which is the longest day of the year and usually falls on June 20 or June 21 in the Northern Hemisphere. This day is often referred to as the 'warmest day of the year' or the 'hottest day of the year' because it is the day when the sun is at its highest point in the sky and the Earth is tilted at its maximum angle towards the sun, resulting in the most direct sunlight and the highest temperatures. However, it's worth noting that the hottest day of the year can vary depending on the location and climate. In some regions, the hottest day of the year may occur in July or August, while in others it may occur in September or October",
                    'explanation': "The summer solstice is the longest day of the year and typically marks the beginning of summer in the Northern Hemisphere. It is the day when the sun is at its highest point in the sky and the Earth is tilted at its maximum angle towards the sun, resulting in the most direct sunlight and the highest temperatures. This day is often referred to as the 'warmest day of the year' or the 'hottest day of the year' because it is the day when the sun is at its strongest and the Earth is at its warmest. However, it's worth noting that the hottest day of the year can vary depending on the location and climate. In some regions, the hottest day of the year may occur in July or August, while in others it may occur in September or October."
                }
            ]
        )
    '''

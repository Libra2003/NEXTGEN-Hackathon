from clarifai.client.model import Model

prompt = "What’s the future of AI?"

# openai_api_key = OpenAI_API_KEY

inference_params = dict(temperature=0.2, max_tokens=600)

# Model Predict
model_prediction = Model("https://clarifai.com/openai/chat-completion/models/gpt-4-turbo").predict_by_bytes(prompt.encode(), input_type="text", inference_params=inference_params)

print(model_prediction.outputs[0].data.text.raw)


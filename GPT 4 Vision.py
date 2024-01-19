from clarifai.client.model import Model
import base64

image_path = "C:\\Users\\pak\Desktop\\Hackthons\\NextGen GPT AI Hackathon with Clarifai\\image1.png"

with open(image_path, "rb") as f:
  base64image = base64.b64encode(f.read()).decode('utf-8')

prompt = "Write the contents of the page like reading a book?"

inference_params = dict(temperature=0.2, max_tokens=1000, image_base64=base64image)

# Model Predict
model_prediction = Model("https://clarifai.com/openai/chat-completion/models/gpt-4-vision").predict_by_bytes(prompt.encode(), input_type="text", inference_params=inference_params)
print(model_prediction.outputs[0].data.text.raw)

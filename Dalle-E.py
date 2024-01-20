from clarifai.client.model import Model
convo1 = """Create a pi chart divided by 60 30 5 2 1 2 and divide the pie accordingly"""
# conv2 = "Do you enjoy space-themed movies or TV shows? What are some of your favorites? If not, what do you dislike about them?"

prompt = f"{convo1}"


inference_params = dict(quality="standard", size='1024x1024')

# Model Predict
model_prediction = Model("https://clarifai.com/openai/dall-e/models/dall-e-3").predict_by_bytes(prompt.encode(), input_type="text", inference_params=inference_params)

output_base64 = model_prediction.outputs[0].data.image.base64

with open('image.png', 'wb') as f:
    f.write(output_base64)

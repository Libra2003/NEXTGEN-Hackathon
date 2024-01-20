from clarifai.client.model import Model

input = "I love your product very much"


inference_params = dict(voice="alloy", speed=1.0)

# Model Predict
model_prediction = Model("https://clarifai.com/openai/tts/models/openai-tts-1").predict_by_bytes(input.encode(), input_type="text", inference_params=inference_params)

output_base64 = model_prediction.outputs[0].data.audio.base64
audio_filename = f"output_audio.wav"
with open(audio_filename, 'wb') as f:
      f.write(output_base64)

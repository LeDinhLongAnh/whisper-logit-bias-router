import whisper
import logit_bias
import json

print('Loading whisper model (base.en)...')
# This will download the model to the .models folder on the first run
model = whisper.load_model('base.en', download_root='.models')

print('Loading logit bias config...')
bias_cfg = logit_bias.load_logit_bias_config('logit_bias.json')
tokenizer = whisper.tokenizer.get_tokenizer(multilingual=False, language='en', task='transcribe')
bias_filter = logit_bias.build_bias_filter(bias_cfg, tokenizer)

# Load global prompt from scenarios.json
with open('scenarios.json', 'r', encoding='utf-8') as f:
    scenarios = json.load(f)
global_prompt = scenarios.get('global_prompt', '')

def process_audio(audio_path):
    print(f'Transcribing {audio_path}...')
    text, elapsed_time = logit_bias.transcribe_with_bias(
        model=model,
        audio=audio_path,
        prompt=global_prompt,
        bias_filter=bias_filter
    )
    print(f'Result: {text}')
    print(f'Time: {elapsed_time:.2f}s')
    return text

if __name__ == '__main__':
    print('Ready! Replace "test.wav" with your actual audio file.')
    # result = process_audio('test.wav')

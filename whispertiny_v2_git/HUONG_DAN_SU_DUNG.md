# Hướng Dẫn Tích Hợp Initial Prompt & Logit Bias Vào Whisper

Tài liệu này hướng dẫn bạn cách tích hợp cơ chế **Initial Prompt** và **Logit Bias** vào hệ thống nhận diện giọng nói (STT) hiện tại của bạn dựa trên thư viện OpenAI Whisper.

Giải pháp này sử dụng kỹ thuật *monkey-patching* để can thiệp trực tiếp vào thư viện Whisper ở mức runtime. **Bạn không cần phải sửa đổi mã nguồn gốc của thư viện Whisper.**

## 1. Yêu cầu hệ thống (Prerequisites)

- Python 3.8 trở lên.
- Thư viện Whisper chính thức từ OpenAI.
- fmpeg đã được cài đặt trên hệ thống (dùng để xử lý audio).

**Cài đặt các thư viện cần thiết:**
``bash
pip install -U openai-whisper
``

## 2. Thành phần của gói chia sẻ

Khi tải kho lưu trữ (repository) này về, bạn sẽ có các file quan trọng sau:
- **logit_bias.py**: Chứa logic xử lý can thiệp vào Whisper (cốt lõi của hệ thống).
- **logit_bias.json**: File cấu hình chứa các từ khoá cần ưu tiên nhận diện (bias) và mức độ ưu tiên (trọng số).
- **scenarios.json**: File chứa global_prompt - mồi ngữ cảnh giúp Whisper nhận diện sát với Domain hơn.
- **example_usage.py**: Script mẫu để bạn tham khảo cách gọi hàm.

## 3. Cách tích hợp vào source code của bạn

Nếu bạn đang có một hệ thống Router và muốn cắm Whisper này vào, hãy làm theo các bước sau:

### Bước 3.1. Đưa file vào project của bạn
Copy 3 file sau vào cùng thư mục chứa code của bạn:
1. logit_bias.py
2. logit_bias.json
3. scenarios.json

### Bước 3.2. Viết code gọi model

Trong file code xử lý STT của bạn, hãy import và setup theo mẫu sau:

``python
import whisper
import logit_bias
import json

# 1. Tải Whisper Model (Lần đầu chạy sẽ tự động tải model từ internet)
print("Đang tải model Whisper...")
# Lưu ý: Nếu bạn ĐÃ tải sẵn model Whisper trên máy từ trước (ở thư mục mặc định), 
# hãy xoá tham số download_root=".models" để Whisper dùng lại model cũ, tránh tải lại.
# Ví dụ: model = whisper.load_model("base.en")
model = whisper.load_model("base.en", download_root=".models")

# 2. Khởi tạo Logit Bias Filter
print("Đang cấu hình Logit Bias...")
# Đọc file cấu hình từ vựng
bias_cfg = logit_bias.load_logit_bias_config("logit_bias.json")

# Lấy tokenizer chuẩn của Whisper
tokenizer = whisper.tokenizer.get_tokenizer(
    multilingual=False, 
    language="en", 
    task="transcribe"
)

# Tạo filter ép từ khóa (bias_filter)
bias_filter = logit_bias.build_bias_filter(bias_cfg, tokenizer)

# 3. Nạp Initial Prompt (Mồi ngữ cảnh)
# Đọc từ file scenarios.json (Hoặc bạn có thể gán thẳng chuỗi string vào biến này)
with open("scenarios.json", "r", encoding="utf-8") as f:
    scenarios = json.load(f)
global_prompt = scenarios.get("global_prompt", "")

# 4. Hàm xử lý file âm thanh
def transcribe_audio(audio_path):
    \"\"\"
    Nhận diện giọng nói áp dụng Initial Prompt và Logit Bias.
    \"\"\"
    print(f"Đang xử lý: {audio_path}")
    
    # Dùng hàm transcribe_with_bias THAY VÌ model.transcribe thông thường
    text, elapsed_time = logit_bias.transcribe_with_bias(
        model=model,
        audio=audio_path,
        prompt=global_prompt,    # Truyền Initial Prompt vào đây
        bias_filter=bias_filter  # Truyền bộ lọc ép từ vào đây
    )
    
    print(f"Kết quả nhận diện: {text}")
    print(f"Thời gian xử lý: {elapsed_time:.2f}s")
    
    return text

# 5. Chạy thử
if __name__ == "__main__":
    audio_file = "test.wav" # Thay bằng đường dẫn file âm thanh thực tế của bạn
    
    # KẾT QUẢ ĐẦU RA (result) LÀ ĐẦU VÀO CHO ROUTER CỦA BẠN
    result = transcribe_audio(audio_file)
``

## 4. Cách tuỳ chỉnh từ vựng và ngữ cảnh (Nâng cao)

Sau khi hệ thống đã chạy được, bạn hoàn toàn có thể thay đổi cách nhận diện mà **không cần đụng vào code python**, chỉ cần sửa file JSON:

- **Sửa scenarios.json (Trường global_prompt):** 
  Thay đổi đoạn văn mồi để định hướng ngữ pháp và bối cảnh chung cho Whisper. Nên dùng một câu dài chứa các từ khoá phổ biến của Domain.
  
- **Sửa logit_bias.json:**
  - Thêm/bớt các từ khoá cần bắt (ví dụ: Wi-Fi, outer, QoS...).
  - Điều chỉnh ias: Mức tăng xác suất (ví dụ 1.0 đến 3.0). Bias quá cao có thể gây "ảo giác" (hallucination) khiến từ đó xuất hiện mọi nơi dù không có tiếng nói, nên tăng từ từ.


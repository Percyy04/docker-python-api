# Face Recognition API

API để nhận diện khuôn mặt từ base64 image sử dụng InsightFace.

## Cài đặt

### Sử dụng Conda Environment (Khuyến nghị)

1. Kích hoạt conda environment:

```bash
conda activate face-checkin
```

2. Cài đặt dependencies (nếu chưa có):

```bash
pip install -r requirements.txt
```

3. Đảm bảo đã build face database:

```bash
python build_face_db.py
```

4. Chạy API server:

**Trên Windows:**

```bash
# Cách 1: Sử dụng script
run_api.bat

# Cách 2: Chạy trực tiếp
conda activate face-checkin
python api.py
```

**Trên Linux/Mac:**

```bash
# Cách 1: Sử dụng script
chmod +x run_api.sh
./run_api.sh

# Cách 2: Chạy trực tiếp
conda activate face-checkin
python api.py
```

**Hoặc sử dụng conda run:**

```bash
conda run -n face-checkin python api.py
```

API sẽ chạy tại `http://localhost:8000`

### Không sử dụng Conda

1. Cài đặt dependencies:

```bash
pip install -r requirements.txt
```

2. Đảm bảo đã build face database:

```bash
python build_face_db.py
```

3. Chạy API server:

```bash
python api.py
```

## Endpoints

### POST /recognize

Nhận diện khuôn mặt từ base64 image.

**Request:**

```json
{
  "image": "base64_string_here"
}
```

**Response thành công:**

```json
{
  "users": [
    {
      "userId": "F01",
      "name": "Nguyen Van A",
      "confidence": 0.95,
      "house": "House A"
    }
  ],
  "detected_faces": 1,
  "recognized_faces": 1
}
```

**Response khi không có khuôn mặt:**

```json
{
  "users": [],
  "message": "No faces detected"
}
```

### GET /health

Kiểm tra trạng thái API và database.

**Response:**

```json
{
  "status": "ok",
  "model_loaded": true,
  "database_size": 100
}
```

### GET /api/users

Lấy danh sách users đã check-in (từ checkedin_users.json).

## Cấu hình Frontend

Trong file `.env` của frontend, đặt:

```
VITE_AI_API_URL=http://localhost:8000/recognize
```

Hoặc trong code frontend:

```javascript
const AI_API_URL = "http://localhost:8000/recognize";
```

## Lưu ý

- API sử dụng port 8000 mặc định
- Cần build database trước khi sử dụng API
- Threshold mặc định là 0.4 (có thể thay đổi trong `src/config.py`)
- API hỗ trợ CORS để frontend có thể gọi từ browser

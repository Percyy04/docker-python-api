# Docker Deployment Guide

## Cách build và chạy Docker image

### 1. Build Docker image

```bash
docker build -t gala-face-checkin:latest .
```

### 2. Chạy container

```bash
docker run -d \
  --name gala-face-checkin \
  -p 8000:8000 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/checkedin_users.json:/app/checkedin_users.json \
  gala-face-checkin:latest
```

### 3. Sử dụng Docker Compose (Khuyến nghị)

```bash
# Build và chạy
docker-compose up -d

# Xem logs
docker-compose logs -f

# Dừng
docker-compose down
```

## Lưu ý quan trọng

1. **Face Database**: Đảm bảo bạn đã build face database trước khi chạy container:

   ```bash
   python build_face_db.py
   ```

   Hoặc mount thư mục `data/processed/` chứa:

   - `face_embeddings.npy`
   - `face_labels.csv`

2. **Port**: Mặc định sử dụng port 8000. Có thể thay đổi bằng biến môi trường `PORT`

3. **Volumes**:

   - `./data` - Lưu trữ face database
   - `./checkedin_users.json` - Lưu trữ danh sách check-in

4. **Health Check**: API có endpoint `/health` để kiểm tra trạng thái

## Kiểm tra container

```bash
# Xem logs
docker logs gala-face-checkin

# Kiểm tra health
curl http://localhost:8000/health

# Vào trong container
docker exec -it gala-face-checkin bash
```

## Deploy lên cloud

### Render.com

- Sử dụng Dockerfile có sẵn
- Set environment variable: `PORT` (Render tự động set)

### Railway

- Sử dụng Dockerfile
- Set `PORT` environment variable

### Heroku

- Sử dụng Dockerfile
- Heroku tự động detect và build

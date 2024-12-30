## Elephant Detection
- Clone repository.
```bash
git clone https://github.com/B-Mayur/elephant_detection.git
cd elephant_detection
```

- Install docker

- Pull docker-image of a [simple RTSP Server](https://hub.docker.com/r/bluenviron/mediamtx).
```bash
docker run --rm -it -e MTX_RTSPTRANSPORTS=tcp -e MTX_WEBRTCADDITIONALHOSTS=192.168.1.2 -p 8554:8554 -p 1935:1935 -p 8888:8888 -p 8889:8889 -p 8890:8890/udp -p 8189:8189/udp bluenviron/mediamtx-ffmpeg
```

- Install ffmpeg if not allready installed.

- Once the RTSP server is up and running, in a new shell window publish the sample video file as an RTSP feed in indefinite loop.
```bash
ffmpeg -re -stream_loop -1 -i <path_to_sample_video_mp4> -c:v libx264 -b:v 1500k -maxrate 1500k -bufsize 2M -c:a aac -b:a 128k -f rtsp -rtsp_transport tcp -muxdelay 0.1 -muxpreload 0.5 rtsp://localhost:8554/mystream
```

- Once the RTSP stream is up, confirm it in VLC by opening a network. using `rtsp://localhost:8554/mystream` as network url.

- Get an API KEY from Roboflow. Its free. Follow [this guide](https://docs.roboflow.com/api-reference/authentication#retrieve-an-api-key) to acquire your `API KEY`.

- For info. [this](https://universe.roboflow.com/roboflow-universe-projects/elephant-detection-cxnt1) is the dataset on which the model is trained on for inferences. Model ID: `elephant-detection-cxnt1/4`


- Install python3

- Setup python environment
```bash
python3 -m venv venv
source venv/bin/activate
```

- Install required dependencies
```bash
pip install -r requirements.txt
```

- Run detections python script.
```bash
python elephant_detection_example.py --rtsp_url 'rtsp://localhost:8554/mystream' --roboflow_api_key <roboflow_api_key>
```

NOTE:
  There will be some UserWarnings. For now, don't pay any attention to those.

## 🛠️ script arguments
- `--rtsp_url`: Complete RTSP URL for the video stream.

- `--model_id`: Designates the Roboflow model ID to be used. The default value is `"elephant-detection-cxnt1/4"`.

- `--confidence_threshold` (optional) : Confidence level for detections (`0` to `1`). Default is `0.7`.

- `--iou_threshold` (optional) : IOU threshold for non-max suppression. Default is `0.7`.

- `--roboflow_api_key` (optional): The API key for Roboflow services. Follow [this guide](https://docs.roboflow.com/api-reference/authentication#retrieve-an-api-key) to acquire your `API KEY`.

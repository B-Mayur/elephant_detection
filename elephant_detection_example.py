import argparse
from inference import InferencePipeline
from inference.core.interfaces.stream.sinks import render_boxes

# Custom handler
def custom_handler(image, prediction):
    render_boxes(image, prediction)
    # Add your extra functionality here

def main(
    rtsp_url: str,
    model_id: str,
    confidence: float,
    iou: float,
    api_key: str,
) -> None:  
    pipeline = InferencePipeline.init(
        model_id=model_id,
        video_reference=rtsp_url,
        on_prediction=custom_handler,
        api_key=api_key,
        confidence=confidence,
        iou_threshold=iou,
    )

    pipeline.start()
    try:
        pipeline.join()
    except KeyboardInterrupt:
        pipeline.terminate()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Detecting elephants in RTSP stream using ROBOFLOW's pretrained model."
    )
    parser.add_argument(
        "--rtsp_url",
        type=str,
        required=True,
        help="Complete RTSP URL for the video stream.",
    )
    parser.add_argument(
        "--model_id", type=str, default="elephant-detection-cxnt1/4", help="Roboflow model ID."
    )
    parser.add_argument(
        "--confidence_threshold",
        type=float,
        default=0.7,
        help="Confidence level for detections (0 to 1). Default is 0.7",
    )
    parser.add_argument(
        "--iou_threshold",
        default=0.7,
        type=float,
        help="IOU threshold for non-max suppression. Default is 0.7.",
    )
    parser.add_argument(
        "--roboflow_api_key",
        default=None,
        help="Roboflow API key",
        type=str,
    )
    args = parser.parse_args()

    main(
        rtsp_url=args.rtsp_url,
        model_id=args.model_id,
        confidence=args.confidence_threshold,
        iou=args.iou_threshold,
        api_key=args.roboflow_api_key
    )
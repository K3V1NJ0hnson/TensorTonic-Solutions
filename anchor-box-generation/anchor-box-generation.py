import numpy as np

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    anchors = []
    stride = image_size / feature_size

    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + .5) * stride
            cy = (i + .5) * stride

            for s in scales:
                for r in aspect_ratios:
                    w = s * math.sqrt(r)
                    h = s / math.sqrt(r)

                    box = [cx - w/2, cy - h/2, cx + w/2, cy + h/2]
                    anchors.append(box)

    return anchors
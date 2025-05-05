import torch
import os
import io
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import patchcore.patchcore
import patchcore.common
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image
import torchvision.transforms as transforms
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PySide6.QtGui import QImage, QPixmap

def detectDefects(image_path, 
                  model_path, 
                  models = "models",
                 ):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    patchcore_model = patchcore.patchcore.PatchCore(device)
    
    faiss_on_gpu = torch.cuda.is_available()
    faiss_num_workers = 8  
    nn_method = patchcore.common.FaissNN(faiss_on_gpu, faiss_num_workers)

    # load model
    patchcore_model.load_from_path(load_path=os.path.join(models, model_path), device=device, nn_method=nn_method)

    
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((224, 224)), 
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    input_tensor = transform(image).unsqueeze(0) 

    patchcore_model.eval()

    # detect defects
    with torch.no_grad():
        scores, segmentations = patchcore_model.predict(input_tensor)
    
    return segmentations, image

def drawDefects(segmentations, image, threshold=0.8):
    norm_mask = (segmentations - np.min(segmentations)) / np.ptp(segmentations)
    if norm_mask.ndim == 3:
        norm_mask = np.squeeze(norm_mask, axis=0)
    
    bin_mask = (norm_mask > threshold).astype(np.uint8)
    width, height = image.size
    heatmap = np.ma.masked_equal(norm_mask * bin_mask, 0)
    
    mask_resized = cv2.resize(bin_mask, (width, height), interpolation=cv2.INTER_NEAREST)
    heatmap = cv2.resize(heatmap, (width, height), interpolation=cv2.INTER_NEAREST)
    
    contours, _ = cv2.findContours(mask_resized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # plot heatmap
    tol = 1e-3
    rgba_heatmap = cm.jet(heatmap)
    rgba_heatmap[heatmap <= tol, 3] = 0
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.imshow(image, alpha=1)
    plt.imshow(rgba_heatmap, cmap='jet', alpha=0.3)
    
    ax = plt.gca()
    
    for c in contours:
        epsilon = 1e-10 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True).reshape(-1, 2)
        polygon = plt.Polygon(approx, fill=None, edgecolor='red', linewidth=2)
        ax.add_patch(polygon)
    
    ax.axis('off')
    buf = io.BytesIO()
    
    # save the figure to the buffer as a PNG image
    fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    plt.close(fig)
    
    # load the image data into a QImage, then convert to QPixmap
    qimage = QImage()
    qimage.loadFromData(buf.getvalue())
    qpixmap = QPixmap.fromImage(qimage)

    return qpixmap
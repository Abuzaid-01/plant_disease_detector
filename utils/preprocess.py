"""
Image preprocessing functions for plant disease detection
"""

from torchvision import transforms
from PIL import Image


def preprocess_image(uploaded_file):
    """
    Preprocess uploaded image for model prediction
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        torch.Tensor: Preprocessed image tensor
    """
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                           std=[0.229, 0.224, 0.225])
    ])
    
    image = Image.open(uploaded_file).convert("RGB")
    image_tensor = transform(image)
    return image_tensor

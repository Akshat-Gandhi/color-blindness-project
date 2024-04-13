import numpy as np
import cv2
from PIL import Image


class Transforms1:
    """
    Holds transformation matrices.
    """

    @staticmethod
    def rgb_to_lms():
        """
        Matrix for RGB color-space to LMS color-space transformation.
        """
        return np.array([[17.8824   , 43.5161 , 4.11935],
                         [ 3.45565  , 27.1554 , 3.86714],
                         [ 0.0299566, 0.184309, 1.46709]]).T

    @staticmethod
    def lms_to_rgb() -> np.ndarray:
        """
        Matrix for LMS colorspace to RGB colorspace transformation.
        """
        return np.array([[ 0.0809, -0.1305,  0.1167],
                         [-0.0102,  0.0540, -0.1136],
                         [-0.0004, -0.0041,  0.6935]]).T

    @staticmethod
    def lms_protanopia_sim(degree: float = 1.0) -> np.ndarray:
    
     return np.array([[0.5, 1.0, -1.5],
                        [0, 1, 0],
                        [0, 0, 1]]).T

    '''Protanopia Simulation Matrix:

Protanopia is a type of color blindness where the red cones in the retina are missing or defective. To simulate this deficiency, we need to reduce the sensitivity to red light. The transformation matrix is designed to reduce the contribution of red to the LMS (Luminance, Medium, Short) color space.
Mathematically, the transformation matrix is constructed to set the red component of the input to zero and adjust the green and blue components accordingly.
Here's the breakdown:
Red component: 0 * Red + 2.02344 * Green - 2.52581 * Blue
Green component: 0 * Red + 1 * Green + 0 * Blue
Blue component: 0 * Red + 0 * Green + 1 * Blue
This results in a reduction of the red contribution and a shift in the color balance towards green and blue.
 @staticmethod
    def lms_protanopia_sim(degree: float = 1.0) -> np.ndarray:
    
     return np.array([[0.2, 2.02344, -2.52581],
                        [0, 1, 0],
                        [0, 0, 1]]).T'''
    

    @staticmethod
    def correction_matrix() -> np.ndarray:
        """
        Matrix for Correcting Colorblindness (protanomaly) from LMS color-space.
        """
        
        return np.array([[1   , 0  , 0   ],
                         [0.5 , 0.5, 0   ],
                         [0.25, 0  , 0.75]]).T


class Utils1:
    """
    Couple of utils for loading the images.
    """
    @staticmethod
    def load_rgb(image):
        # img_rgb = np.array(Image.open(path)) / 255
        image = image / 255
        return image

    @staticmethod
    def load_lms(image):
        # img_rgb = np.array(Image.open(path)) / 255
        image = image / 255
        img_lms = np.dot(image[:,:,:3], Transforms1.rgb_to_lms())

        return img_lms

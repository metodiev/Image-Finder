# image_finder/finder.py

import os
from typing import List

class ImageFinder:
    """
    Recursively searches for image files in a directory.
    """

    SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.heic')

    def __init__(self, root_dir: str):
        self.root_dir = root_dir

    def find_images(self) -> List[str]:
        """
        Recursively find all image files in the directory.
        Returns a list of full file paths.
        """
        image_paths = []
        for dirpath, _, filenames in os.walk(self.root_dir):
            for file in filenames:
                if file.lower().endswith(self.SUPPORTED_FORMATS):
                    full_path = os.path.join(dirpath, file)
                    image_paths.append(full_path)

        return image_paths

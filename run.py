# run.py

from image_finder.finder import ImageFinder
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py <path_to_search>")
        return

    search_path = sys.argv[1]

    if not os.path.isdir(search_path):
        print(f"The path '{search_path}' is not a valid directory.")
        return

    finder = ImageFinder(search_path)
    images = finder.find_images()

    if not images:
        print("No image files found.")
    else:
        print(f"\nFound {len(images)} image(s):\n")
        for img in images:
            print(f"{img}")

if __name__ == "__main__":
    main()

# Square Counter

Square Counter can detect closed shapes (e.g. a square) in multiple images and count the number of them. The number of shapes in each image will be recorded

## Requirement
Square Counter requires the following libraries.

- OpenCV-Python
- Pandas
- OpenPyXL

## Notice
Square Counter relies on OpenCV findContours function. You can change parameters (e.g. cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) if it fails to detect shapes.

Since I chose cv2.RETR_LIST, I removed the very last element of 'contours' as it indicates the outer edge of whole image. If you change this setting, you have to change line 19 too.
```python
contours = contours[:-1]
```

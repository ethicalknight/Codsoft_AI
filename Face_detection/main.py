import cv2
import face_recognition

# Load a reference image and encode the face
reference_image = face_recognition.load_image_file("person1.jpg")  # Put the path to your reference face image here
reference_encoding = face_recognition.face_encodings(reference_image)[0]

# Load the image (or use cv2.VideoCapture for real-time)
image = cv2.imread("test.jpg")  # Path to input image with faces

# Convert image from BGR (OpenCV) to RGB (face_recognition)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Detect faces and get encodings
face_locations = face_recognition.face_locations(rgb_image)
face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Compare this face to the reference
    matches = face_recognition.compare_faces([reference_encoding], face_encoding)
    name = "Unknown"
    if matches[0]:
        name = "Person 1"

    # Draw a rectangle around the face
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    # Label the face
    cv2.putText(image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

cv2.imshow("Face Detection & Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
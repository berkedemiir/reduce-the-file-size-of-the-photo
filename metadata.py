import cv2
import piexif

def read_metadata(image_path):
    # Read the metadata informations.
    exif_data = piexif.load(image_path)
    print("Metadata informations of the photos:")
    print(exif_data)

    return exif_data

def remove_unnecessary_metadata(exif_data):
    # Storing only 'Exif', 'GPS' and 'Interop' metadata as an example
    keep_tags = {
        'Exif': exif_data.get('Exif', {}),
        'GPS': exif_data.get('GPS', {}),
        'Interop': exif_data.get('Interop', {}),
    }

    # Create a new exif data with the remaining base metadata
    exif_data.clear()
    exif_data.update(keep_tags)

    return exif_data

if __name__ == "__main__":
    input_image_path = "peribacalari.jpg"
    output_image_path = "peribacalari_no_unnecessary_metadata.jpg"

    # Read the metadata of the original photo
    exif_info = read_metadata(input_image_path)

    if exif_info:
        # Remove unnecessary metadata information and save new photo
        new_exif_info = remove_unnecessary_metadata(exif_info)
        img = cv2.imread(input_image_path)
        # Reduce the file size by lowering the JPEG quality
        cv2.imwrite(output_image_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

        # Add metadata information of original photo to new photo
        piexif.insert(piexif.dump(new_exif_info), output_image_path)
        
        print("Photo saved with unnecessary metadata removed and file size reduced:", output_image_path)
    else:
        print("Photo processing error.")






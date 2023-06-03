from PIL import Image, ImageFilter


def apply_grayscale(image):
    return image.convert("L")


def apply_blur(image):
    return image.filter(ImageFilter.BLUR)


def apply_sharpen(image):
    return image.filter(ImageFilter.SHARPEN)


def apply_artistic_effect(image):
    return image.filter(ImageFilter.CONTOUR)


def main():
    # Prompt user for image path
    image_path = input("Enter the path to the image file: ")
    original_image = Image.open(image_path)

    while True:
        print("\nAvailable Filters:")
        print("1. Grayscale")
        print("2. Blur")
        print("3. Sharpen")
        print("4. Artistic Effect")
        print("5. Quit")

        # Prompt user for filter choice
        choice = input("Enter the filter number (1-4) or 5 to quit: ")

        if choice == '1':
            modified_image = apply_grayscale(original_image)
        elif choice == '2':
            modified_image = apply_blur(original_image)
        elif choice == '3':
            modified_image = apply_sharpen(original_image)
        elif choice == '4':
            modified_image = apply_artistic_effect(original_image)
        elif choice == '5':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        # Prompt user for output path
        output_path = input("Enter the path to save the modified image: ")
        modified_image.save(output_path)
        print("Modified image saved successfully.")


if __name__ == "__main__":
    main()

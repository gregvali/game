import cv2
import numpy as np
from PIL import Image
import argparse
import os

def is_green_pixel(pixel, tolerance=30, min_green=80, max_brightness=300):
    """
    Check if a pixel is predominantly green (but not white/bright).
    
    Args:
        pixel: RGB or BGR pixel values
        tolerance: How much the green channel must exceed red/blue
        min_green: Minimum green value to consider
        max_brightness: Maximum total brightness to avoid white pixels
    
    Returns:
        bool: True if pixel is considered green
    """
    if len(pixel) >= 3:
        # Convert to int to avoid overflow warnings
        b, g, r = int(pixel[0]), int(pixel[1]), int(pixel[2])
        
        # Calculate total brightness to exclude white/bright pixels
        brightness = r + g + b
        
        # Must be green dominant, above minimum green, and not too bright (to exclude white)
        is_green_dominant = (g > r + tolerance) and (g > b + tolerance)
        is_green_enough = g > min_green
        is_not_too_bright = brightness < max_brightness
        
        # Additional check: green should be significantly higher than average of red and blue
        avg_rb = (r + b) / 2
        is_significantly_green = g > avg_rb + tolerance
        
        return is_green_dominant and is_green_enough and is_not_too_bright and is_significantly_green
    return False

def green_to_transparent(input_path, output_path=None, tolerance=30, min_green=80, max_brightness=300, preview=False):
    """
    Convert green pixels to transparent in an image.
    
    Args:
        input_path: Path to input image
        output_path: Path to save result (must be PNG for transparency)
        tolerance: Green detection tolerance (how much green must exceed other colors)
        min_green: Minimum green value to consider (0-255)
        max_brightness: Maximum total RGB brightness to avoid white pixels (0-765)
        preview: Show before/after comparison
    
    Returns:
        numpy.ndarray: Image with green pixels made transparent
    """
    # Load image
    image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        raise ValueError(f"Could not load image from {input_path}")
    
    height, width = image.shape[:2]
    print(f"Processing image: {width}x{height}")
    
    # Convert to RGBA if not already
    if len(image.shape) == 3 and image.shape[2] == 3:  # BGR
        # Convert BGR to BGRA
        rgba_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    elif len(image.shape) == 3 and image.shape[2] == 4:  # Already BGRA
        rgba_image = image.copy()
    else:
        raise ValueError("Unsupported image format")
    
    # Count green pixels for reporting
    green_pixel_count = 0
    total_pixels = height * width
    
    # Process each pixel
    for y in range(height):
        for x in range(width):
            pixel = rgba_image[y, x]
            if is_green_pixel(pixel, tolerance, min_green, max_brightness):
                # Make pixel transparent
                rgba_image[y, x, 3] = 0  # Set alpha to 0 (transparent)
                green_pixel_count += 1
    
    print(f"Made {green_pixel_count:,} pixels transparent ({green_pixel_count/total_pixels*100:.1f}% of image)")
    
    # Save result
    if output_path:
        # Ensure output is PNG for transparency support
        name, ext = os.path.splitext(output_path)
        if ext.lower() != '.png':
            output_path = name + '.png'
            print(f"Changed output format to PNG for transparency support: {output_path}")
        
        # Convert BGRA to RGBA for saving with PIL (which handles transparency better)
        rgba_pil = cv2.cvtColor(rgba_image, cv2.COLOR_BGRA2RGBA)
        pil_image = Image.fromarray(rgba_pil)
        pil_image.save(output_path, 'PNG')
        print(f"Saved transparent image to: {output_path}")
    
    # Show preview if requested
    if preview:
        # Create a checkerboard background to show transparency
        checker_size = 20
        checker = np.zeros((height, width, 3), dtype=np.uint8)
        
        for y in range(0, height, checker_size):
            for x in range(0, width, checker_size):
                if ((y // checker_size) + (x // checker_size)) % 2 == 0:
                    checker[y:y+checker_size, x:x+checker_size] = [200, 200, 200]  # Light gray
                else:
                    checker[y:y+checker_size, x:x+checker_size] = [150, 150, 150]  # Dark gray
        
        # Composite the transparent image over the checkerboard
        alpha = rgba_image[:, :, 3] / 255.0
        preview_image = checker.copy()
        
        for c in range(3):
            preview_image[:, :, c] = (alpha * rgba_image[:, :, c] + 
                                    (1 - alpha) * preview_image[:, :, c])
        
        # Resize for display if too large
        max_height = 600
        if height > max_height:
            scale = max_height / height
            new_w = int(width * scale)
            
            original_display = cv2.resize(image, (new_w, max_height))
            preview_display = cv2.resize(preview_image.astype(np.uint8), (new_w, max_height))
        else:
            original_display = image
            preview_display = preview_image.astype(np.uint8)
        
        cv2.imshow('Original', original_display)
        cv2.imshow('Green to Transparent (on checkerboard)', preview_display)
        print("Press any key to close preview windows...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return rgba_image

def batch_process(input_folder, output_folder=None, tolerance=30, min_green=80, max_brightness=300):
    """
    Process multiple images in a folder.
    
    Args:
        input_folder: Folder containing input images
        output_folder: Folder to save processed images
        tolerance: Green detection tolerance
        min_green: Minimum green value
        max_brightness: Maximum brightness to avoid white pixels
    """
    if output_folder is None:
        output_folder = input_folder + "_transparent"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif')
    processed = 0
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_folder, filename)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(output_folder, name + '_transparent.png')
            
            try:
                print(f"\nProcessing: {filename}")
                green_to_transparent(input_path, output_path, tolerance, min_green, max_brightness)
                processed += 1
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    print(f"\nBatch processing complete. Processed {processed} images.")

def main():
    parser = argparse.ArgumentParser(description='Convert green pixels to transparent')
    parser.add_argument('input', help='Input image path or folder')
    parser.add_argument('-o', '--output', help='Output image path or folder')
    parser.add_argument('-t', '--tolerance', type=int, default=30, 
                       help='Green detection tolerance (0-100)')
    parser.add_argument('-m', '--min-green', type=int, default=80,
                       help='Minimum green value to consider (0-255)')
    parser.add_argument('--max-brightness', type=int, default=300,
                       help='Maximum total brightness to avoid white pixels (0-765)')
    parser.add_argument('-p', '--preview', action='store_true', 
                       help='Show before/after preview')
    parser.add_argument('-b', '--batch', action='store_true',
                       help='Process all images in a folder')
    
    args = parser.parse_args()
    
    try:
        if args.batch or os.path.isdir(args.input):
            # Batch processing
            batch_process(args.input, args.output, args.tolerance, args.min_green, args.max_brightness)
        else:
            # Single image processing
            if not args.output:
                name, ext = os.path.splitext(args.input)
                args.output = f"{name}_transparent.png"
            
            green_to_transparent(args.input, args.output, args.tolerance, 
                               args.min_green, args.max_brightness, args.preview)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage if run directly
    if len(os.sys.argv) == 1:
        print("Green to Transparent Converter")
        print("Usage: python green_transparent.py input_image.jpg [-o output.png] [options]")
        print("")
        print("Options:")
        print("  -o, --output      Output filename (default: input_transparent.png)")
        print("  -t, --tolerance   Green detection tolerance 0-100 (default: 30)")
        print("  -m, --min-green   Minimum green value 0-255 (default: 80)")
        print("  --max-brightness  Maximum total brightness 0-765 (default: 200)")
        print("  -p, --preview     Show before/after comparison")
        print("  -b, --batch       Process all images in folder")
        print("")
        print("Examples:")
        print("  python green_transparent.py photo.jpg -p")
        print("  python green_transparent.py photo.jpg -m 70 --max-brightness 180")
        print("  python green_transparent.py image_folder/ -b")
        print("")
        print("Note: Output will be PNG format to support transparency")
    else:
        main()
import os
from rembg import remove, new_session
from PIL import Image

# ✅ Force rembg to use CPU only
os.environ["ORT_DISABLE_GPU"] = "1"

def remove_background(input_path: str, output_path: str):
    # Load image
    with Image.open(input_path).convert("RGBA") as img:
        original_size = img.size

        # ✅ Use higher-quality model (u2net)
        session = new_session(model_name="u2net")

        # ✅ Remove background with session
        result = remove(img, session=session)

        # ✅ Ensure result image is RGBA and same size
        result = Image.frombytes("RGBA", original_size, result.tobytes())
        result.save(output_path, format='PNG')

        print(f"✅ Background removed and saved at: {output_path}")
        print(f"Original Size: {original_size}, Output Size: {result.size}")

if __name__ == "__main__":
    input_file = input("Enter the path to the image (jpg/png): ").strip('"')

    if not os.path.exists(input_file):
        print("❌ File does not exist.")
    elif os.path.isdir(input_file):
        print("❌ Path is a folder. Please enter a file path.")
    else:
        file_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"{file_name}_no_bg.png"
        remove_background(input_file, output_file)

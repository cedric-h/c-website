import os
import subprocess

def process_html_files(template_dir, root_dir, ext=".template.html"):
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            if file.endswith(ext):
                template_path = os.path.join(root, file)
                # Calculate the relative path from the template directory
                relative_path = os.path.relpath(template_path, template_dir)
                build_path = os.path.join(root_dir, "build", relative_path)
                
                # Create the necessary directories in the build path
                os.makedirs(os.path.dirname(build_path), exist_ok=True)
                
                output_path = build_path.replace(ext, ".html")
                
                # Apply the cpp command
                command = f"cpp -P {template_path} {output_path}"
                subprocess.run(command, shell=True, check=True)
                print(f"Processed: {template_path} -> {output_path}")

if __name__ == "__main__":
    ROOT_DIRECTORY = "."  # Root of your project
    TEMPLATE_DIR = "templates"  # Replace with the path to your template directory
    TEMPLATE_EXT = ".template.html"
    process_html_files(TEMPLATE_DIR, ROOT_DIRECTORY, TEMPLATE_EXT)

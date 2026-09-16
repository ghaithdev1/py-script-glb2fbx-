import os
import subprocess
import sys

def find_blender_path():
    common_paths = [
        r"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.1\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.0\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 5.0\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 3.3\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 3.5\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 3.0\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 3.1\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.3\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 4.2\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 4.1\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 5.1\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 4.0\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 3.6\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 5.0\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 5.2\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 3.3\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 3.4\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 3.5\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 3.0\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 3.1\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 4.3\blender.exe",
        r"D:\Program Files\Blender Foundation\Blender 4.5\blender.exe",
    ]
    for path in common_paths:
        if os.path.exists(path):
            return path
    return "blender"

def get_current_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def main():
    blender_path = find_blender_path()
    target_dir = get_current_dir()
    
    glb_files = [f for f in os.listdir(target_dir) if f.lower().endswith('.glb')]
    
    if not glb_files:
        print("No .glb files found in this folder.")
        input("Press Enter to exit...")
        return

    print(f"Found {len(glb_files)} .glb file(s). Processing...")

    for glb in glb_files:
        glb_path = os.path.join(target_dir, glb)
        fbx_path = os.path.splitext(glb_path)[0] + ".fbx"
        
        # Fix path escape issues by converting backslashes to forward slashes for Blender
        safe_glb_path = glb_path.replace("\\", "/")
        safe_fbx_path = fbx_path.replace("\\", "/")
        
        blend_script = f"""
import bpy

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath={repr(safe_glb_path)})

objects_to_remove = [obj for obj in bpy.data.objects if obj.name in {'Cube', 'Camera', 'Light'}]

bpy.ops.object.select_all(action='DESELECT')
for obj in objects_to_remove:
    obj.select_set(True)
bpy.ops.object.delete()

bpy.ops.export_scene.fbx(filepath={repr(safe_fbx_path)})
"""
        
        script_path = os.path.join(target_dir, "_temp_convert.py")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(blend_script)
        
        cmd = [blender_path, "--background", "--python", script_path]
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(f"Successfully converted: {glb} -> {os.path.basename(fbx_path)}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {glb}. Blender Error:")
            print(e.stderr)
        except Exception as e:
            print(f"Unexpected error on {glb}: {e}")
        finally:
            if os.path.exists(script_path):
                os.remove(script_path)

    print("\nAll tasks completed.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

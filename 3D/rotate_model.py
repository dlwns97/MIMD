import open3d as o3d
import numpy as np
import argparse
import os

# Create directory if not exists #
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def main():


   parser = argparse.ArgumentParser(description='Capture and save images using an 3D model.')
   parser.add_argument('--output_path', type=str, default="C:/Users/user/Desktop/Workspace/231023_objply/output/", help='Directory path to save captured images.')
   parser.add_argument('--model_path', type=str, default="C:/Users/user/Desktop/Workspace/231023_objply/garuda-and-vishnu-ply/Garuda and Vishnu.ply", help='Path to the 3D model file.')
   # parser.add_argument('--model_path', type=str, default="C:/Users/user/Desktop/Workspace/231023_objply/Potato/Potato.obj", help='Path to the 3D model file.')
   parser.add_argument('--rotation_angle', nargs='+', type=float, default=30.0, help='Desired rotation angle')

   args = parser.parse_args()

   # Check directory path #
   create_directory(args.output_path)

   # Get 3D model name #
   file_name = os.path.basename(args.model_path)
   file_name, ext = os.path.splitext(file_name)
   file_name = os.path.join("output", file_name)


   # Load 3D model #
   mesh = o3d.io.read_triangle_mesh(args.model_path)
   mesh.rotate(mesh.get_rotation_matrix_from_xyz((np.pi,0,0)),
                center=(0, 0, 0))

   # Set camera to capture image #
   viewer = o3d.visualization.Visualizer()
   viewer.create_window()
   viewer.create_window(width=800, height=600)
   ctr = viewer.get_view_control()
   viewer.add_geometry(mesh)

   # Capture initial scene #
   initial_name = os.path.join("","initial.png")
   viewer.poll_events()
   viewer.update_renderer()
   viewer.capture_screen_image(initial_name)


   # Rotate 3D model #
   rotation_angle = args.rotation_angle
   ctr.rotate(rotation_angle,0.0)
   viewer.poll_events()
   viewer.update_renderer()
   rotated_name = os.path.join("",f"rotated{rotation_angle}.png")
   viewer.capture_screen_image(rotated_name)

if __name__=="__main__":
    main()



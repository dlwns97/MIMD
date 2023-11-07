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
    parser.add_argument('--output_path', type=str, default="../output/",
                        help='Directory path to save captured images.')

    parser.add_argument('--model_path', type=str,
                        default="../small-mango-2/source/smg/smg.obj",
                        help='Path to the 3D model file.')
    texture_path = "../small-mango-2/source/smg/smg.jpg"
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
    mesh2 =  o3d.io.read_triangle_mesh(args.model_path)

    # Texture Image
    texture_image = o3d.io.read_image(texture_path)
    mesh.textures = [texture_image]
    mesh2.textures = [texture_image]


    # Set camera to capture image #
    viewer = o3d.visualization.Visualizer()
    viewer2 = o3d.visualization.Visualizer()
    viewer.create_window()
    viewer.create_window(width=800, height=600)
    ctr = viewer.get_view_control()
    viewer.add_geometry(mesh)



    # Capture initial scene #
    initial_name = os.path.join("", "initial.png")
    viewer.poll_events()
    viewer.update_renderer()
    viewer.capture_screen_image(initial_name)
    viewer.run()

    # Create Rotated 3D Model
    rotation_angle = args.rotation_angle
    mesh2.rotate(mesh.get_rotation_matrix_from_xyz((rotation_angle, 0, 0)),
                center=(0, 0, 0))

    viewer2.create_window()
    viewer2.create_window(width=800, height=600)
    ctr2 = viewer2.get_view_control()
    viewer2.add_geometry(mesh2)


    # Rotate 3D model #
    viewer2.poll_events()
    viewer2.update_renderer()
    rotated_name = os.path.join("", f"rotated{rotation_angle}.png")
    viewer2.capture_screen_image(rotated_name)
    viewer2.run()



if __name__ == "__main__":
    main()


# THIS CODE IS DEPRECATED. DO NOT EDIT. ~231023 17:50
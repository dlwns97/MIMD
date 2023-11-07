import open3d as o3d
import numpy as np
import argparse
import os
import cv2


# Create directory if not exists #
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def main():
    parser = argparse.ArgumentParser(description='Capture and save images using an 3D model.')
    parser.add_argument('--output_path', type=str, default="../output/",
                        help='Directory path to save captured images.')
    # data_root = "../"+ "small-mango-2/source/smg" + "/"   # mango
    # data_root = "../"+ "strawberry/source/a4967ef33ac64dd89d3e9ec2fb8baf66" + "/" # strawberry
    # data_root = "../"+ "purple-onion/source/dyc" + "/"    # onion
    # data_root = "../"+ "kiwi-scan/source/kiwi" + "/"  # kiwi - 얘는 meshlab에서도 안됨 + 사각메쉬
    # data_root = "../"+ "banana/source/ripe-banana" + "/"   # ripe-bababa    # tif 안됨
    # data_root = "../"+ "Potato/source/potato" + "/"   # potato
    # data_root = "../"+ "oriental-melon/source/baked_mesh" + "/"   # oriental_melon
    data_root = "../"+ "avocado/source/test" + "/"   # avocado

    # texture_path = data_root + "ripe-banana.jpg" # (Legacy code ~231106)
    model_path = data_root + "model_Avocado_20210206_170204399.obj"
    parser.add_argument('--model_path', type=str,
                        default=model_path,
                        help='Path to the 3D model file.')
    parser.add_argument('--rotation_angle', nargs='+', type=float, default=30.0, help='Desired rotation angle')

    args = parser.parse_args()

    # Check directory path #
    create_directory(args.output_path)

    # Get 3D model name #
    file_name = os.path.basename(args.model_path)
    file_name, ext = os.path.splitext(file_name)
    file_name = os.path.join("output", file_name)

    # Load 3D model
    mesh = o3d.io.read_triangle_mesh(args.model_path, True)
    mesh2 = o3d.io.read_triangle_mesh(args.model_path, True)

    # #   Load 3D model (Legacy code ~231106)
    # mesh = o3d.io.read_triangle_mesh(args.model_path)
    # mesh2 =  o3d.io.read_triangle_mesh(args.model_path)
    #
    # # # Texture Image (Legacy code ~231106)      # read_triangle_mesh에 True인수를 주면 필요 없음
    # texture_image = o3d.io.read_image(texture_path)
    # mesh.textures = [texture_image]
    # mesh2.textures = [texture_image]

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


import seaborn as sns
import numpy as np
import open3d as o3d

'''
Author: Rahul Sajnani
Date: 16th September 2021
'''


def create_color_samples(N):
    '''
    Creates N distinct colors
    N x 3 output
    '''

    palette = sns.color_palette(None, N)
    palette = np.array(palette)

    return palette


def visualize_pointclouds(pcd_list, frame_1 = None, frame_2 = None):
    '''
    Visualize the list of point clouds in Open3D
    '''
    pallete = create_color_samples(len(pcd_list))
    pcd_object_list = []

    for pcd_num in range(len(pcd_list)):

        points = pcd_list[pcd_num]
        # print(points.shape)
        colors = np.ones(points.shape) * pallete[pcd_num, :][:, np.newaxis]
        pcd_cloud = o3d.geometry.PointCloud()
        pcd_cloud.points = o3d.utility.Vector3dVector(points.T)
        pcd_cloud.colors = o3d.utility.Vector3dVector(colors.T)

        pcd_object_list.append(pcd_cloud)
    
    if frame_1 is not None:
        pcd_object_list.append(frame_1)
    
    if frame_2 is not None:
        pcd_object_list.append(frame_2)
    
    o3d.visualization.draw_geometries(pcd_object_list)
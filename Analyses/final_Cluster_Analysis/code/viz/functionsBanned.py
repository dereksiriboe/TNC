import numpy as np #linear algebra
import pandas as pd #data manipulation and analysis
import matplotlib.pyplot as plt #data visualization
import seaborn as sns #data visualization
import sklearn.preprocessing as skp #machine learning (preprocessing)
import sklearn.cluster as skc #machine learning (clustering)
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.path as mpath
from adjustText import adjust_text
import warnings # ignore warnings
warnings.filterwarnings('ignore')


def filter_banned_counties(df):
    banned_dfs = []
    for i in range(df['cluster_id'].nunique()):
        cluster_banned = df.loc[(df['cluster_id'] == i) & (df['Banned or not'] == 1)]

        if len(cluster_banned) > 2:
            banned_dfs.append(cluster_banned)
            print(f"Cluster{i} had enough banned counties to find non-banned counties in the banned counties convex hull.")
            
    return banned_dfs if len(banned_dfs) > 0 else None



def get_banned_cluster_coords_dict(cluster_dfBanned, df):
    banned_cluster_coords_dict = {}
    for col1 in range(0, len(cluster_dfBanned.columns)-3):
        for col2 in range(col1+1, len(cluster_dfBanned.columns)-3):
            if col1 < col2:
                banned_cluster_coords_dict[cluster_dfBanned.columns[col1], cluster_dfBanned.columns[col2]] = cluster_dfBanned[[df.columns[col1], df.columns[col2]]].values.tolist()
                
    return banned_cluster_coords_dict



def bannedCoords(df_list, df):
    bannedCoords_list = []
    for i in range(len(df_list)):
        coords_dict =  get_banned_cluster_coords_dict(df_list[i], df)
        bannedCoords_list.append(coords_dict)
        
    return bannedCoords_list


def clusterk_dict_banned(clusterkBanned_df_list, bannedCoords_list):
    dic = {}
    for i in range(len(clusterkBanned_df_list)):
        dic[f"cluster{i}"] = bannedCoords_list[i]
    return dic


def cluster0Banned(clusterKBanned_dict):
    return clusterKBanned_dict[f"cluster{str(0)}"]

def cluster1Banned(clusterKBanned_dict):
    return clusterKBanned_dict[f"cluster{str(1)}"]

def cluster2Banned(clusterKBanned_dict):
    return clusterKBanned_dict[f"cluster{str(2)}"]




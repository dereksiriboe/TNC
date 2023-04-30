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


def split_dataframe_by_cluster(df, cluster_column):
    """
    Splits a data frame into multiple data frames based on a categorical column.

    Parameters:
        df (pandas.DataFrame): The data frame to split.
        cluster_column (str): The name of the cluster column to split on.

    Returns:
        dict: A dictionary of data frames, where each key is a unique value in the
        categorical column, and the corresponding value is a data frame with only
        the rows that have that categorical value.
    """
    # get a list of unique categorical values
    categories = df[cluster_column].unique()

    # create a list of data frames
    df_list = []
    for cat in categories:
        sub_df = df[df[cluster_column] == cat]
        df_list.append(sub_df)

    return df_list


def get_cluster_coords_dict(cluster_df, df):
    cluster_coords_dict = {}
    for col1 in range(0, len(cluster_df.columns)-3):
        for col2 in range(col1+1, len(cluster_df.columns)-3):
            if col1 < col2:
                cluster_coords_dict[cluster_df.columns[col1], cluster_df.columns[col2]] = cluster_df[[df.columns[col1],
                                                                                                      df.columns[col2]]].values.tolist()
    return cluster_coords_dict



def coords(df_list, df):
    coords_list = []
    for i in range(len(df_list)):
        coords_dict =  get_cluster_coords_dict(df_list[i], df)
        coords_list.append(coords_dict)
        
    return coords_list


# coords_list = coords(df_list, housingCluster)

# split the data frame by category
def clusterk_dict(clusterk_df_list, coords_list):
    dic = {}
    for i in range(len(clusterk_df_list)):
        dic[f"cluster{i}"] = coords_list[i]
    return dic


# clusterK_dict = clusterk_dict(df_list, coords_list)

def cluster0(clusterK_dict):
    return clusterK_dict[f"cluster{str(0)}"]

def cluster1(clusterK_dict):
    return clusterK_dict[f"cluster{str(1)}"]

def cluster2(clusterK_dict):
    return clusterK_dict[f"cluster{str(2)}"]




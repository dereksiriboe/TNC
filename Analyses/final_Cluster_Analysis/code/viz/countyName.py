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

    

def banned_counties_list(df):
    bannedCountiesList = []
    bannedCounties = df.loc[df['Banned or not'] == 1]
    bannedCounties = bannedCounties['County Name'].tolist()
    for i in range(len(bannedCounties)):
        bannedCountiesList.append(bannedCounties[i][:-13])
    return bannedCountiesList




def countyNames_cluster0(df, clusterk_dict, clusterk_banned_dict, bannedCountiesList):
    path0BannedDict = {}
    for i in clusterk_dict:
        hull0Banned = ConvexHull(clusterk_banned_dict[i])
        path0BannedDict[i] = mpath.Path(np.array(clusterk_banned_dict[i])[hull0Banned.vertices])
        
        
    countyNameDict0={}

    for key, nested_list in clusterk_dict.items():
        countyNameL = []
        value2 = path0BannedDict[key]
        for sublist in nested_list:
            if value2.contains_point(sublist):
                countyName = df.loc[(df[key[0]] == sublist[0]) & (df[key[1]] == sublist[1]), 'County Name']
                if len(countyName) > 0:
                    countyNameL.append(countyName.values[0][:-13])
                    countyNameDict0[key[0], key[1]] = countyNameL
                        
                        
    for key, value in countyNameDict0.items():
        countyNameDict0[key] = [county for county in value if county not in bannedCountiesList]

    return countyNameDict0


def countyNames_cluster1(df, clusterk_dict, clusterk_banned_dict, bannedCountiesList):
    
    path1Banned = {}
    for i in clusterk_dict:
        hull1Banned = ConvexHull(clusterk_banned_dict[i])
        path1Banned[i] = mpath.Path(np.array(clusterk_banned_dict[i])[hull1Banned.vertices])
        
        
    countyNameDict1={}

    for key, nested_list in clusterk_dict.items():
        countyNameL = []
        value2 = path1Banned[key]
        for sublist in nested_list:
            if value2.contains_point(sublist):
                countyName = df.loc[(df[key[0]] == sublist[0]) & (df[key[1]] == sublist[1]), 'County Name']
                if len(countyName) > 0:
                    countyNameL.append(countyName.values[0][:-13])
                    countyNameDict1[key[0], key[1]] = countyNameL
                        
                        
    for key, value in countyNameDict1.items():
        countyNameDict1[key] = [county for county in value if county not in bannedCountiesList]

    return countyNameDict1
                


def countyNames_cluster2(df, clusterk_dict, clusterk_banned_dict, bannedCountiesList):
    
    path2Banned = {}
    for i in clusterk_dict:
        hull2Banned = ConvexHull(clusterk_banned_dict[i])
        path2Banned[i] = mpath.Path(np.array(clusterk_banned_dict[i])[hull2Banned.vertices])
        
        
    countyNameDict2={}

    for key, nested_list in clusterk_dict.items():
        countyNameL = []
        value2 = path2Banned[key]
        for sublist in nested_list:
            if value2.contains_point(sublist):
                countyName = df.loc[(df[key[0]] == sublist[0]) & (df[key[1]] == sublist[1]), 'County Name']
                if len(countyName) > 0:
                    countyNameL.append(countyName.values[0][:-13])
                    countyNameDict2[key[0], key[1]] = countyNameL
                        
                        
    for key, value in countyNameDict2.items():
        countyNameDict2[key] = [county for county in value if county not in bannedCountiesList]

    return countyNameDict2

        
    

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            if isinstance(merged_dict[key], list) and isinstance(value, list):
                merged_dict[key].extend(value)
            else:
                merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value
    return merged_dict


    

    

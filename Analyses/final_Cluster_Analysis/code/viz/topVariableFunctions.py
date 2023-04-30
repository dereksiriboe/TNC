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




def filtered_var_pairs(allCounties):
    filtered_pairs = []

    # Loop through each key-value pair in the dictionary
    for key, value in allCounties.items():
        category, subcategory = key

        # Otherwise, add the key-value pair to the filtered list
        filtered_pairs.append({'Category':category, 'Subcategory':subcategory, 'List of Counties':value})
        
    return filtered_pairs


def categoryCountyList(filtered_pairs):    
    max_counties = 0
    max_category = ''

    for pair in filtered_pairs:
        if len(pair['List of Counties']) > max_counties:
            max_counties = len(pair['List of Counties'])
            max_category = pair['Category']

    print(f"The category with the most counties is '{max_category}' with {max_counties} counties.")

    category_CountyLists = {}
    for pair in filtered_pairs:
        if pair['Category'] in category_CountyLists:
            if len(pair['List of Counties']) > max_counties:
                category_CountyLists[pair['Category']] += pair['List of Counties']
        else:
            category_CountyLists[pair['Category']] = pair['List of Counties']
    sorted_category_counts = sorted(category_CountyLists.items(), key=lambda x: x[1], reverse=True)

    return category_CountyLists





def subcategoryCountyList(filtered_pairs):    

    max_counties = 0
    max_subcategory = ''

    for pair in filtered_pairs:
        if len(pair['List of Counties']) > max_counties:
            max_counties = len(pair['List of Counties'])
            max_subcategory = pair['Subcategory']

    print(f"The subcategory with the most counties is '{max_subcategory}' with {max_counties} counties.")

    subcategory_CountyList = {}
    for pair in filtered_pairs:
        if len(pair['List of Counties']) > max_counties:
            if pair['Subcategory'] in subcategory_CountyList:
                subcategory_CountyList[pair['Subcategory']] += pair['List of Counties']
        else:
            subcategory_CountyList[pair['Subcategory']] = pair['List of Counties']
    sorted_subcategory_counts = sorted(subcategory_CountyList.items(), key=lambda x: x[1], reverse=True)


    return subcategory_CountyList




def commonKeys(Dict1, Dict2):
    # Find keys in Dict1 and Dict2
    common_keys = set(Dict1.keys()) & set(Dict2.keys())

    # Create a new dictionary with the combined keys and their values. 
    common_dict = {}
    for key in common_keys:
        common_dict[key] = list(set(Dict1[key] + Dict2[key]))
    return common_dict




def freq_var(ranked_list):
    var_freq = []

    for item in ranked_list:
        var_name = item[1]
        counties = item[3]
        for county in counties:
            county_found = False
            for i in range(len(var_freq)):
                if var_freq[i][0] == county:
                    var_freq[i][1].append(var_name)
                    county_found = True
                    break
            if not county_found:
                var_freq.append((county, [var_name]))
                
    return var_freq













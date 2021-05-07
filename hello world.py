import csv
import plotly.figure_factory as ff
import pandas as pd
from plotly.offline import iplot


def remove_char(jobs, punc):
    for job_1 in jobs:
        for ele in job_1[-1]:
            job_1[-1]=job_1[-1].replace("\n"," ")
            if(ele in punc):
                job_1[-1] = job_1[-1].replace(ele," ")
    return jobs




def convert_to_list(x):
    stop_words = ["i", "a", "an", "the" "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    x[-1] = x[-1].split(" ")
    y = x[-1]
    x[-1] = []
    for z in y:
        if ((z.lower() != "") and (z.lower() not in stop_words)):
            x[-1].append(z)
    return x[-1]


def dict_words(jobs):
    words = {}
    for job in jobs:
        for ele in job[-1]:
            ele = ele.lower()
            if(ele in words.keys()):
                words[ele]+=1
            else:
                words[ele]=1
    return words



def plot():
##    scope = ['New York']
##    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv")
##    df_new = df[df['STNAME'].isin(scope)]
##    values = df_new['TOT_POP'].tolist()
##    fips = df_new['FIPS'].tolist()
##    colorscale = ["#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3","#2daa4b","#80b1d3"]
    fig = ff.create_choropleth() #fips=fips, values=values, scope=scope, colorscale=colorscale, round_legend_values=True,simplify_county=0, simplify_state=0,county_outline={'color':'rgb(15,15,55)','width':0.5},legend_title='Population per county',title='New York')
    iplot(fig,filename='Chloropleth Map Creation')

def get_geo_dict(fields,jobs):
    geo_dict = {}
    loc = fields.index('Location')
    for job in jobs:
        if(job[loc] in geo_dict):
            geo_dict[job[loc]]+=1
        else:
            geo_dict[job[loc]] = 1
    return geo_dict

def get_state_dict(geo):
    state_dict = {}
    for i in geo:
        if(i!=""):
            if(";" in i):
                x = i.split("; ")[1]
                if(x in state_dict.keys()):
                    state_dict[x] += geo[i]
                else:
                    state_dict[x] = geo[i]
            else:
                state_dict['IL'] += 2
    return state_dict

def main():

    fields=[]
    jobs=[]
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    words = {}
    geo = {}
    states{O: 'AL', 1, "AK", }    

    with open('loxo.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)

        for job in reader:
            jobs.append(job)

        jobs = remove_char(jobs,punc)

        for x in jobs:
            x[-1] = convert_to_list(x)
            

        words = dict_words(jobs)

        words = sorted(words.items(), key=lambda x: x[1], reverse=True)

        geo = get_geo_dict(fields,jobs)
        state = get_state_dict(geo) 
        geo = sorted(geo.items(), key=lambda x: x[1], reverse=True)
        state = sorted(state.items(), key=lambda x: x[1], reverse=True)
        print(state)
    #for i in words:
        #print(i)
    #plot()


main()

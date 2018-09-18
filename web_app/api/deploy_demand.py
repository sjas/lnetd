import networkx as nx
import pandas as pd


def deploy_demand(arr,source,target,demand):
    df = arr
    df['util']=0
    #print df
    d3js_links =[]
    #print "panda in function : %s" %df
    df['metric'] = pd.to_numeric(df['metric'], errors='coerce')
    df['index'] = pd.to_numeric(df['index'], errors='coerce')

    g = nx.from_pandas_edgelist(df, 'source', 'target', ['index', 'metric','l_ip','r_ip','util'],create_using =nx.MultiDiGraph())
    paths = list(nx.all_shortest_paths(g, source, target, weight='metric'))
    num_ecmp_paths = len(paths)
    demand_path = demand / int(len(paths))
    ecmp_links = 0
    #print "number of paths: %s" %num_ecmp_paths
    #print "demand per path is : %s " %demand_path
    #print "this are the paths: %s" %paths
    #print "initial list : %s " %d3js_links
    for p in paths:
        #print "All nodes  in path: %s" %p
        u=p[0]
        for v in p[1:]:
            #print "path betwen p[0] si v in p[:1]: %s" %v
            min_weight = min(d['metric'] for d in g[u][v].values())
            #print "u variable:%s" %u
            #print "v variable:%s" %v
            values_g=(g[u][v].values())
            items_g=g[u][v].items()
            #print "g[u][v].values() :%s" %values_g
            #print "g[u][v].items() :%s" %items_g
            for d in values_g:
                if d['metric'] == min_weight:
                    #print "print d :%s" %d
                    ecmp_links = ecmp_links +1
                    #d3js_links.append(d)
            #print "number of ECMP links between nodes :%s" %ecmp_links
            #print "demand for each links is : %s" %(int(demand)/int(ecmp_links))
            for d in values_g:
                if d['metric'] == min_weight:
                    #print "d before : %s" %d
                    #d['util'] = int(d['util']) + int(demand_path)/int(ecmp_links)
                    d['util'] = int(demand_path)/int(ecmp_links)
                    #print "d after : %s" %d
                    #print "----\nentry d after util added : %s" %d
                    #print "list before append:\n%s" %d3js_links
                    d3js_links.append(d)
                    #print "list after append:\n%s" %d3js_links
            #print "----end for this path list after for d in values :\n %s" %d3js_links
            ecmp_links = 0
            u=v
    #print "resulting list : \n%s" %d3js_links
    df_demand = pd.DataFrame(d3js_links)
    #print "initial panda \n %s " %df
    #print "resulting panda with demand \n %s" %df_demand
    #print "merge pandas on l_ip\n"
    #df_merge = pd.merge(df,df_demand)
    #print "resulting panda \n%s" %df_merge
    #print df_demand
    return df_demand


import os
import glob
import pandas as pd
import numpy as np

dataset = 'StanfordPoliteness'

input_data_path = 'D:/pseudo_labels/data'
output_data_path = 'D:/pseudo_labels/data/slue'

#dts = ['train','tune', 'test']
dts_out = [ 'train', 'dev', 'test']


domains = ['wikipedia','stack-exchange']

data = []
for domain in domains:
    domain_path = input_data_path+"/"+dataset+"/"+domain+".annotated.csv"
    data.append(pd.read_csv(domain_path,index_col=0))
data = pd.concat(data)

# random split
msk = np.random.rand(len(data)) < 0.9
train = data[msk]
devtest = data[~msk]
msk = np.random.rand(len(devtest)) < 0.5
dev = devtest[msk]
test = devtest[~msk]
print(len(train), len(dev), len(test))


# write to files
for dt_out,d in zip(dts_out, [train, dev, test]):
    dataset_path = output_data_path+"/"+dataset+"/"+dt_out+".tsv"
    with open(dataset_path, "w", encoding="utf-8") as fout:
        for index, row in d.iterrows():
            text = row.Request.replace('\r',' ').replace('\n',' ').strip()
            fout.write('{}\t{}\t{}\t{}\n'.format(index,row.Id,text,row[-1]))
print("train, test files created!")

# for dt,dt_out in zip(dts,dts_out):
    # fout = open(os.path.join('../slue_data',dataset,'{}.tsv'.format(dt_out)),'w')
    # for domain in domains:
        # for label in ['formal','informal']:
            # with open(os.path.join('../slue_data/', dataset, domain, dt,label)) as f:
                # for line in f:
                    # line = line.strip()
                    # fout.write('{}\t{}\n'.format(line, label))
 #    fout.close()


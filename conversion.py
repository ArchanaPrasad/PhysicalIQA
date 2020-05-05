import json


def createJson(inpfile1, inpfile2, outfile):

    f1 = open(inpfile1)
    o = open(outfile, 'w')
    filenames = [inpfile1, inpTfile2]
    allfiles = []
    for path in filenames:
        with open(path, 'r') as f:
            file = f.readlines()
            allfiles.append(file)

    eachData = {}
    x = 0
    for i in f1:
        j = eval(i)
        eachData['id'] = j['id']
        eachData['premises'] = [j['goal']]
        eachData['choices'] = [j['sol1'], j['sol2']]
        eachData['gold_label'] = int(allfiles[1][x])
        o.write(json.dumps(eachData))
        o.write("\n")
        x += 1
    f1.close()


# inpTfile1 = "data/train.jsonl"
# inpTfile2 = "data/train-labels.lst"
# outTfile = "data/final_train.jsonl"
inpTfile1 = "data/dev.jsonl"
inpTfile2 = "data/dev-labels.lst"
outTfile = "data/final_dev.jsonl"
createJson(inpTfile1, inpTfile2, outTfile)

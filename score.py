import sys

gold_file = sys.argv[1]
pred_file = sys.argv[2]

# Load the gold standard
gold = {}
for line in open(gold_file):
    record, string, entity = line.strip().split('\t', 2) #record is the document id, string is the entity name, 
                                                         #entity is the freebase id
    gold[(record, string)] = entity
n_gold = len(gold)
print('Gold entities: %s' % n_gold)

# Load the predictions
pred = {}
for line in open(pred_file):
    record, string, entity = line.strip().split('\t', 2)
    pred[(record, string)] = entity
n_predicted = len(pred)
print('Linked entities: %s' % n_predicted)

# Evaluate predictions
n_correct = sum( int(pred[i]==gold[i]) for i in set(gold) & set(pred) )
print('Correct mappings: %s' % n_correct)

# Calculate scores
precision = float(n_correct) / float(n_predicted)
print('Precision: %s' % precision )
recall = float(n_correct) / float(n_gold)
print('Recall: %s' % recall )
f1 = 2 * ( (precision * recall) / (precision + recall) )
print('F1: %s' % f1 )

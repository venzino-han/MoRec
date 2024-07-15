import os

root_data_dir = '../../'

dataset = 'dataset/MIND'
behaviors = 'mind_60w_users.tsv'
news = 'mind_60w_items.tsv'
logging_num = 4
testing_num = 1

# bert_model_load = 'bert-base-uncased'
bert_model_load = 'bert-base-uncased'
bert_model_load = 'roberta-base'
freeze_paras_before = 0
news_attributes = 'title'

mode = 'train'
item_tower = 'modal'

epoch = 150
load_ckpt_name = 'None'


l2_weight_list = [0.01]
drop_rate_list = [0.1]
batch_size_list = [32]
lr_list_ct = [
    (1e-4, 5e-5), 
    # (5e-5, 5e-5)
    ]
embedding_dim_list = [512]

from slack import send_message

try:
    for l2_weight in l2_weight_list:
        for batch_size in batch_size_list:
            for drop_rate in drop_rate_list:
                for embedding_dim in embedding_dim_list:
                    for lr_ct in lr_list_ct:
                        lr = lr_ct[0]
                        fine_tune_lr = lr_ct[1]
                        label_screen = '{}_bs{}_ed{}_lr{}_dp{}_L2{}_Flr{}'.format(
                            item_tower, batch_size, embedding_dim, lr,
                            drop_rate, l2_weight, fine_tune_lr)
                        run_py = "CUDA_VISIBLE_DEVICES='0' \
                                python3 \
                                run.py --root_data_dir {}  --dataset {} --behaviors {} --news {}\
                                --mode {} --item_tower {} --load_ckpt_name {} --label_screen {} --logging_num {} --testing_num {}\
                                --l2_weight {} --drop_rate {} --batch_size {} --lr {} --embedding_dim {} \
                                --news_attributes {} --bert_model_load {}  --epoch {} --freeze_paras_before {}  --fine_tune_lr {}".format(
                            root_data_dir, dataset, behaviors, news,
                            mode, item_tower, load_ckpt_name, label_screen, logging_num, testing_num,
                            l2_weight, drop_rate, batch_size, lr, embedding_dim,
                            news_attributes, bert_model_load, epoch, freeze_paras_before, fine_tune_lr)
                        os.system(run_py)
except Exception as e:
    error_message = f"Error: {e}"
    send_message(error_message)

send_message(f"{bert_model_load} based end2end seqrec Training is done!")

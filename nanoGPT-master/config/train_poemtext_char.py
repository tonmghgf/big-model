out_dir = 'out-poemtext-fast'
eval_interval = 250
eval_iters = 100
log_interval = 10

always_save_checkpoint = False

dataset = 'poemtext'
gradient_accumulation_steps = 1
batch_size = 16      # 大幅缩小
block_size = 128     # 大幅缩小

n_layer = 2          # 模型变小
n_head = 2
n_embd = 128
dropout = 0.1

learning_rate = 2e-3
max_iters = 5000
lr_decay_iters = 5000
min_lr = 1e-4
beta2 = 0.99

dtype = "float16"    # 开启 GPU 加速关键！
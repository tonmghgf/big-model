# nanoGPT 文本生成实验

这是一个基于 `nanoGPT` 的小型文本生成项目，我围绕两个方向做了实践：

1. 使用 Shakespeare 数据集训练字符级语言模型，生成带有莎士比亚风格的英文文本。
2. 使用自定义中文小说语料训练小型 GPT，尝试生成具有《斗罗大陆》叙事风格的文本。

项目的目标不是追求超大参数规模，而是从数据处理、模型训练到采样生成，完整走通一个轻量级 GPT 的训练流程，理解语言模型的基本工作方式。

## 项目亮点

- 基于 Andrej Karpathy 的 `nanoGPT` 框架进行本地训练与实验。
- 包含英文字符级建模实验，适合快速验证训练流程。
- 包含中文自定义语料实验，可迁移到小说、诗词、台词等不同文本风格任务。
- 保留了训练输出权重与相关 notebook，方便复现实验过程。

## 项目结构

```text
.
├─ nanoGPT-master/                # nanoGPT 主体代码
│  ├─ config/
│  │  ├─ train_shakespeare_char.py
│  │  └─ train_poemtext_char.py
│  ├─ data/
│  │  ├─ shakespeare_char/        # Shakespeare 字符级数据
│  │  └─ poemtext/                # 自定义中文语料
│  ├─ out-shakespeare-char/       # 莎士比亚实验输出
│  └─ out-poemtext-fast/          # 中文风格实验输出
├─ 1.ipynb                        # Word2Vec 相关练习
├─ 2.ipynb                        # PyTorch Word2Vec 训练实验
├─ 3.ipynb                        # 其他实验记录
├─ requirements.txt               # 环境依赖
└─ README.md
```

## 实验一：莎士比亚文本生成

这个实验使用 `nanoGPT-master/data/shakespeare_char` 中的数据，采用字符级建模方式训练一个小型 GPT。

对应配置文件：

- `nanoGPT-master/config/train_shakespeare_char.py`

配置特点：

- `block_size = 256`
- `n_layer = 6`
- `n_head = 6`
- `n_embd = 384`
- `max_iters = 5000`

这个实验的优点是数据小、训练快、结果直观，非常适合用来理解：

- 字符级语言模型如何建模上下文
- GPT 如何根据历史 token 预测下一个 token
- 训练完成后如何通过采样生成连续文本

## 实验二：斗罗大陆风格 GPT

第二个实验使用自定义中文文本语料，目标是训练一个能够模仿《斗罗大陆》文本风格的小型 GPT。

对应配置文件：

- `nanoGPT-master/config/train_poemtext_char.py`

对应数据目录：

- `nanoGPT-master/data/poemtext/`

目前仓库中的这套流程已经包含：

- 文本语料读取
- 训练集 / 验证集划分
- token 编码
- `train.bin` 与 `val.bin` 的生成
- 基于 `nanoGPT` 的训练与采样

如果要切换成《斗罗大陆》语料，核心思路是将原始文本放入自定义数据目录，并按同样流程完成预处理，再使用训练配置启动训练。这样模型虽然规模不大，但已经能够学习特定语料中的常见措辞、人物称呼、叙事节奏和风格特征。

## 环境配置

建议使用 `conda` 创建环境，Python 版本以 `3.9` 为主。

```bash
conda create -n nanogpt python=3.9
conda activate nanogpt
pip install torch torchvision torchaudio
pip install tiktoken numpy transformers datasets tqdm
```

如果希望严格参考当前仓库环境，也可以查看：

- `requirements.txt`

## 运行方式

### 1. 训练莎士比亚生成模型

```bash
cd nanoGPT-master
python train.py config/train_shakespeare_char.py
```

### 2. 采样生成莎士比亚风格文本

```bash
cd nanoGPT-master
python sample.py --out_dir=out-shakespeare-char
```

### 3. 训练中文风格模型

```bash
cd nanoGPT-master
python train.py config/train_poemtext_char.py
```

### 4. 采样生成中文风格文本

```bash
cd nanoGPT-master
python sample.py --out_dir=out-poemtext-fast
```

## 我的收获

通过这个项目，我系统实践了一个轻量级 GPT 的完整流程，包括：

- 数据集准备与清洗
- 文本编码与二进制数据构建
- GPT 模型配置调整
- 训练过程监控与参数调优
- 训练后文本生成效果观察

同时，我也更直观地理解了“小模型 + 特定语料”在风格模仿任务中的价值。即使不是超大模型，只要语料和任务足够聚焦，模型依然可以生成具有明显风格特征的文本。

## 后续优化方向

- 将中文语料正式替换为完整的《斗罗大陆》文本并重新清洗。
- 增大训练步数与上下文长度，提升生成连贯性。
- 调整采样参数，如 `temperature` 和 `top_k`，改善文本多样性。
- 尝试从字符级建模升级到更适合中文的分词或子词建模。
- 增加生成样例展示与 loss 曲线，可用于课程汇报或项目展示。

## 致谢

本项目基于 Andrej Karpathy 开源的 `nanoGPT` 实现完成，在此表示感谢。

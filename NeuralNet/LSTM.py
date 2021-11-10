from tensorflow.keras.layers import Input,LSTM,Dense 
from tensorflow.keras.models import Model,load_model 
from tensorflow.keras.utils import plot_model
from tensorflow.metrics import accuracy
# from tensorflow.keras.metrics import top_k_categorical_accuracy
import pandas as pd
import numpy as np

N_UNITS = 256 #LSTM 单元中隐藏层节点数 
BATCH_SIZE = 64 #网络训练时每个批次的大小 
EPOCH = 200 #训练的 epoch 数 ，训练次数
NUM_SAMPLES = 1000 #训练数据数量，即样本条数 
data_path = 'cmn_zhsim.txt' #训练数据路径(根据的路径设置)

df = pd.read_table(data_path,header=None).iloc[:NUM_SAMPLES,:,] 
df.columns=['inputs','targets'] 
#将每句中文句首加上'\t'作为起始标志，句末加上'\n'作为终止标志 
df['targets'] = df['targets'].apply(lambda x: '\t'+x+'\n') 
#英文句子列表 
input_texts = df.inputs.values.tolist() 
#中文句子列表 
target_texts = df.targets.values.tolist() 
#确定中英文各自包含的字符。df.unique()直接取 sum 可将 unique 数组中的各个句子拼接成 一个长句子 
input_characters = sorted(list(set(df.inputs.unique().sum()))) 
target_characters = sorted(list(set(df.targets.unique().sum())))
#输入数据的时刻 t 的长度，这里为最长的英文句子长度 
INUPT_LENGTH = max([len(i) for i in input_texts]) 
#输出数据的时刻 t 的长度，这里为最长的中文句子长度 
OUTPUT_LENGTH = max([len(i) for i in target_texts]) 
#每个时刻进入 encoder 的 lstm 单元的数据 xt 的维度，这里为英文中出现的字符数 
INPUT_FEATURE_LENGTH = len(input_characters) 
#每个时刻进入 decoder 的 lstm 单元的数据 xtxt 的维度，这里为中文中出现的字符数 
OUTPUT_FEATURE_LENGTH = len(target_characters)

encoder_input = np.zeros((NUM_SAMPLES,INUPT_LENGTH,INPUT_FEATURE_LENGTH))
decoder_input = np.zeros((NUM_SAMPLES,OUTPUT_LENGTH,OUTPUT_FEATURE_LENGTH)) 
decoder_output = np.zeros((NUM_SAMPLES,OUTPUT_LENGTH,OUTPUT_FEATURE_LENGTH))

#构建英文字符集的字典 
input_dict = {char:index for index,char in enumerate(input_characters)} 
#键值调换 
input_dict_reverse = {index:char for index,char in enumerate(input_characters)} 
#构建中文字符集的字典 
target_dict = {char:index for index,char in enumerate(target_characters)} 
#键值调换 
target_dict_reverse = {index:char for index,char in enumerate(target_characters)}

# 对句子进行字符级 one-hot 编码，将输入输出数据向量化 #encoder 的输入向量 one-hot 
# 形成二进制向量（位置为1，其余为0，位数为总字符数，如字母表则26 + 1（空格）） - 二维数组
for seq_index,seq in enumerate(input_texts): 
    for char_index, char in enumerate(seq): 
        encoder_input[seq_index,char_index,input_dict[char]] = 1

#decoder 的输入输出向量 one-hot, 训练模型时 decoder 的输入要比输出晚一个时间步，这样才能对输出监督 
for seq_index,seq in enumerate(target_texts): 
    for char_index,char in enumerate(seq): 
        decoder_input[seq_index,char_index,target_dict[char]] = 1.0 
        if char_index > 0: 
            decoder_output[seq_index,char_index-1,target_dict[char]] = 1.0

# 每条句子经过对字母转换成 one-hot 编码后，生成了 LSTM 需要的三维输入[n_samples, timestamp, one-hot feature]

def create_model(n_input,n_output,n_units): 
    #训练阶段 
    #encoder - 编码器
    #encoder 输入维度 n_input 为每个时间步的输入 xt 的维度，这里是用来 one-hot 的英文 字符数
    encoder_input = Input(shape = (None, n_input))
    #n_units 为 LSTM 单元中每个门的神经元的个数，return_state 设为 True 时才会返回最后 时刻的状态 h,c 
    encoder = LSTM(n_units, return_state=True) 
    #保留下来 encoder 的末状态作为 decoder 的初始状态 
    _,encoder_h,encoder_c = encoder(encoder_input) 
    encoder_state = [encoder_h,encoder_c]

    #decoder - 解码器
    #decoder 的输入维度为中文字符数 
    decoder_input = Input(shape = (None, n_output))
    #训练模型时需要 decoder 的输出序列来与结果对比优化，故 return_sequences 也要设 为 True 
    decoder = LSTM(n_units,return_sequences=True, return_state=True)
    #在训练阶段只需要用到 decoder 的输出序列，不需要用最终状态 h.c 
    decoder_output, _, _ = decoder(decoder_input,initial_state=encoder_state)
    #输出序列经过全连接层得到结果 
    decoder_dense = Dense(n_output,activation='softmax') 
    decoder_output = decoder_dense(decoder_output)
    
    #生成的训练模型 
    #第一个参数为训练模型的输入，包含了 encoder 和 decoder 的输入，第二个参数为模型的输出，包含了 decoder 的输出 
    model = Model([encoder_input,decoder_input],decoder_output)
    
    #推理阶段，用于预测过程 
    #推断模型—encoder，预测时对序列 predict，生成的 state 给 decoder 
    encoder_infer = Model(encoder_input,encoder_state)
    #推断模型-decoder 
    decoder_state_input_h = Input(shape=(n_units,)) 
    decoder_state_input_c = Input(shape=(n_units,))
    decoder_state_input = [decoder_state_input_h, decoder_state_input_c] #上个时刻的 状态 h - 隐藏层节点状态,c - 特征量
    
    decoder_infer_output, decoder_infer_state_h, decoder_infer_state_c = decoder(decoder_input,initial_state=decoder_state_input) 
    decoder_infer_state = [decoder_infer_state_h, decoder_infer_state_c] #当前时刻得到 的状态
    
    decoder_infer_output = decoder_dense(decoder_infer_output)#当前时刻的输出
    #参数输入和输出；输入：input+前一个状态的 state_input,输出：output+state_output 
    decoder_infer = Model([decoder_input] + decoder_state_input, [decoder_infer_output] + decoder_infer_state) 
    
    # 准确率
    acc, acc_op = accuracy(decoder_output, decoder_infer_output)
    
    return model, encoder_infer, decoder_infer, acc_op

model_train, encoder_infer, decoder_infer, acc = create_model(INPUT_FEATURE_LENGTH, OUTPUT_FEATURE_LENGTH, N_UNITS)

# 动量、自适应学习率增加收敛速度；交叉熵损失函数
model_train.compile(optimizer='adam', loss='categorical_crossentropy')
#查看模型结构 
model_train.summary()
# 英文字符总数62个， 中文字符数754个，LSTM隐藏节点256个

# 编码器推理模型
encoder_infer.summary()

# 解码器推理模型
decoder_infer.summary()

# 模型训练
# 输入：编码器、解码器输入；解码器输出；单次训练的规模；总训练次数；训练集分出0.2part给验证集
# 成品api接口，可以完成：分批，乱序，制作迭代，等一些列操作；
model_train.fit([encoder_input,decoder_input],decoder_output,batch_size=BATCH_SIZE, epochs=EPOCH,validation_split=0.2)

def predict_chinese(source,encoder_inference, decoder_inference, n_steps, features): 
    #先通过推理 encoder 获得预测输入序列的隐状态 
    state = encoder_inference.predict(source) #第一个字符'\t',为起始标志 
    predict_seq = np.zeros((1,1,features)) 
    predict_seq[0,0,target_dict['\t']] = 1
    
    output = ''
    
    #开始对 encoder 获得的隐状态进行推理 
    #每次循环用上次预测的字符作为输入来预测下一次的字符，直到预测出了终止符
    for i in range(n_steps): #n_steps 为句子最大长度
        #给 decoder 输入上一个时刻的 h,c 隐状态，以及上一次的预测字符 predict_seq
        yhat,h,c = decoder_inference.predict([predict_seq]+state)
        #注意，这里的 yhat 为 Dense 之后输出的结果，因此与 h 不同 
        #每次预测都是最后一个中文字符
        char_index = np.argmax(yhat[0,-1,:]) 
        char = target_dict_reverse[char_index] 
        output += char
        #更新 state，本次状态做为下一次的初始状态继续传递 
        state = [h,c]
        #前一状态的输出结果会作为下一状态的输入信息 
        predict_seq = np.zeros((1,1,features)) 
        predict_seq[0,0,char_index] = 1
        if char == '\n':
            #预测到了终止符则停下来 
            break
        
    return output

for i in range(100,200): 
    test = encoder_input[i:i+1,:,:] #i:i+1 保持数组是三维 
    out = predict_chinese(test,encoder_infer,decoder_infer,OUTPUT_LENGTH,OUTPUT_FEATURE_LENGTH) 
    print(input_texts[i]) 
    print(out)

print("acc: " + str(acc))
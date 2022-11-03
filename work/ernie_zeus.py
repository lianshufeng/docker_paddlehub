import paddlehub as hub

# 加载模型
model = hub.Module(name='ernie_zeus')

# 自由问答
result = model.answer_generation(
    text='杜鹃花怎么养？' 
)

print(result)
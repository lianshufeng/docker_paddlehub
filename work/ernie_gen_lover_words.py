import paddlehub as hub

module = hub.Module(name="ernie_gen_lover_words")

test_texts = ['我是一只没有水的鱼']
results = module.generate(texts=test_texts, use_gpu=True, beam_width=5)
for result in results:
    print(result)
    
import paddlehub as hub

# 在模型定义时，可以通过设置line=4或8指定输出绝句或律诗，设置word=5或7指定输出五言或七言。
# 默认line=4, word=7 即输出七言绝句。

test_texts = ['张亚军帅得飞起']


module = hub.Module(name="ernie_gen_acrostic_poetry", line=8, word=7)


results = module.generate(texts=test_texts, use_gpu=True, beam_width=5)
for result in results:
    print(result)
#下面我们安装并导入ernie_vilg模块
import paddlehub as hub
ernie_vilg_module = hub.Module(name='ernie_vilg')

results = ernie_vilg_module.generate_image(text_prompts="鲨鱼 蜜蜂", style="油画", output_dir='./ernievilg_output')

'''
Author: physico
Date: 2022-11-02 14:17:08
LastEditTime: 2022-11-02 21:19:01
FilePath: /mmengine/Registry_detective.py
Description: 
Function List: 
'''
import subprocess
def shell_output(command):
    _result = subprocess.getoutput(command)
    # 执行失败不需要特殊处理，因为该方法无法判断失败成功，只负责将结果进行返回
    return _result  # 返回执行结果，但是结果返回的是一个str字符串（不论有多少行）

def find_target(target):
    COMMAND = f"grep  -r -n '{target}' --include='*.py' ./  "
    _result_list = shell_output(COMMAND).split("\n")
    _result = [i for i in _result_list if "Registry_detective" not in i]
    return _result 

TARGET_LIST = [
    'Registry', 'RUNNERS', 'RUNNER_CONSTRUCTORS', 'HOOKS', 'DATASETS',
    'DATA_SAMPLERS', 'TRANSFORMS', 'MODELS', 'WEIGHT_INITIALIZERS',
    'OPTIMIZERS', 'OPTIM_WRAPPER_CONSTRUCTORS', 'TASK_UTILS',
    'PARAM_SCHEDULERS', 'METRICS', 'MODEL_WRAPPERS', 'OPTIM_WRAPPERS', 'LOOPS',
    'VISBACKENDS', 'VISUALIZERS', 'LOG_PROCESSORS', 'EVALUATOR',
]

TARGET = "@VISUALIZERS"
print(find_target(TARGET))

for i in TARGET_LIST:
    import pprint
    print(i)
    pprint.pprint(find_target("@"+i))
    print("\n")

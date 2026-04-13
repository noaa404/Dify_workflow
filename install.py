#!/usr/bin/env python3
"""
Qwen3-ASR 一键安装脚本
Qwen3-ASR-1.7B/Qwen3-ASR-0.6B 

https://huggingface.co/Qwen/Qwen3-ASR-0.6B
https://www.text-to-speech.cn/

"""

import sys
import os
import subprocess
import json

PYENV_ROOT = os.path.expanduser("~/.pyenv")
PYTHON_VERSION = "3.12.0"

def run(cmd, **kwargs):
    """运行命令"""
    return subprocess.run(cmd, shell=True, **kwargs)

def check_pyenv():
    """检查 pyenv 是否安装"""
    result = run("which pyenv", capture_output=True)
    if result.returncode == 0:
        print("✓ pyenv 已安装")
        return True
    return False

def install_pyenv():
    """安装 pyenv"""
    print("安装 pyenv...")
    run("curl https://pyenv.run | bash", check=True)
    print("✓ pyenv 安装完成")
    print("\n请执行以下命令后重新运行安装脚本:")
    print('  export PATH="$HOME/.pyenv/bin:$PATH"')
    print('  eval "$(pyenv init -)"')
    sys.exit(0)

def setup_pyenv_env():
    """设置 pyenv 环境变量"""
    os.environ["PYENV_ROOT"] = PYENV_ROOT
    os.environ["PATH"] = f"{PYENV_ROOT}/bin:{os.environ.get('PATH', '')}"

def install_python():
    """用 pyenv 安装 Python 3.12"""
    setup_pyenv_env()
    
    # 检查是否已安装
    result = run(f"pyenv versions | grep {PYTHON_VERSION}", capture_output=True)
    if result.returncode == 0:
        print(f"✓ Python {PYTHON_VERSION} 已安装")
        return
    
    print(f"安装 Python {PYTHON_VERSION} ...")
    run(f"pyenv install {PYTHON_VERSION}", check=True)
    print(f"✓ Python {PYTHON_VERSION} 安装完成")

def get_python_path():
    """获取 pyenv 安装的 Python 路径"""
    return f"{PYENV_ROOT}/versions/{PYTHON_VERSION}/bin/python3"

def check_cuda():
    """检查 CUDA 是否可用"""
    print("检查 CUDA...")
    # 先安装 torch 才能检查
    return True  # 暂时跳过，安装完依赖后再检查

def select_option(title, options):
    """选择选项"""
    print(f"\n{title}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    
    while True:
        choice = input("\n请输入数字选择: ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return idx, options[idx]
        except ValueError:
            pass
        print("请重试")

def create_venv(python_path):
    """创建虚拟环境"""
    venv_path = "./venv"
    if os.path.exists(venv_path):
        print("✓ 虚拟环境已存在")
        return venv_path
    
    print("创建虚拟环境...")
    run(f"{python_path} -m venv {venv_path}", check=True)
    print("✓ 虚拟环境创建完成")
    return venv_path

def install_deps(venv_path):
    """安装依赖"""
    pip = os.path.join(venv_path, "bin", "pip")
    print("安装依赖...")
    run(f"{pip} install -U qwen-asr[vllm] modelscope", check=True)
    print("✓ 依赖安装完成")

def check_cuda_real(venv_path):
    """真实检查 CUDA"""
    python = os.path.join(venv_path, "bin", "python")
    script = """
import torch
if torch.cuda.is_available():
    print(f"✓ CUDA 可用: {torch.cuda.get_device_name(0)}")
else:
    print("✗ CUDA 不可用")
"""
    result = run(f"{python} -c '{script}'")
    return result.returncode == 0

def download_model(venv_path, version):
    """下载模型"""
    python = os.path.join(venv_path, "bin", "python")
    model_name = f"Qwen/Qwen3-ASR-{version}"
    local_dir = f"./models/Qwen3-ASR-{version}"
    
    if os.path.exists(local_dir):
        print(f"✓ 模型已存在: {local_dir}")
        return local_dir
    
    print(f"下载模型 {model_name}...")
    os.makedirs("./models", exist_ok=True)
    
    script = f"""
from modelscope import snapshot_download
snapshot_download('{model_name}', local_dir='{local_dir}')
print('下载完成')
"""
    run(f"{python} -c '{script}'", check=True)
    print(f"✓ 模型下载完成: {local_dir}")
    return local_dir

def save_config(model_path, port):
    """保存配置"""
    config = {
        "model_path": model_path,
        "port": port,
        "host": "0.0.0.0"
    }
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)
    print("✓ 配置已保存到 config.json")

def main():
    print("=" * 50)
    print("Qwen3-ASR 一键安装")
    print("=" * 50)
    
    # 1. 检查/安装 pyenv
    print("\n【检查 pyenv】")
    if not check_pyenv():
        install_pyenv()
    
    setup_pyenv_env()
    
    # 2. 安装 Python 3.12
    print("\n【安装 Python 3.12】")
    install_python()
    python_path = get_python_path()
    
    # 3. 检查 CUDA
    print("\n【环境检查】")
    check_cuda()
    
    # 4. 选择模型
    _, version = select_option("选择模型版本:", ["0.6B (需要 4GB 显存)", "1.7B (需要 8GB 显存)"])
    version = "0.6B" if "0.6B" in version else "1.7B"
    print(f"已选择: {version}")
    
    # 5. 创建虚拟环境
    print("\n【环境准备】")
    venv_path = create_venv(python_path)
    
    # 6. 安装依赖
    install_deps(venv_path)
    
    # 7. 检查 CUDA（安装完 torch 后）
    print("\n【检查 CUDA】")
    has_cuda = check_cuda_real(venv_path)
    if not has_cuda:
        print("\n CUDA 不可用，服务启动后无法使用 GPU")
    
    # 8. 下载模型
    print("\n【模型下载】")
    model_path = download_model(venv_path, version)
    
    # 9. 保存配置
    print("\n【保存配置】")
    save_config(model_path, 8000)
    
    # 10. 完成
    print("\n" + "=" * 50)
    print("安装完成!")
    print("=" * 50)
    print(f"\n手动启动:")
    print(f"  source venv/bin/activate")
    print(f"  qwen-asr-serve {model_path} --host 0.0.0.0 --port 8000")

if __name__ == "__main__":
    main()

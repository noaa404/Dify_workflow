# Dify Workflow CLI

> 原项目地址 https://github.com/Akabane71/dify-workflow-cli
> CLI-Anything 包装器 https://github.com/HKUDS/CLI-Anything/tree/main/dify-workflow/agent-harness

> dify-workflow-cli/agent-harness/DIFY_WORKFLOW.md
## 安装

```bash
创建虚拟环境

# 1. 上游 CLI
pip install "dify-ai-workflow-tools @ git+https://github.com/Akabane71/dify-workflow-cli.git@main"

# 2. 包装器
cd dify-workflow/agent-harness
pip install -e .
```


```bash
# 帮助
cli-anything-dify-workflow --help


- 上游 CLI 提供核心功能（创建、编辑、验证 Dify 工作流）
- 本项目是 CLI-Anything 生态的包装器，方便 AI 发现使用
- 本地文件编辑，不直接连接 Dify 服务器

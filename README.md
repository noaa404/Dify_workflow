# Dify\_workflow

> 工具环境配置 + dify-DSL工作流示例

***

## 目录

- [项目简介](#项目简介)
- [项目结构](#项目结构)
- [安装说明](#安装说明)
  - [Qwen3-ASR-0.6B](#qwen3-asr-06b)
  - [ragflow](#ragflow)
  - [Dify Workflow CLI](#dify-workflow-cli)

***

## 项目简介

Dify + RAGflow + Qwen3-ASR

CLI-Anything -> Dify

***

## 项目结构

```

├── README.md                          # 项目说明文档
├── install.py                         # Qwen3-ASR-0.6B 安装程序
├── dify-workflow-cli-install.py       # Dify Workflow CLI 安装程序
├── images                        # 项目图片资源
├── RAGFLOW_SETUP.md                   # RAGFlow 安装
├── .gitignore   
├── dify-workflow-cli/                 # Dify Workflow CLI 源码
│   └── agent-harness/                 # Agent Harness 包装器
│       ├── setup.py                   # 包安装配置
│       ├── MANIFEST.in                # 打包清单
│       ├── DIFY_WORKFLOW.md           # 工作流文档
│       │
│       ├── cli_anything/              # CLI Anything 主模块
│       └── cli_anything_dify_workflow.egg-info/   # 包元数据
│
└── [其他目录/文件...]
```

***

## 安装说明

### Qwen3-ASR-0.6B
ASR模型

| 属性   | 信息                                           |
| ---- | -------------------------------------------- |
| 模型地址 | <https://huggingface.co/Qwen/Qwen3-ASR-0.6B> |
| 安装程序 | [install.py](./install.py)                   |

安装步骤：

```bash
python install.py
```

### ragflow

| 属性    | 信息                                      |
| ----- | --------------------------------------- |
| 项目地址  | <https://github.com/infiniflow/ragflow> |
| Setup | [RAGFLOW\_SETUP.md](./RAGFLOW_SETUP.md) |

### Dify Workflow CLI
dify cli化，使用ai进行dify工作流迭代

| 属性               | 信息                                                                            |
| ---------------- | ----------------------------------------------------------------------------- |
| 原项目              | <https://github.com/Akabane71/dify-workflow-cli>                              |
| CLI-Anything 包装器 | <https://github.com/HKUDS/CLI-Anything/tree/main/dify-workflow/agent-harness> |
| 安装程序             | [dify-workflow-cli-install.py](./dify-workflow-cli-install.py)                |

安装步骤：

```bash
python dify-workflow-cli-install.py
```

***


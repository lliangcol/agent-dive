# Graphify 问题排查记录

## 问题：PowerShell 中 `/graphify .` 不适用

- 发现时间：2026-06-10
- 当前状态：待本机验证
- 影响范围：Windows PowerShell 用户

### 现象

README 提醒 PowerShell 中应使用 `graphify .`，不要使用 `/graphify .`。在 PowerShell 中，前导 `/` 容易被当作路径分隔符或参数前缀，导致命令解释不符合助手 slash command 语义。

### 环境

- 操作系统：Windows / PowerShell
- 运行时版本：待验证
- 项目版本 / Commit：`5504c84324fc9249eb4c9d0cca86da7140250032`
- 关键依赖：`graphifyy`

### 复现步骤

1. 在 PowerShell 中尝试 `/graphify .`。
2. 对比执行 `graphify .`。
3. 记录错误输出和实际行为。

### 初步判断

- 可能原因：PowerShell 命令解析与 AI 助手 slash command 语义不同。
- 排除项：不是 Graphify 图谱构建本身失败。

### 定位过程

| 步骤 | 操作 | 结果 | 结论 |
|---|---|---|---|
| 1 | 阅读 README PowerShell note | README 明确建议用 `graphify .` | 先按 CLI 方式执行 |

### 解决方案

- 最终处理：Windows PowerShell 下优先使用 `graphify .`。
- 验证命令：待执行。
- 剩余风险：不同 shell 和助手内置命令语义仍需分别记录。

## 问题：PyPI 包名与 CLI 命令名不一致

- 发现时间：2026-06-10
- 当前状态：待本机验证
- 影响范围：安装和 PATH 排查

### 现象

README 写明官方 PyPI 包是 `graphifyy`，但 CLI 命令是 `graphify`。如果误装其他 `graphify*` 包，可能得到错误项目或命令不可用。

### 初步判断

- 可能原因：包名和命令名不同。
- 排除项：不是 GitHub 仓库不存在。

### 解决方案

- 使用 `uv tool install graphifyy` 或 `pipx install graphifyy`。
- 安装后执行 `graphify --help` 或 `graphify --version` 确认命令来源。
- 避免在未确认来源时安装其他同名近似包。

## 问题：私有仓库非代码材料 semantic extraction 的数据边界不清

- 发现时间：2026-06-10
- 当前状态：待源码和配置验证
- 影响范围：私有代码、内部文档、图片、视频、转写内容

### 现象

Graphify 既有本地静态解析，也支持 OpenAI、Anthropic、Gemini、Azure、Bedrock、Ollama 等 backend extras。README 的 Privacy 说明称代码文件通过 Tree-sitter 本地处理，视频 / 音频本地转写，docs、PDF、图片会发往用户配置的 AI assistant / backend。对私有仓库使用前，需要确认非代码材料是否允许外发。

### 初步判断

- 可能原因：semantic extraction 和静态解析是不同阶段，数据外发边界取决于 backend 和输入类型。
- 排除项：不能仅凭 MIT License 判断运行时数据安全。

### 解决方案

- 先阅读 `SECURITY.md` 和 `docs/how-it-works.md`。
- 用公开小仓库做 dry run。
- 私有仓库先禁用或限制 docs、PDF、图片等非代码 semantic extraction，直到确认外发内容。
- 记录 backend、环境变量、输入范围和生成结果。

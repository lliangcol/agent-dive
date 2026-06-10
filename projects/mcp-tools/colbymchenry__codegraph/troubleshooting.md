# CodeGraph 问题排查记录

## 问题：安装后 `codegraph` 命令找不到

- 发现时间：2026-06-10
- 当前状态：未验证
- 影响范围：首次安装和 Windows PowerShell 使用

### 现象

README 提醒安装器会把 `codegraph` 放到 PATH，但不会改变当前 shell，因此安装后当前终端可能仍无法解析命令。

### 解决方案

- 最终处理：重新打开终端后再运行 `codegraph --version`。
- 验证命令：`codegraph --version`
- 剩余风险：企业终端策略可能阻止 PATH 修改。

## 问题：MCP tools 报项目未初始化

- 发现时间：2026-06-10
- 当前状态：未验证
- 影响范围：Agent 已接入但目标仓库没有 `.codegraph/`

### 现象

`src/mcp/server-instructions.ts` 明确把没有 `.codegraph/` 作为限制：项目未初始化时需要运行 `codegraph init -i`。

### 解决方案

```bash
cd your-project
codegraph init -i
codegraph status
```

剩余风险：如果仓库很大，首次索引可能耗时较长。

## 问题：Node 版本不兼容

- 发现时间：2026-06-10
- 当前状态：未验证
- 影响范围：npm 安装、开发源码、SDK 嵌入

### 现象

`package.json` 标注 Node `>=20.0.0 <25.0.0`；`src/bin/codegraph.ts` 对 Node 25+ 和过低版本有硬性检查；README 的 Library Usage 说明嵌入式 API 需要 Node 22.5+ 的 `node:sqlite`。

### 解决方案

- CLI 用户优先使用 README 提供的自包含安装器。
- npm/源码开发用户检查 Node 版本。

```bash
node --version
npm test
```

剩余风险：不同安装路径对运行时要求不同，必须按实际路径验证。

## 问题：索引结果过期或 watcher 不工作

- 发现时间：2026-06-10
- 当前状态：未验证
- 影响范围：编辑后立即查询、sandbox、网络文件系统

### 现象

README 说明 MCP server 使用 watcher 和 debounce 自动同步；`src/mcp/engine.ts` 中 watcher 不可用时会提示运行 `codegraph sync`。工具结果可能出现 pending sync / staleness banner。

### 解决方案

```bash
codegraph status
codegraph sync
```

如果 Agent 工具结果提示某个文件 pending re-index，对该文件使用原始读取或等待自动 sync 后重试。

## 问题：静态解析不能证明运行时行为

- 发现时间：2026-06-10
- 当前状态：客观限制
- 影响范围：动态语言、反射、运行时路由、框架魔法、跨语言桥接

### 初步判断

CodeGraph 的引用解析是静态 best-effort。README 和源码都强调它补充编译器、测试和 linter，而不是替代真实验证。

### 解决方案

- 用 CodeGraph 定位影响面。
- 用项目原生测试、类型检查、集成测试验证行为。
- 对动态调用链保留“待运行验证”标注。

## 问题：文档和源码表述不完全一致

- 发现时间：2026-06-10
- 当前状态：已记录
- 影响范围：理解安装器是否写 instructions 文件

### 现象

`site/src/content/docs/reference/mcp-server.md` 仍写着 installer 会把 guidance 写入 agent instructions file；但当前 README 和 `src/mcp/server-instructions.ts`、`src/installer/targets/codex.ts`、`src/installer/targets/claude.ts` 都显示工具指导由 MCP initialize response 提供，并清理旧 instructions block。

### 解决方案

本次收录以源码和 README 当前状态为准；后续如果要提交上游 issue，可指出 docs reference 页面可能需要同步。

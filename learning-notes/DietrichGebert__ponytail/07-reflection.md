# Ponytail 阶段反思

## 当前收获

Ponytail 的价值不在“让 Agent 说得更短”，而在把工程实现前的取舍顺序固定下来：先判断是否需要实现，再找标准库和平台能力，最后才写最小代码。这套规则如果和证据要求配合好，可以减少 AI 编码常见的过度抽象。

## 当前不足

- 没有真实宿主安装证据，不能证明 Codex 或 Claude Code 中的体验。
- SubagentStart 目前只有源码和本地测试证据，真实宿主中还没验证。
- benchmark 没有复现，现阶段只能引用 upstream 方法和结果边界。

## 对 AgentDive 的启发

AgentDive 收录类似“规则型工具”时，不能只问它是否能完成任务，还要问：

- 它如何被宿主加载。
- 它是否有生命周期 hook。
- 它的规则副本如何防漂移。
- 它的 benchmark 是否有 correctness gate。
- 它是否明确说明不适用边界。

## 下一步

下一步做隔离宿主 smoke。只有真实插件安装、mode 切换和 SubagentStart 注入通过后，才考虑把项目状态提升到 `study-ready`。

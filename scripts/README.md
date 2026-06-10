# Scripts

本目录保存轻量流程说明和后续自动化入口。

当前阶段没有实现真实自动化收录程序。`collect-project.md` 是收录流程规范，用于指导人工或 AI Agent 辅助执行。

已经提供轻量一致性检查脚本：

```bash
python scripts/check-agent-dive.py
```

该脚本只检查仓库文档、元数据、学习进度和证据文件的一致性，不联网、不执行第三方项目命令、不修改文件。

详细使用说明和 Hermes Agent 示例见 [collect-project-usage.md](collect-project-usage.md)。

## 后续脚本原则

- 不引入复杂依赖。
- 默认不修改 `docs/`。
- 写入范围必须限制在当前项目目录、对应学习笔记目录、`PROJECTS.md` 和 `LEARNING_PROGRESS.md`。
- 每次收录或更新必须维护 `meta.json`、`evidence.md` 和 `learning-notes/<owner__repo>/progress.json`。
- 项目状态提升到 `study-ready`、`in-study` 或 `completed` 前必须有 evidence 支撑。
- 第三方源码缓存放入 `.cache/sources/<owner__repo>/`，运行缓存放入 `.cache/runs/<owner__repo>/`。

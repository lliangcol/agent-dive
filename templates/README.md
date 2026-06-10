# Templates

本目录保存 AgentDive 的通用模板，用于项目收录、项目精读、源码阅读、集成实践、问题排查、图解生成、学习任务和收录报告。

## 使用原则

- 模板是起点，不是最终稿。
- 不要删除“依据”“风险”“待验证”类字段。
- 不要把未验证结论写成事实。
- 单项目内容应保存到 `projects/<category>/<owner__repo>/`。
- 学习过程内容应保存到 `learning-notes/<owner__repo>/`。

## 模板清单

| 模板 | 用途 |
|---|---|
| `project-analysis-template.md` | 项目精读主文档 |
| `source-code-reading-template.md` | 源码阅读路线和调用链记录 |
| `integration-guide-template.md` | 集成到本地或业务项目的指南 |
| `troubleshooting-template.md` | 问题排查记录 |
| `learning-todo-template.md` | 分层学习任务清单 |
| `project-evaluation-template.md` | 项目客观评价 |
| `diagram-checklist-template.md` | 图解类型和质量检查 |
| `collect-report-template.md` | 一次收录过程的报告 |

## 通用质量要求

- 项目名称、GitHub 地址、分析日期和分析版本必须明确。
- 运行验证、源码分析、图解结论必须标注依据。
- 推测内容必须写入“待验证”或“人工判断”。
- 不写入账号、密钥、本机绝对路径或私有配置。

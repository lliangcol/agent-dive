# <Project Name> 收录报告

## 使用场景

用于记录一次项目收录过程，说明收录结论、依据、风险、生成文件和待人工确认事项。

## 填写说明

- 收录报告必须保存到对应项目目录。
- Level D 暂不收录的项目也可以保留报告，但不要创建完整项目精读目录。
- 不要把未执行的自动化能力写成已完成。

## 标准结构

### 1. 基本信息

- GitHub 地址：
- 收录时间：
- 项目名称：
- 项目 ID：
- 项目分类：
- 收录等级：
- 当前状态：
- 是否建议收录：
- 收录人 / Agent：

### 2. 收录依据

- 与 AI Agent 的相关性：
- 项目学习价值：
- 工程参考价值：
- 文档和源码可分析性：
- License 初步判断：
- 是否重复收录：

### 3. 风险

- 运行风险：
- 维护风险：
- 安全风险：
- 文档过期风险：
- 结论待验证项：

### 4. 生成文件清单

- [ ] `projects/<category>/<owner__repo>/README.md`
- [ ] `projects/<category>/<owner__repo>/project-analysis.md`
- [ ] `projects/<category>/<owner__repo>/learning-todo-list.md`
- [ ] `projects/<category>/<owner__repo>/collect-report.md`
- [ ] `projects/<category>/<owner__repo>/assets/diagrams/`
- [ ] `learning-notes/<owner__repo>/`
- [ ] `PROJECTS.md` 更新
- [ ] `LEARNING_PROGRESS.md` 更新

### 5. 待人工确认事项

- [ ] License 是否允许引用和学习整理。
- [ ] 核心调用链是否与源码一致。
- [ ] 快速开始是否真实跑通。
- [ ] 图解是否准确。
- [ ] 收录等级是否合适。

### 6. 下一步建议

- 后续行动：

## 待办检查项

- [ ] 已填写 GitHub 地址、收录时间、分类和等级。
- [ ] 已写明是否建议收录。
- [ ] 已列出依据、风险和生成文件。
- [ ] 已列出待人工确认事项。

## 质量检查项

- [ ] 没有生成虚假收录结果。
- [ ] 没有夸大自动化能力。
- [ ] 收录等级与输出要求匹配。
- [ ] 目录 ID 使用 `owner__repo`。

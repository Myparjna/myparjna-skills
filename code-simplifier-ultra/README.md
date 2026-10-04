# Code Simplifier Ultra

版本 2.3.0 聚焦轻量代码精简：在保持有效行为和代码质量的前提下，减少耦合、重复状态、多余封装和理解成本，让开发者与 AI 更容易追踪功能、定位责任和持续修改项目。

## 工作方式

理解实际调用链，找到可以消除的复杂度，按职责完成小批改动，再运行足以发现相关错误的检查。优先收拢分散的业务知识、减少调用方协调和双向依赖；拆文件、增加接口或减少代码行数本身不构成收益。

已授权的精简直接执行；需要用户取舍的候选在回复中说明位置、收益、风险和推荐项。输出简短文字，不生成 HTML 或独立报告，不强制绘图、设计追问或全库扫描。参考资料仅在遇到对应问题时加载。

## 测试与自动检查

测试、CI 步骤及质量阈值也可精简：核实其发现的故障、适用行为和剩余保护，删除没有独立价值的重复项、过时项或绑定实现细节的检查。保留必要的失败路径、安全、兼容与数据保护；项目强制检查按既有规则处理。具体标准见 [验证与测试精简](references/verification-and-reporting.md)。

## 调用

```text
使用 $code-simplifier-ultra 精简订单流程，减少重复状态和多余封装，保持行为。
使用 $code-simplifier-ultra 检查无效测试和重复 CI 步骤，删除没有独立保护价值的项。
使用 $code-simplifier-ultra --survey --broad 简短列出候选，供我选择。
```

原有参数保持兼容：`--simplify` 执行精简，`--review` 单独使用时只读，`--survey` / `--architecture` 调查候选，`--broad` 扩大授权范围的覆盖，`--no-verify` 披露并推迟可执行检查，`--no-report` 返回最短工作结论。明确只读请求优先。

## 维护入口

- [SKILL.md](SKILL.md)：主流程与参数规则。
- [结构判断](references/structural-proof.md)：跨文件删除、消费者和净收益。
- [职责与耦合](references/architecture-survey.md)：模块收敛与调用方负担。
- [行为保持](references/behavior-parity.md)：容易遗漏的等价性要求。
- [评估场景](evals/evals.json)：局部精简、动态消费者、文字候选和测试检查取舍。

范围快照脚本仅辅助记录差异，使用限制见 [范围说明](references/scope-and-context.md)。技能不依赖其他技能、可视化工具或独立评审代理。
## 来源

本次融合 [tt-a1i/simplify-codebase](https://github.com/tt-a1i/simplify-codebase) 和 [mattpocock/skills](https://github.com/mattpocock/skills) 的架构普查、模块设计、设计追问与领域建模方法。固定版本和适配差异见来源记录。

保留既有来源：

- [getsentry/skills](https://github.com/getsentry/skills/blob/main/agents/code-simplifier.md)：行为保持与平衡原则。
- [PaulRBerg/agent-skills](https://github.com/PaulRBerg/agent-skills)：范围冻结、模式、风险与报告。
- [pproenca/dot-skills](https://github.com/pproenca/dot-skills)：简化规则分类。
- [rtk-ai/rtk](https://github.com/rtk-ai/rtk)：项目约束与回归检查。
- [aktsmm/Agent-Skills](https://github.com/aktsmm/Agent-Skills)：触发场景与完成清单。
- simonwong/writing-skills：getsentry agent 的社区变体。

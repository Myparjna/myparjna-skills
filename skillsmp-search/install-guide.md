# Skill 安装指南

搜索到合适的 Skill 后，可通过以下方式安装：

## 方式一：npx skills add（推荐）

```bash
npx skills add <repo> --skill <name>
```

示例：
```bash
npx skills add anthropics/skill-creator --skill skill-creator
npx skills add zkksdk/cocoloop --skill tencentcloud-cvm-skill
```

## 方式二：SkillHub CLI

```bash
skillhub install <name>
```

示例：
```bash
skillhub install tencentcloud-lighthouse-skill
skillhub install tencentcloud-cvm-skill
```

## 安装位置

| 级别 | 路径 | 说明 |
|------|------|------|
| 用户级（默认） | `~/.workbuddy/skills/` | 所有项目共享 |
| 项目级 | `{workspace}/.workbuddy/skills/` | 仅当前项目 |

## 验证安装

安装后重启 Agent 会话，新 Skill 会被自动加载。也可通过 `/skills` 命令查看已安装技能列表。
